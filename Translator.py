import os
import io
import pygame
import textwrap
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from gtts import gTTS
from googletrans import Translator
from PyDictionary import PyDictionary


class App(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        translate_tab = ttk.Notebook(root)
        translate_tab.configure(width=340, height=400)
        self.translate_tab = ttk.Frame(translate_tab)
        translate_tab.add(self.translate_tab, text="Translate Menu")
        translate_tab.grid()
        self.translate_tab.grid_propagate(0)
        self.speak_it = BooleanVar()
        self.languages = {
            'English': 'en', 'Hindi': 'hi', 'Spanish': 'es'
        }
        self.translate_tab_page()

    def translate_tab_page(self):
        self.word_label = Label(self.translate_tab, text="Word")
        self.word_label.grid(row=0, column=0, sticky=W, pady=2)
        self.word_entry = Entry(self.translate_tab, width=35)
        self.word_entry.grid(row=0, column=1, pady=2)
        self.language_lable = Label(
            self.translate_tab, text="In Language translate ")
        self.language_lable.grid(column=0, row=2, pady=5)
        self.language_menu = ttk.Combobox(
            self.translate_tab, values=[*self.languages.keys()])
        self.language_menu.grid(column=1, row=2)
        self.language_menu.current(0)
        self.translate_button = Button(
            self.translate_tab, text="Translate", command=self.translation_function)
        self.translate_button.grid(column=0, row=3, pady=10)
        self.speak_checkbutton = Checkbutton(
            self.translate_tab, text="Speak out", command=self.translation_function)
        self.speak_checkbutton.grid(column=1, row=3)
        self.word_frame = LabelFrame(
            self.translate_tab, text="Word", width=250, height=48)
        self.word_frame.grid(column=0, row=4, columnspan=2)
        self.word_frame.grid_propagate(0)
        self.word_result = Label(self.word_frame, text="")
        self.word_result.grid()
        self.noun_frame = LabelFrame(
            self.translate_tab, text="Noun", width=250, height=90)
        self.noun_frame.grid(column=0, row=5, columnspan=2)
        self.noun_frame.grid_propagate(0)
        self.noun_result = Label(self.noun_frame, text="")
        self.noun_result.grid()
        self.verb_frame = LabelFrame(
            self.translate_tab, text="Verb", width=250, height=90)
        self.verb_frame.grid(column=0, row=6, columnspan=2)
        self.verb_frame.grid_propagate(0)
        self.verb_result = Label(self.verb_frame, text="")
        self.verb_result.grid()

    def translation_function(self):
        word = self.word_entry.get()
        language = self.languages.get(self.language_menu.get())
        noun, verb = self.defined(word)
        try:
            noun = str(*noun[0])
            verb = str(*verb[0])
        except:
            noun = str(noun[0])
            verb = str(verb[0])
        translated_word = self.translate_function_run_data(word, language).text
        translated_noun = self.translate_function_run_data(noun, language).text
        translated_verb = self.translate_function_run_data(verb, language).text
        speakout_thread = threading.Thread(
            target=self.speak_funtion_runner, args=(translated_word, language))
        self.word_result.configure(text=translated_word)
        self.noun_result.configure(text=textwrap.fill(translated_noun, 48))
        self.verb_result.configure(text=textwrap.fill(translated_verb, 48))
        if self.speak_it.get():
            speakout_thread.start()

    def defined(self, word):
        nouns, verbs = [], []
        dictionary = PyDictionary()
        word = self.translate_function_run_data(word, "en").text
        meaning_to_word = dictionary.meaning(word)
        try:
            if meaning_to_word['Noun']:
                nouns.append(meaning_to_word['Noun'][0])
            if meaning_to_word['Verb']:
                verbs.append(meaning_to_word['Verb'][0])
        except:
            nouns.append("Nothing Found")
            verbs.append("Nothing Found")
        return nouns, verbs

    def translate_function_run_data(self, words, language):
        translator = Translator(service_urls=["translate.google.com"])
        translation = translator.translate(words, dest=language)
        return translation

    def speak_funtion_runner(self, text, language):
        with io.BytesIO as file:
            gTTS(text=text, lang=language).write_to_fp(file)
            file.seek(0)
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue


if __name__ == '__main__':
    root = Tk()
    root.title("Translator")
    root.geometry("350x435")
    App(root)
    root.mainloop()
