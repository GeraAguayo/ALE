import pyttsx3

class Voice:
    
    def __init__(self, rate, voice_id):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('voice', self.voices[voice_id].id)

    def setVoiceRate(self, rate):
        self.engine.setProperty('rate',rate)

    def setVoice(self, voice_id):
        self.engine.setProperty('voice', self.voices[voice_id].id)

    def speak(self, text):
        self.engine.say(text)
        print(f'VOICE: {text}')
        self.engine.runAndWait()