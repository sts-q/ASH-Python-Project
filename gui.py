from tkinter import *
from tkinter import ttk



root = Tk()
root.title("Centered Label and Button")

# Make the window resizable
root.geometry("300x200")  # You can set any initial size you like
root.minsize(200, 150)  # Set a minimum window size for resizing



page1 = Frame(root)
page2 = Frame(root)

def show_page1():
    page2.pack_forget()
    page1.pack(expand=True)

def show_page2():
    page1.pack_forget()
    page2.pack(expand=True)

frame1 = Frame(page1)
frame1.pack(expand=True)

# Create a label widget
label = Label(frame1, text="Anki Flashcards")
label.pack(expand=True)

# Create a button widget
button = Button(frame1, text="Let's Start", command=show_page2)
button.pack(expand=True)


frame2 = Frame(page2)
frame2.pack(expand=True)

# Create a label widget
label = Label(frame2, text="page 2")
label.pack(expand=True)

# Create a button widget
button = Button(frame2, text="Go Back", command=show_page1)
button.pack(expand=True)

#basic setup for navigation
show_page1()

# Run the Tkinter event loop
root.mainloop()

#for navigation, setup a page which can just be a frame, and then pack and unpack the frame as needed
#frame is equivalent to div in html
