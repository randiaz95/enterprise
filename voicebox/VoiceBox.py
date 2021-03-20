import pyttsx3


class VoiceBox:
    def __init__(self, startup=False, rate=None, volume=None, voice=None):
        self.engine = pyttsx3.init()
        if rate is not None:
            self.engine.setProperty('rate', rate)
        if volume is not None:
            self.engine.setProperty('volume', volume)
        if voice is not None:
            self.engine.setProperty('voice', voice)

        if isinstance(startup, str):
            self.engine.say(startup)
            self.engine.runAndWait()
        elif startup and isinstance(startup, bool):
            self.engine.say("Initiating voice Box")
            self.engine.runAndWait()
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


