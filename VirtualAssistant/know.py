import pyttsx3

say = input()
engine = pyttsx3.init()
if "hello" in say:
    engine.say("hello Nagomi")
    engine.runAndWait()
elif "night" in say:
    engine.say("good night Maru")
    engine.runAndWait()
else:
    engine.say("I don't know!")
    engine.runAndWait()

