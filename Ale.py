from cgitb import text
import pywhatkit 
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
            texto.lower()
            print(texto) 
            
            
    except:
        pass
    return texto

def ALE ():
    texto = escuchar()

    if 'hola' in texto:
        print('Hola Gerardo, me alegro de verte de nuevo')
        decir('Hola Gerardo, me alegro de verte de nuevo')
    elif 'reproduce' in texto:
        cancion = texto.replace('reproduce','')
        print('Reproduciendo ' + cancion)
        decir('Reproduciendo ' + cancion)
        pywhatkit.playonyt(cancion)
    elif 'gracias' in texto:
        print('Es un placer')
        decir('Es un placer')
        exit()
    else:
        print('Intentalo de nuevo')
        decir('Intentalo de nuevo')




while True:
    ALE()



    





