import pyttsx3

target = int(input())

engine = pyttsx3.init("dummy")
engine.setProperty("rate", 1000)

for number in range(target):
    engine.say(str(number))
    engine.runAndWait()
