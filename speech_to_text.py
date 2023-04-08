import spacy
import pyttsx3
import time
import threading
import speech_recognition as sr

en = spacy.load('en_core_web_sm')
sw_spacy = en.Defaults.stop_words

sw_spacy.remove("next")
sw_spacy.remove("name")

class Handeler:
    def __init__(self):
        pass
    
    def Speech_to_text(self):
        text_to_speech = pyttsx3.init()
        r = sr.Recognizer()
        try:
            m = sr.Microphone()
            with m as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                
            return MyText
        except sr.RequestError as e:
            self.say("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            self.say("Did not get it, please try again")

    def say(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    def Process(self, text):
        if text == None:
            return "lol"
        words = [word for word in text.split() if word.lower() not in sw_spacy]
        new_text = " ".join(words)
        return new_text

    def listen(self):
        text_inp = self.Speech_to_text()
        text_corpus = self.Process((text_inp))
        return text_corpus

if __name__ == "__main__":
    input_seq = "Hello"
    ob = Handeler()
    ob.say("hello")
    print(ob.listen())