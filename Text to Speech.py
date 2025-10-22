import speech_recognition
import pyttsx3
from datetime import date, datetime
import time

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

robot_mouth.setProperty('rate', 180)
robot_mouth.startLoop (False)

while (True):
    with speech_recognition.Microphone() as mic:
        print ("Robot: I'm listening!!")
        audio = robot_ear.listen (source = mic)

    print ("Robot: ...")
    try:
        you = robot_ear.recognize_google (audio)
    except:
        you = ""
    print ("You:", you)
    # you = str (input())

    if (you == ""):
        robot_brain = "i can't hear you, try again"
    elif ("bye" in you):
        robot_brain = "See you later"
    elif ("your name" in you):
        robot_brain = "i'm a robot answering your questions"
    elif ("hello" in you):
        robot_brain = "Hello Crystal"
    elif ("day today" in you):
        today = date.today()
        robot_brain = today.strftime ("%A %d %B %Y")
    elif ("time" in you):
        current = datetime.now()
        robot_brain = current.strftime ("%H:%M")
    elif ("my birthday" in you):
        robot_brain = "It's march 15th"
    
    
    elif ("thanks" in you) or ("thank you" in you):
        robot_brain = "you're welcome"
    else:
        robot_brain = "I don't know the answer"
    
    print ("Robot:", robot_brain)
    robot_mouth.say (robot_brain)
    # for i in range(15):
    #     robot_mouth.iterate()
    #     time.sleep(0.1)

    robot_mouth.iterate()
    time.sleep (1.5)
    
    if "bye" in you:
        break

robot_mouth.endLoop()