"""

Libraries used:
    >speech recognition
    >pyttsx3
    >pyaudio
    
INSTRUCTIONS:
Story names will be displayed on the screen which are stored in the database.
Then, user need to give input of story name which he want to listen in form of speech.

NOTE: path(in function 'read') is static, i.e, user need to give path where their stories are saved.
        example- If stories are in 'D' drive in folder named 'stories'. Then,
                    path="D:\\\\stories\\"+val+".txt"
                        Use \\ for \
                
"""
import speech_recognition as sr 
import pyttsx3

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
def read(val):
    path="C:\\\\AI PROJECT STORY TELLING - FABULA\\DATABASE\\"+val+".txt"
    f = open(path, "r")
    text=f.read()# text contains the story
    print(text) # prints the story
    return text # returns the story

def speak(command): 
    engine = pyttsx3.init()# engine is part of pyttsx3 , this is reference  
    # to engine and is responsible for loading all the necessary drivers
    engine.say(command) #speaks text ** command ? **
    engine.runAndWait() # wait till the queue is empty

def intro():
    introFile=read("INTRO") # prints intro
    read("story names") # prints story names
    speak(introFile) # speaks intro

def ask():
    print("\nDo you want to listen another story?\n")
    print("\nEnter Yes/No\n")
    speak("Do you want to listen another story?")
    speak("Enter Yes or No")
    yn=input(print("........"))
    if(yn=="yes" or yn=="Yes" or yn=="YES" or yn=="Y" or yn=="y"):
        Input()
    else:
        s="Thank you for listening!"
        print(s)
        speak(s)
            
def Input():
        speak("Go on, I am listening")
        print("\nwaiting..............\n")
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1) # external noise
            audio = r.listen(source, timeout=1000) # save input to 'audio'
        try:
            MyText=r.recognize_google(audio) # google converts speech to text
            MyText = MyText.lower()
            print("Did you say: "+MyText)
            text=read(MyText) # call to fun. read that returns the story
            speak(text) # text is the story
            ask()
        except sr.RequestError as e: ## *?*
            print("Could not request results; {0}".format(e))
            Input()         
        except sr.UnknownValueError: # speech unintelligible
            print("unknown error occured")
            Input()
        except: # any other error
            print("Unable to understand")
            Input()

intro()
Input()
