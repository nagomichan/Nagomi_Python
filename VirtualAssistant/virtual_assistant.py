import pyttsx3
import sys
import datetime

# while True:
#     say = input()
#     engine = pyttsx3.init()
#     if "hello" in say:
#         engine.say("hello Maru")
#     elif "night" in say:
#         engine.say("good night Maru")
#     elif "exit" in say:
#         engine.say("bye maru")
#         engine.runAndWait()
#         sys.exit()
#     else:
#         engine.say("I don't know!")
#     engine.runAndWait()


while True:
    listense = input("Say something: ")
    engine = pyttsx3.init()
    if "hello" in listense:
        engine.say("hello Maru")
    elif "night" in listense:
        engine.say("good night Maru")
    elif "nagomi" in listense:
        engine.say("my friend")
    elif "today" in listense:
        today = datetime.date.today()
        today.strftime("%B %d, %Y")
        print(today.strftime("%B %d, %Y"))
        engine.say(today)
    elif "exit" in listense:
        sys.exit()
    else:
        engine.say("I don't know!")
    engine.runAndWait()
