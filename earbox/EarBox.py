from voicebox.VoiceBox import VoiceBox
import sounddevice as sd
import numpy as np
import asyncio
import sys


class EarBox:
    def __init__(self, startup=True):
        self.voicebox = VoiceBox(startup="Initiating ear box")
        
    def __record(self, duration, **kwargs):
        loop = asyncio.get_event_loop()
        event = asyncio.Event()
        idx = 0

        def callback(indata, frame_count, time_info, status):
            nonlocal idx
            if status:
                print(status)
            remainder = len(buffer) - idx
            if remainder == 0:
                loop.call_soon_threadsafe(event.set)
                raise sd.CallbackStop
            indata = indata[:remainder]
            buffer[idx:idx + len(indata)] = indata
            idx += len(indata)

        stream = sd.InputStream(callback=callback, 
                                dtype=buffer.dtype,
                                channels=buffer.shape[1], 
                                **kwargs)
        with stream:
            await event.wait()


    def __transform(self):
        pass

    def listen(self, duration=10.0):
        recording = self.__record(duration)
        return self.__transform(recording)