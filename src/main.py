from tkinter import messagebox
import sys
import pyperclip
import re
import deepl
import json

## initialize api
# read api key
with open("api_key.json", "r") as file:
    dict = json.load(file)
API_KEY = dict["key"]

# check api key
if API_KEY == "your_api_key":
    messagebox.showerror('Error', 'Enter your deepl key in [api_key.json]')
    sys.exit()

# initialize
translator = deepl.Translator(API_KEY)

##param
source_lang = 'EN'
target_lang = 'JA'

## main
# get english text
text_raw = pyperclip.paste()

# check empty paste
if text_raw == '':
    messagebox.showerror('Error', 'There is no text on clip bord')
    sys.exit()

# remove paragraph
text = re.sub("\n", " ", text_raw)

# execute translate
result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)

# copy clipbord
pyperclip.copy(result.text)