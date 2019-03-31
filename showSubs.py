from tkinter import *

# This function will be run every N milliseconds


def get_text(root, val, name):
    # try to open the file and set the value of val to the last line of the file
    try:
        with open(name, "r") as f:
            val.set(f.readlines()[-1])
    except IOError as e:
        print(e)
    else:
        # schedule the function to be run again after 1000 milliseconds
        root.after(1000, lambda: get_text(root, val, name))


root = Tk()
root.title("Transcription")
eins = StringVar()
root.overrideredirect(True)
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Turn off the window shadow
root.wm_attributes("-alpha", 0.0)
# Set the root window background color to a transparent color
root.config(bg='white')
root.geometry("+700+300")
get_text(root, eins, "out.txt")
label = Label(root, textvariable=eins)
# Set the label background color to a transparent color
label.config(bg='white', font=('times', 37))
label.pack()
# root.wm_attributes('-alpha', 0.9)
#root.minsize(740, 400)

# data1 = Label(root,, bg='white') 
# data1.config(font=('times', 37))
# data1.pack()
root.mainloop()
