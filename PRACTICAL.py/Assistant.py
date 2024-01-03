# Developing a voice assistant using python modules
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time 

def user_spech():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)

        try:
            print("Recognizing..")
            data = recognize.recognize_google(audio)
            return data.lower()
        
        except sr.UnknownValueError:
            print("Not Understand")



def assist_spech(x):
    engine  = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', '150')
    engine.say(x)
    engine.runAndWait()
#The below statement  define the code inside that  should run when the complete python 
#executed directly and not execute when it is imported as a module to other python file     
if __name__ == '__main__':

    assist_spech("Hi, how can I help you.") # calling the assistant function to help the user

    while True:
        voice = user_spech()
        if voice:
            if "how are " in voice :
                greet = "I am fine Vinay, how are you?"
                assist_spech(greet)
                print(greet)
                
            elif "are you" in voice:
                respond = "I am here for you what can I do for?"
                assist_spech(respond)
                print(respond)
            
            elif "time" in voice:
                present = datetime.datetime.now().strftime("%I:%M %p")
                assist_spech(present)
            
            elif "youtube" in voice:
                webbrowser.open("https://www.youtube.com/channel/UCTowQ2L_f2cEn16m1xLxvYg")
# webbrowser module is used to redirect to any media that is given in the path
            elif "chat gpt" in voice:
                webbrowser.open("https://chat.openai.com")

            elif "git hub" in voice:
                webbrowser.open("https://github.com")
            
            elif "joke" in voice:
                joke = pyjokes.get_joke(language="en")
                print(joke)
                assist_spech(joke)
            
            elif 'play song' in voice:
                push = r"C:"# write a songs path here
                songlist = os.listdir(push) # collecting all the songs to one list
                print(songlist)
                song_path = os.path.join(push, songlist[1]) # song started from index zero
                os.startfile(song_path) # playing a song


            elif 'exit' in voice:
                assist_spech("Good Bye! See you soon.")
                break
            time.sleep(6) # taking six seconds after every output to listen again
        
        else:
            assist_spech("Sorry! I can't hear you")
    
   