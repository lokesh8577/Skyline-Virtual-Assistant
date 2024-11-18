import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLib
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# apikey = "b70554742a0a4dd59b5692f948e80c4a"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('text.mp3')    

# Initialize the pygame mixer
    pygame.mixer.init()

# Load the music file (ensure the file exists in the specified path)
    pygame.mixer.music.load("text.mp3")

# Play the music
    pygame.mixer.music.play()

# Keep the program running to let the music play
    while pygame.mixer.music.get_busy():  # Music is still playing
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("text.mp3")      # Waits for the music to finish playing

r = sr.Recognizer()
def process_ai(command):
    api_key = "your api key"
    genai.configure(api_key=api_key)
    command = f"Briefly explain: {command}"
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open linkdin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        speak("opening instagrm")
        webbrowser.open("https://www.instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={Your api key}")   
        if r.status_code == 200:
    # Parse the JSON response
            data = r.json()
    
    # Extract the 'articles' field
            articles = data.get('articles', [])

    # Print only the titles of the articles
        if articles:
            for article in articles:
                speak(article['title'])
                print(article['title'])

        else:
            print("No articles found.") 

    else:
        output = process_ai(command)   
        print(output) 
        speak(output)


if __name__ == "__main__":
    speak("Initializing skyline....")
    
    while True:
        print("Recognizing...")  # Added this inside the loop to indicate recognition attempt
        
        try:
            # Use the same recognizer instance 'recognizer' globally
            with sr.Microphone() as source:
                print("Say something!")
                # recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                
            # Recognize the speech using Google's recognizer
            word = recognizer.recognize_google(audio)
            print(word)
            if word.lower() == "skyline":
                speak("Ya")

                with sr.Microphone() as source:
                    print("Skyline engine start")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)   

                    processCommand(command)
            
        
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
