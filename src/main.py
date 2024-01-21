from ale_voice import Voice
from speech_recon import SpeechRecon
import pywhatkit

def test():

    ale = Voice(150, 2)

    ale.speak("Hola Gerardo")
    ale.setVoiceRate(130)
    voice_id = 0
    ale.setVoice(voice_id)
    ale.speak("ENCUENTROS DE TRAILEROS CACHONDOS CON TRANSEXUALES EN NAUCALPAN")
    ale.setVoice(2)
    ale.setVoiceRate(150)
    ale.speak("Saludos a la driver")



def test_recon():
    sr = SpeechRecon()

    comando = sr.listen()

ale = Voice(150, 2)
sr = SpeechRecon()

def main():


    while True:
        ale.speak("Dime..")
        command = sr.listen()

        if command == "reproduce in euro":
            ale.speak("Reproduciendo Y lloro de Junior H en Youtube")
            pywhatkit.playonyt("Y lloro Junior H")
        if command == "gracias":
            ale.speak("No hay problema")
            quit()
        else:
            ale.speak("Repitelo de nuevo")



main()
        


