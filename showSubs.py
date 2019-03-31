from tkinter import *

# This function will be run every N milliseconds
def get_text(root,val,name):
    # try to open the file and set the value of val to its contents 
    try:
        with open(name,"r") as f:
            val.set(f.readlines()[-1])
    except IOError as e:
        print e
    else:
        # schedule the function to be run again after 1000 milliseconds  
        root.after(1000,lambda:get_text(root,val,name))

root = Tk()
root.minsize(740,400)
eins = StringVar()
data1 = Label(root, textvariable=eins)
data1.config(font=('times', 37))
data1.pack()
get_text(root,eins,"out.txt")
root.mainloop()
