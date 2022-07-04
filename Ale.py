import pyttsx3
import speech_recognition as sr

#Configuracion de la voz de Ale
voz = pyttsx3.init()
voz.setProperty('rate',150)

def decir(texto):
    voz.say(texto)
    voz.runAndWait()


decir('Hola Gerardo, me da gusto verte de nuevo')

print('test finalizado !')