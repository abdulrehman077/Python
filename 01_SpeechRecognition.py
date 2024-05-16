import speech_recognition as sr
import pyaudio

#Creating Intrence for Recognizer

recognizer = sr.Recognizer()

#Capture Audio Input from Microphone

with sr.Microphone() as source:
    print("Listensing....")
    audio_data=recognizer.listen(source)

#Perform Speech Recognition Using Google Api
try:
    text=recognizer.recognize_google(audio_data)
    print("You Said",text)
except sr.UnknownValueError:
    print("Sorry Could not Understand Audio.")
except sr.RequestError as e :
    print("Error : Could not request result from Google Speech Recognition Service.")



