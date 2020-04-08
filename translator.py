import os
from translate import Translator

translator = Translator(to_lang="te")

try:
    with open("translate.txt","r") as my_file:
        for line in my_file:
            translated_line = translator.translate(line)
            print(translated_line)
            mode = "a" if os.path.exists("translated.txt") else "w"
            with open("translated.txt", mode) as translated_file:
                translated_file.write(translated_line + "\n")
except FileNotFoundError:
    print("fie doesn\'t exist ")
