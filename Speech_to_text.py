#!/usr/bin/env python3

import time
import threading
import speech_recognition as sr


def main():
    # Initialize the recognizer and microphone objects
    r = sr.Recognizer()
    m = sr.Microphone()

    # Adjust for ambient noise
    with m as source:
        r.adjust_for_ambient_noise(source)

    # Define a flag to indicate if the program is still running
    running = True

    # Define the callback function to handle speech recognition results
    def callback(recognizer, audio):
        nonlocal running

        try:
            # Use Google Speech Recognition to recognize the audio
            result = recognizer.recognize_google(audio)
            print("You said: " + result)

            # Check if the user wants to stop the program
            if result.lower() in ["stop", "exit"]:
                running = False
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Start a separate thread to handle speech recognition
    stop_listening = r.listen_in_background(m, callback)

    # Wait for the user to say "stop" or "exit"
    while running:
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            # Cleanly exit the program if the user presses Ctrl+C
            running = False

    # Stop listening and wait for the background thread to finish
    stop_listening(wait_for_stop=True)


if __name__ == '__main__':
    main()
