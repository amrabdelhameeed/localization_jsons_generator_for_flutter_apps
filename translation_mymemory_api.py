# this method with mymemory Api

import json
import requests
import os
import tkinter as tk

root = tk.Tk()
root.title("Create localization JSON files for your Flutter app")
root.geometry("420x500")

def translate():
    input_words = input_field.get("1.0", "end-1c").split("\n")
    en = {}
    ar = {}
    
    if os.path.isfile("en.json"):
        with open('en.json', 'r', encoding='utf-8') as f:
            en = json.load(f)
    
    if os.path.isfile("ar.json"):
        with open('ar.json', 'r', encoding='utf-8') as f:
            ar = json.load(f)
    
    for word in input_words:
        if word != "" and word not in en:
            url = f"https://api.mymemory.translated.net/get?q={word}&langpair=en|ar"
            response = requests.get(url)
            response_json = response.json()
            
            if 'responseData' in response_json and 'translatedText' in response_json['responseData']:
                translation = response_json['responseData']['translatedText']
                if "," in translation:
                    ar[word] = translation.split(',')[0].strip()
                else:
                    ar[word] = translation
                en[word] = word
                
    
    with open('en.json', 'w', encoding='utf-8') as f:
        json.dump(en, f, ensure_ascii=False)
    
    with open('ar.json', 'w', encoding='utf-8') as f:
        json.dump(ar, f, ensure_ascii=False)
    
    output_field.delete("1.0", "end")
    output_field.insert("end", f"Translation complete. Files saved in:\n{os.getcwd()}")
    output_field.insert("end", "\n----------------english--------------\n")
    output_field.insert("end", json.dumps(en, indent=4))
    output_field.insert("end", "\n----------------arabic--------------\n")
    output_field.insert("end", json.dumps(ar, indent=4,ensure_ascii=False))

input_label = tk.Label(root, text="Enter English words to translate, separated by newlines:")
input_label.pack(pady=10)

input_field = tk.Text(root, width=40, height=10)
input_field.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=5)

output_field = tk.Text(root)
output_field.pack(pady=5)

root.mainloop()
