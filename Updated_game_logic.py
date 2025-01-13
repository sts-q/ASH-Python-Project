from tkinter import *
from tkinter import ttk, font as tkFont
from tkextrafont import Font
import random
from PIL import Image, ImageTk  # For handling images
from database import Database

db = Database("temp_dataset.json")  # Use your dataset here

# Initialize Tkinter
root = Tk()
root.title("Anki Flashcards")
root.geometry("500x400")  # Window size is fixed to 500x400
root.minsize(200, 150)

custom_font = Font(family="Times")
fontL = tkFont.Font(family="Times", size=20)
fontM = tkFont.Font(family="Times", size=15)

# Load the background image
background_image_path = r"Final_Card_Font.jpg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((500, 400), Image.Resampling.LANCZOS)  # Resize to fit the window
bg_image_tk = ImageTk.PhotoImage(background_image)

# Frames for pages
page_main = Frame(root)
page_game = Frame(root)

# Current card and answer variables
current_card = None
options = []

# Functions to handle the game logic and navigation
def show_main_menu():
    page_game.pack_forget()
    page_main.pack(expand=True)

def start_game():
    page_main.pack_forget()
    page_game.pack(expand=True)
    load_next_card()

def load_next_card():
    global current_card, options
    
    card_data = db.fetch_random_card()  # Fetch a random card from the database
    if not card_data:
        feedback_label.config(text="No more cards available!", fg="red")
        return

    current_card = card_data
    word_label.config(text=current_card['German'])  # Display the German word

    correct_answer = current_card['English']  # The correct answer is the English meaning
    options = [correct_answer]

    # Populate remaining options with random meanings
    while len(options) < 4:
        random_option = db.fetch_random_meaning()  # Fetch a random meaning
        if random_option not in options:
            options.append(random_option)

    random.shuffle(options)

    # Update option buttons
    for idx, option in enumerate(options):
        option_buttons[idx].config(text=option, command=lambda opt=option: check_answer(opt))

def check_answer(selected_option):
    global current_card

    if selected_option == current_card['English']:  # Check against the correct answer (English meaning)
        feedback_label.config(text="Congratulations, Correct Answer", fg="green")
        db.update_score(current_card['id'], score=1)  # Increment score by 1 for correct answer
    else:
        feedback_label.config(text="Wrong Answer. Try Again!", fg="red")
        db.update_score(current_card['id'], score=-1)  # Decrement score by 1 for wrong answer

    # Delay before loading the next card
    root.after(1000, load_next_card)  # 1 second delay before loading the next card

frame_main_top = Frame(page_main)
frame_main_top.pack(expand=True, fill='both', side='top')

frame_main_bottom = Frame(page_main, pady=20)
frame_main_bottom.pack(expand=True, fill='both', side='bottom')

label_main = Label(frame_main_top, text="Anki Flashcards", font=fontL, fg='blue', bg='white')
label_main.pack(expand=True, anchor='center')

button_start = Button(frame_main_bottom, text="Start Game", font=fontM, command=start_game)
button_start.pack(expand=True, anchor='center')

button_exit = Button(frame_main_bottom, text="Exit", font=fontM, command=root.quit)
button_exit.pack(expand=True, anchor='center')

# Game Page
canvas_game = Canvas(page_game, width=1800, height=1200)
canvas_game.pack(fill="both", expand=True)

# Add the background image to the canvas
canvas_game.create_image(0, 0, anchor=NW, image=bg_image_tk)

# Place widgets over the canvas
word_label = Label(canvas_game, text="", font=fontL, fg='black', bg="#ffffff")
canvas_game.create_window(250, 90, window=word_label)

option_buttons = [Button(canvas_game, text="", font=fontM, bg="#ffffff") for _ in range(4)]
for idx, btn in enumerate(option_buttons):
    canvas_game.create_window(250, 150 + idx* 40, window=btn)

feedback_label = Label(canvas_game, text="", font=fontM, fg='red', bg="#ffffff")
canvas_game.create_window(250, 310, window=feedback_label)

button_back = Button(canvas_game, text="Back to Menu", font=fontM, command=show_main_menu, bg="#ffffff")
canvas_game.create_window(250, 350, window=button_back)

# Initial Setup
show_main_menu()
root.mainloop()
