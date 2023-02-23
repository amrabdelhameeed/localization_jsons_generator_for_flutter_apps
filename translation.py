import json
import requests
import os
import tkinter as tk
root = tk.Tk()
root.title("create localization json files for your flutter app")
root.geometry("420x500")
# api_key = 'AIzaSyAd_uvZdGqIB09AxDD_qlMSFK16PKMHTUw'
def translate():
    input_words = input_field.get("1.0", "end-1c").split("\n")
    en = {}
    ar = {}
    if(os.path.isfile("en.json")):
        with open('en.json', 'r', encoding='utf-8') as f:
            en = json.load(f)
    if(os.path.isfile("ar.json")):
        with open('ar.json', 'r', encoding='utf-8') as f:
            ar = json.load(f)
    for word in input_words:
        if word != "" and word not in en:
            url = f'https://translation.googleapis.com/language/translate/v2?key={input_api.get("1.0",tk.END)}&source=en&target=ar&q={word}'
            response = requests.get(url)
            translation = response.json()['data']['translations'][0]['translatedText']
            en[word] = word
            ar[word] = translation
    with open('en.json', 'w', encoding='utf-8') as f:
        json.dump(en, f, ensure_ascii=False)
    with open('ar.json', 'w', encoding='utf-8') as f:
        json.dump(ar, f, ensure_ascii=False)
    output_field.delete("1.0", "end")
    output_field.insert("end", f"Translation complete. Files saved in :\n{os.getcwd()}")
    output_field.insert("end", "\n----------------english--------------\n")
    output_field.insert("end", en)
    output_field.insert("end", "\n----------------arabic--------------\n")
    output_field.insert("end", ar)
    with open('api_key.json', 'w', encoding='utf-8') as f:
        json.dump({"0":input_api.get("1.0",tk.END).replace('\n', '')}, f, ensure_ascii=False)
input_label = tk.Label(root, text="enter your google api key : ")
input_label.pack(pady=1)
input_api = tk.Text(root, width=40, height=1)
if(os.path.isfile("api_key.json")):
    with open('api_key.json', 'r', encoding='utf-8') as f:
        input_api.insert("1.0",json.load(f)["0"])
input_api.pack(pady=1)
input_label = tk.Label(root, text="Enter English words to translate, separated by newlines:")
input_label.pack(pady=10)
input_field = tk.Text(root, width=40, height=10)
input_field.pack(pady=5)
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=5)
output_field = tk.Text(root,)
output_field.pack(pady=5)
root.mainloop()