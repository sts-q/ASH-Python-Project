from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Centered Label and Button")

# Make the window resizable
root.geometry("300x200")  # You can set any initial size you like
root.minsize(200, 150)  # Set a minimum window size for resizing

frame1 = Frame(root)
frame1.pack(expand=True)

# Create a label widget
label = Label(frame1, text="Centered Label")
label.pack(expand=True)

# Create a button widget
button = Button(frame1, text="Click Me")
button.pack(expand=True)

# Run the Tkinter event loop
root.mainloop()