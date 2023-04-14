import time
from gtts import gTTS
import playsound
import speech_recognition as sp
import webbrowser
import random


def listen_command():
    r = sp.Recognizer()
    with sp.Microphone() as micro:
        print("Скажите Вашу команду: ")
        audio = r.listen(source=micro)
    try:
        speech = r.recognize_google(audio_data=audio, language="ru")
        print(f"Было сказано: {speech}")
        return speech

    except sp.UnknownValueError:
        return "Ничего не понял :("


def open_browser():
    webbrowser.open_new_tab("https://yandex.ru")


def you_are_welcome():
    a = "Всегда пожалуйста"
    b = "Рада стараться!"
    flag = random.randint(1, 2)
    if flag == 1:
        say_message(a)
    else:
        say_message(b)


def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Здравствуйте, мастер!")
    if "пока" in message:
        say_message("До скорых встреч, мастер!")
        exit()
    if "открой интернет" in message:
        open_browser()
    if "спасибо" or "благодарю" or "ух ты" in message:
        you_are_welcome()
    else:
        say_message("Данная команда ещё не прописана моим создателем, я его обязательно попрошу это исправить!")


def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = f"_audio_{str(time.time())}_{str(random.randint(0, 100000))}.mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print(message)

if __name__ == "__main__":
    while True:
        command = listen_command()
        do_this_command(command)
