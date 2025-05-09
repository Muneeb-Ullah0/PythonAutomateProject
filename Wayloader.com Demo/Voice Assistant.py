import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print(f"User said: {command}")
    except:
        command = ""
    return command

def run_assistant():
    command = listen_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'search' in command:
        topic = command.replace('search', '')
        talk(f'Searching for {topic}')
        pywhatkit.search(topic)
    elif 'stop' in command:
        talk("Goodbye!")
        exit()
    else:
        talk("MY name is muneeb ullah and I am your assistant. How can I help you? You can ask me to play a song, check the time, search for something, or stop the assistant.")

talk("Hello! I am your assistant. How can I help you?")
while True:
    run_assistant()
