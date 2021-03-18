import pyttsx3


class VoiceBox:
    def __init__(self, startup=False, rate=None, volume=None, voice=None):
        engine = pyttsx3.init()
        if rate is not None:
            engine.setProperty('rate', rate)
        if volume is not None:
            engine.setProperty('volume', volume)
        if voice is not None:
            engine.setProperty('voice', voice)

        if startup:
            engine.say("Initiating voice Box")
            engine.runAndWait()
        
        


