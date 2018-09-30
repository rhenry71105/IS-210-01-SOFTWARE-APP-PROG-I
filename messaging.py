from Tkinter import *
import tkMessageBox



def close_window():
    windows.destroy()
    exit()
def PopUpMsg():
    entryBox = e1Box.get()
    if len(entryBox) > 1:
        tkMessageBox.showinfo("Success!", "You Typed: '%s'." % (entryBox))
    else:
        tkMessageBox.showerror("Warning!", "You Cannot Submit Without Entering The Data.")

DEFAULT_FONT = "SYSTEM"
windows = Tk()
windows.geometry("500x500+200+200")
windows.resizable(height="False", width="False")
windows.title("Rickardo's Messaging App.")

l1 = Label(windows, text="Enter A Message:", font=DEFAULT_FONT)
l1.pack(padx="5", pady="5")
e1Box = Entry(windows, font=DEFAULT_FONT)
e1Box.pack()

Button1 = Button(windows, text="Submit", command=PopUpMsg, font=DEFAULT_FONT)
Button1.pack(padx="20", pady="20")

Button1 = Button(windows, text="Exit", command=close_window, font=DEFAULT_FONT)
Button1.pack(padx="20", pady="20")
    
windows.mainloop()
