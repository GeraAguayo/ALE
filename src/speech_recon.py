import speech_recognition as sr
import pyaudio

class SpeechRecon:
    
    def __init__(self):
        self.listener = sr.Recognizer()
    
    def listen(self):
        try:
            with sr.Microphone() as source:
                print('Escuchando...')
                voice_input = self.listener.listen(source)
                command = self.listener.recognize_google(voice_input)
                command = command.lower()
                print(f'ALE: Eschuché -> {command}')
                return command
        except sr.UnknownValueError:
            response = 'No te he entendido'
            print(f'ALE: {response}')
            return response
        except Exception as e:
            response = f'Ha ocurrido un error: {e}'
            print(f'ALE: {response}')
            return response


