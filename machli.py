import pyttsx3
import time

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

numDict = {1:"ek", 2:"do", 3:"teen", 4:"chaar", 5:"paanch", 6:"shey", 7:"saat", 8:"aanth", 9:"nau", 10:"dus"}

engine = pyttsx3.init()
LANGUAGE = "en_IN"
GENDER = "VoiceGenderFemale"

change_voice(engine, LANGUAGE, GENDER)

LIMIT = 5
delay = time.sleep(0.5)
print("Starting Machli game with limit = {}".format(LIMIT))

for i in range(LIMIT+1):
    temp = i
    while (temp != 0):
        print("{} machli".format(i))
        engine.say(numDict[i] + " mashlee")
        engine.runAndWait()
        delay
        temp -= 1
    temp = i
    while (temp != 0):
        print("Paani mein gayi")
        engine.say("Paaani may gayi")
        engine.runAndWait()
        delay
        temp -= 1
    temp = i
    while (temp != 0):
        print("Chapaak!")
        engine.say("Shapaaak")
        engine.runAndWait()
        delay
        temp -= 1

engine.stop()