from dis import Instruction
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def close_window(self):
        self.root.destroy()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello sir, I am your voice assistance. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    
    while True:
    # if 1:
        instruction = takeCommand().lower()



        try:
                if 'who are you' in instruction:
                    speak('I am your personal voice Assistant')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction:
                    time = datetime.datetime.now().strftime('%I: %M')
                    speak('current time is' + time)

                elif 'open google' in instruction:
                    speak('Opening Google')
                    webbrowser.open('google.com')

                elif 'open youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('youtube.com')

                elif 'open facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('facebook.com')

                elif 'open python geeks' in instruction:
                    speak('Opening PythonGeeks')
                    webbrowser.open('pythongeeks.org')

                elif 'open linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('linkedin.com')

                elif 'open gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('gmail.com')

                elif 'open stack overflow' in instruction:
                    speak('Opening Stack Overflow')
                    webbrowser.open('stackoverflow.com')

                elif 'shutdown' in instruction:
                    speak('I am shutting down')
                    close_window()

                elif 'wikipedia' in instruction:
                    speak('Searching Wikipedia...')
                    query = instruction.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'play music' in instruction:
                    music_dir = 'F:\Music'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak('I did not understand, can you repeat again')
        except:
            speak('Waiting for your response')
            

        # Logic for executing tasks based on query
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)

        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")

        # elif 'open google' in query:
        #     webbrowser.open("google.com")

        # elif 'open gmail' in query:
        #     webbrowser.open("gmail.com")   


        # elif 'play music' in query:
        #     music_dir = 'F:\Music'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'what is the time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        #     speak(f"Sir, the time is {strTime}")

        # elif 'open visual studio' in query:
        #     codePath = "C:\\Users\\om\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        