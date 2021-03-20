testing_matrix = {"voice_box": False, "ear_box": True}




### TEST VOICE BOX WITH BASE STARTUP ###
if testing_matrix["voice_box"]:
    from voicebox.VoiceBox import VoiceBox

    c3p0_voice = VoiceBox(startup=True)
    c3p0_voice.speak("Hello mate")
### END TEST VOICE BOX ###


### TEST EAR BOX WITH BASE STARTUP ###

if testing_matrix["ear_box"]:
    from earbox.EarBox import EarBox

    c3p0_ear = EarBox(startup=False)
    output = c3p0_ear.listen()
    c3p0_ear.speak("I HEARD YOU MY MASTER!")
    c3p0_ear.speak(f"You said {output}")

### END TEST EAR BOX ###