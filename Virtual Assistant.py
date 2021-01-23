import speech_recognition as sr # speech recognition module
import pyttsx3 #text to speech module
import pywhatkit  #To search a song on YT
import datetime  #to show date and time
import wikipedia # search in wikipedia
import pyjokes # for making a jokes
import PyPDF2

listener = sr.Recognizer() # Recognize listner voice
engine = pyttsx3.init() #intialize text to speech
voices =  engine.getProperty('voices') # To change asistant voice

#engine.say('I am alexa! what can I do for u')
#engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening......')
            voice = listener.listen(source) # listen voice
            command = listener.recognize_google(voice) # speech to text using goole API
            command = command.lower()
            if 'alexa' in command:
                command =  command.replace('alexa', '') # Remove alexa with empty string
                print(command)
    except:
        pass
    return command

def run_alexa():
    command =  take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =  datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who is' in command:
        person =  command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing =  command.replace('who is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('I have an headache')
    elif 'are you single' in command:
        talk('I am in a relationship with my duty')
    elif 'i love you' in command:
        talk('i love you too')
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    elif 'read' in command:

        book = open('CGM Notes Unit 1.pdf', 'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        print(pages)


        speaker = pyttsx3.init()

        page = pdfreader.getPage(1)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


    else:
        talk('Please say again')

while True:
    run_alexa()