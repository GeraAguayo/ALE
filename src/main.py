from ale_voice import Voice

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

str = '''
          _      ______ 
     /\   | |    |  ____|
    /  \  | |    | |__   
   / /\ \ | |    |  __|  
  / ____ \| |____| |____ 
 /_/    \_\______|______|
                         
                         
'''
print(str)
test()

