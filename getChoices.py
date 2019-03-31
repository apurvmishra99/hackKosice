from tkinter import *
from subprocess import Popen


def start_transcribe():
    arg1 = " "+speaker_lang.get()
    arg2 = " "+listener_lang.get()
    Popen("python main.py"+arg1+arg2)
    Popen("python showSubs.py")
    


root = Tk()


root.title('Configuration')
root.geometry('1000x500')
speaker_lang = StringVar()
listener_lang = StringVar()

lblSpeaker = Label(root, text = 'Language of the speaker:')
lblSpeaker.grid(row=0, column=0, padx=0, pady=10)
lblSpeaker.config(font=('Times', 30))
entSpeaker = Entry(root, textvariable = speaker_lang).grid(row = 0, column = 1)

lblListener = Label(root, text='Language of the listener:')
lblListener.grid(row=1, column=0, padx=0, pady=10)
lblListener.config(font=('Times', 30))
entSpeaker = Entry(root, textvariable=listener_lang).grid(row=1, column=1)

b = Button(root, text='Start Program',
           command=start_transcribe).grid(row=3, column=1)

root.mainloop()
