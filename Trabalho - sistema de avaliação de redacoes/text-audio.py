import pyttsx3
from pyttsx3 import engine

voz = pyttsx3.init()
voice = voz.getProperty('voice')

texto = input('Escreva o seu texto:')

voz.say(texto)
voz.runAndWait()