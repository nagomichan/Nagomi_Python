import speech_recognition

robot = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    print("Say Something...")
    audio = robot.listen(mic)
    print("listen success...")
text = robot.recognize_google(audio)
print(text)
