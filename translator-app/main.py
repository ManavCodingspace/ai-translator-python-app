from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr 




languages = GoogleTranslator().get_supported_languages(as_dict=True)

def change(text,src,dest ):
    translator = GoogleTranslator(source=src, target = dest)
    return translator.translate(text)
    
def data():
    s = combo_sor.get()
    d = combo_dest.get()
    msg = Sor_txt.get(1.0, END).strip()
   
    if msg == "":
        messagebox.showwarning("wARNING", "Please enter text to translate")
        return
    
    try:
     textget = change(text=msg, src=s, dest=d)

    except Exception as e:
     messagebox.showerror("Error", f"An error occurred: {e}")
    
    else:
     dest_txt.delete(1.0, END)   
     dest_txt.insert(END, textget)

def speak():
   text = dest_txt.get(1.0, END).strip()

   if text == "":
      messagebox.showwarning("Warning", "No text to speak")
      return
   engine = pyttsx3.init()
   engine.say(text) 
   engine.runAndWait()   




def swaplanguages():
    src_lang = combo_sor.get()
    dest_lang = combo_dest.get()

    combo_sor.set(dest_lang)
    combo_dest.set(src_lang)

    # swap text also 
    source_text = Sor_txt.get(1.0, END)
    dest_text = dest_txt.get(1.0, END)

    Sor_txt.delete(1.0, END)
    Sor_txt.insert(END, dest_text)  

    dest_txt.delete(1.0, END)
    dest_txt.insert(END, source_text) 

def copy_text():
   translated_text = dest_txt.get(1.0,END)

   if translated_text.strip() == "":
      messagebox.showwarning("Warning", "No text to copy")
      return
   root.clipboard_clear()
   root.clipboard_append(translated_text)

   messagebox.showinfo("Copied", "Translated text copied to clipboard")
   
def listen():
   recognizer = sr.Recognizer() 

   with sr.Microphone() as source:
    messagebox.showinfo("Listening", "Please speak now")
    audio = recognizer.listen(source)
      
    try:
     text = recognizer.recognize_google(audio)
     Sor_txt.delete(1.0,END)
     Sor_txt.insert(END, text)
      
    except Exception as e:
     messagebox.showerror("Error", "Could not understand audio") 

def clear_text():
   Sor_txt.delete(1.0, END)
   dest_txt.delete(1.0, END)
   combo_sor.set("auto")
   combo_dest.set("english")

#def character_count():
   #text = Sor_txt.get(1.0, END).strip()
   #count = len(text)
   #messagebox.showinfo("Character Count",f"Number of characters:{count} ")         
         
def update_character_count(event=None):
   text = Sor_txt.get(1.0, END)
   count = len(text.strip())
   charac_txt.config(text=f"Characters: {count}")




root = Tk()
root.title("Smart Translator")
root.geometry("600x600")
root.configure(bg="#f0f2f5")

lab_txt = Label(root, text="Translator", font=("Time New Roman", 35, "bold"), bg="#f4f6f9", fg="#2c3e50")
lab_txt.place(x=100, y=40, height=49, width=300)

frame  = Frame(root).pack(side=BOTTOM)

voice_btn = Button(root, text="🎤 Speak", bg = "#e67e22", fg = "white", font = ("Segoe UI", 10, "bold"), relief =GROOVE, command = listen)
voice_btn.place(x = 450, y = 95, width= 90, height = 35)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), bg="#f0f2f5", fg="Black")
lab_txt.place(x=100, y=110, height=20, width=300)

clear_btn = Button(root, text = "Clear", bg = "#c0392b", fg="white", font=("Segoe UI", 10, "bold"), relief=FLAT, command=clear_text)
clear_btn.place(x=10, y=95, height=35, width=80)

Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"),wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

Sor_txt.bind("<KeyRelease>", update_character_count)
Sor_txt.bind("<ButtonRelease>", update_character_count)


list_text = list(languages.keys())
list_text.insert(0, "auto") #add auto detect at top 

combo_sor = ttk.Combobox(frame, values=list_text)
combo_sor.place(x=10, y=300, height=40, width=150)
combo_sor.set("auto")

button_change = Button(frame, text="Translate", bg = "#2c3e50", fg = "White", font = ("Segoe UI", 12, "bold"), relief=FLAT, command=data)
button_change.place(x=170, y=300, height=40, width=150)

swap_btn = Button(frame, text="🔄" , command=swaplanguages)
swap_btn.place(x=425, y=338, height=30, width = 40)

combo_dest = ttk.Combobox(frame, values=list_text)
combo_dest.place(x=330, y=300, height=40, width=150)
combo_dest.set("english")

copy_btn = Button(root, text ='Copy', bg="#27ae60", fg="white",font=("Segoe UI", 10, "bold"), relief=FLAT, command=copy_text)
copy_btn.place(x=200, y=560, height=35, width=100)

speak_btn = Button(root, text= "Listen", bg="#8e44ad", fg="white", font=("Segoe UI", 10, "bold"),relief=RAISED, command = speak)
speak_btn.place(x=320, y=560, height=35, width=100)

lab_txt = Label(root, text="Destination Text", font=("Time New Roman", 20, "bold"), bg="#f0f2f5", fg="Black")
lab_txt.place(x=100, y=370, height=20, width=300)

charac_txt = Label(root, text="Characters: 0", font=("Time New Roman", 12, "bold"), bg="#f0f2f5", fg ="Black")
#charac_txt = Button(root, text="Character Count", font=("Time New Roman", 12 , "bold"), bg="#f0f2f5", fg ="Black", relief = FLAT, command= character_count)
charac_txt.place(x=10, y=560, height=35, width=150)

dest_txt = Text(frame, font=("Time New Roman", 20, "bold"),wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)
dest_txt.insert(END, Text)



root.mainloop()