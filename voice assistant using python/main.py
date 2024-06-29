import tkinter as tk
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command():
    command = entry.get()
    if command:
        response = f"You said: {command}"
        speak(response)
        text.insert(tk.END, response + "\n")
        entry.delete(0, tk.END)

def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        entry.insert(tk.END, command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")

root = tk.Tk()
root.title("Simple Voice Assistant")

frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(frame, width=40, height=10, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text.pack()

scrollbar.config(command=text.yview)

entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack(pady=20)

speak_button = tk.Button(root, text="Speak", command=recognize_speech)
speak_button.pack()

submit_button = tk.Button(root, text="Submit", command=process_command)
submit_button.pack()

root.mainloop()
