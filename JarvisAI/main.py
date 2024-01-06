import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from config import apikey
import datetime
# import random
# import numpy as np


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Mudassir: {query}\n Jarvis:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ***********************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a try catch block
    # print(response["choice"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2334344356443)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     print("Enter the word you want to speak it out by computer")
#     s = input()
#     speaker.speak(s)
def say(text):
    speaker.speak(f" {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: add a feature to play a specific song
        if "open music" in query:
            musicPath = "C:/Users/mudas/Downloads/Unison-Aperture-NCS-Release.mp3"
            os.system(f"start {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/mudas/Downloads/Unison-Aperture-NCS-Release.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open compass".lower() in query.lower():
            os.system(f"start C:/Users/mudas/AppData/Local/MongoDBCompass/MongoDBCompass.exe")

        elif "open code".lower() in query.lower():
            os.system(f"start C:/Users/mudas/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            charStr = ""

        else:
            print("Chatting...")
            chat(query)



            # say(query)
