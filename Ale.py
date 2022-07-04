from cgitb import text
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

#Configuracion de la voz de Ale
voz = pyttsx3.init()
voz.setProperty('rate',150)

def decir(texto):
    voz.say(texto)
    voz.runAndWait()

def escuchar():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            decir('Escuchando')
            audio = r.listen(source)
            texto = r.recognize_google(audio)
            print(texto) 
            texto.lower()
            
    except:
        print('Intentalo de nuevo')
        decir('Intentalo de nuevo')
        pass
    
    return texto







