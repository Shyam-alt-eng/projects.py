import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api = "7d27973512164a7482aa28c891ca93a8"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com/")    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com/")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
        if response.status_code == 200:
        # Parse the JSON response
            data = response.json()
            # Extract the articles
            articles = data['articles']
            # Print the headlines
            for article in articles:
                speak(article['title'])

    

if __name__ == "__main__":
    speak("initializing jarvis.....")
    while True:

        r = sr.Recognizer()
        try:
        
                with sr.Microphone() as source:
                    print("listening...")
                    recognizer.adjust_for_ambient_noise(source,duration = 1)
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                word = r.recognize_google(audio)
                print("recognizing.....")
                print(word)
                if(word.lower() == "jarvis"):
                    speak("yes boss")
                    with sr.Microphone() as source:
                        print("jarvis Activated....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)

                    
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

