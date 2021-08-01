'''
Speech recognition

sudo apt-get install portaudio19-dev
pip3 install pyaudio
pip3 install SpeechRecognition

source:
https://pythonprogramminglanguage.com/speech-recognition/
API only allows 50 sentences a day at 1 sentence at a time.

Visit my blog for more snippets like this
stevepython.wordpress.com
'''
import speech_recognition as sr

# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now:")
    audio = r.listen(source)

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
