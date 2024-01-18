from ale_voice import Voice
from speech_recon import SpeechRecon
import speech_recognition as sr
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

test_recon()


