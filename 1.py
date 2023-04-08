import spacy
import pyttsx3
import time
import threading
import speech_recognition as sr

en = spacy.load('en_core_web_sm')
sw_spacy = en.Defaults.stop_words
class Speech_to_Text():

    def __init__(self,input_sequence):
        self.input_sequence = input_sequence
    
    def Speech_to_text(self):
        text_to_speech = pyttsx3.init()
        r = sr.Recognizer()
        Run = True
        try:
            m = sr.Microphone()
            with m as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                # MyText = Process(MyText)
                print(MyText)
                
            return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")

    def text_to_Speech(self,text):
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(text)
            engine.runAndWait()
            engine.stop()

    def Process(self,text):
        if text == None:
            return "lol"
        words = [word for word in text.split() if word.lower() not in sw_spacy]
        new_text = " ".join(words)
        print(new_text)
        return new_text

    def main(self):
        while(True):
            text_inp = self.Speech_to_text()
            print(type(text_inp))
            text_corpus = self.Process((text_inp))
            print(text_corpus)
            text_output = self.text_to_Speech(self.input_sequence)
            break

input_seq = "Hello This is Pratyush Raj. We are working on a project for hackfest of IIT ISM DHANBAD .  This is a google chrome tool that works on helping blind people able to shop through real time voice integration "
ob = Speech_to_Text(input_sequence=input_seq) 
ob.main()
    


