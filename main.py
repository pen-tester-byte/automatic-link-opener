# make sure to enter changes in line 18

import webbrowser
import time
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("Opening...")
    speak("Opening")
    
    # Enter the link you want to open at the place of google.com
    webbrowser.open("google.com")

    print("Opened!!!")
    speak("Opened")
    
    print("3")
    speak("3")
    time.sleep(1)

    print("2")
    speak("2")
    time.sleep(1)

    print("1")
    speak("1")
    time.sleep(1)

    main()

if __name__ == "__main__":
    print("Created by Shriyans Sudhi")
    speak("Created by Shriyans Sudhi")

    print("Website: https://shriyanssudhi.ml")
    speak("Website: https://shriyanssudhi.ml")

    print("Github: https://github.com/Shriyanss")
    speak("Github: https://github.com/Shriyanss")

    main()
