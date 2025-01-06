from tkinter import *
from tkinter import ttk, font as tkFont
from tkextrafont import Font

root = Tk()
root.title("Centered Label and Button")

# Make the window resizable
root.geometry("500x400")  # You can set any initial size you like
root.minsize(200, 150)  # Set a minimum window size for resizing


custom_font = Font(file="Minecraft.ttf", family="Minecraft")
fontL = tkFont.Font(family="Minecraft", size=24)
fontM = tkFont.Font(family="Minecraft", size=18)
page1 = Frame(root)
page2 = Frame(root)

def show_page1():
    page2.pack_forget()
    page1.pack(expand=True)

def show_page2():
    page1.pack_forget()
    page2.pack(expand=True)

def update_label():
    label.config(text="button clicked")
    

frame1 = Frame(page1)
frame1.pack(expand=True, fill='both', side='top')
frame2 = Frame(page1, pady=20)
frame2.pack(expand=True, fill='both', side='bottom')

# Create a label widget
label = Label(frame1, text="Anki Flashcards", font=fontL, fg='blue', bg='white')
label.pack(expand=True, anchor='center')

# Create a button widget
button1 = Button(frame2, text="Let's Start", font=fontM,command=update_label)
button1.pack(expand=True, anchor='center')

button2 = Button(frame2, text="Add To Database", font=fontM,command=show_page2)
button2.pack(expand=True, anchor='center')

button3 = Button(frame2, text="Remove From Database", font=fontM,command=show_page2)
button3.pack(expand=True, anchor='center')


frame2 = Frame(page2)
frame2.pack(expand=True)

# Create a label widget
label2 = Label(frame2, text="page 2")
label2.pack(expand=True)

# Create a button widget
button = Button(frame2, text="Go Back", command=show_page1)
button.pack(expand=True)

#basic setup for navigation
show_page1()

# Run the Tkinter event loop
root.mainloop()

#for navigation, setup a page which can just be a frame, and then pack and unpack the frame as needed
#frame is equivalent to div in html
