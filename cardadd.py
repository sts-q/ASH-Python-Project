# :file: cardadd.py  --  Add a card to database.


"""Add a card to database.

This module provides functionality to add a card to our database.
A card holds data for a words

 * english meaning
 * german meaning
 * description in a short sentence.
"""


# TODO: Add card with tkinter instead of from terminal.
# TODO: Integrate into main.
# TODO: ??? Check input for what: only ASCII? No!

from tkinter import *
from tkinter import ttk

data_file = "temp_dataset.json"
from database import Database

entry_font   = ("Courier",         18, "normal")
message_font = ("Times New Roman", 16, "normal")

# This function might be moved into class database.Database
def check (db, de, en):
        """Check if word is allready in dataset.

        Return word ID if found.
        Return None if not found.
        """
        id = None
        for w in db.data:
            if w["German"] == de:
                id = w["id"]
                break
            if w["English"] == en:
                id = w["id"]
                break
        return id

def check_word (word):
        res = word.strip()
        if (res == ""):
            res = None
        return res

def add_word (db):
        """Add a word to database."""
        de   = input ("german word:  ")
        en   = input ("english word: ")
        desc = input ("description:  ")
        id = check (db, de, en)
        if id == None:
            db.add_word (de, en, desc)
        else: print ("Word is allready in dataset. ID =", id)
        db.save()

def set_entry_text (e, text):
    e.delete (0,"end")
    e.insert (0,text)

def label_say (label, mess):
        label.config (text=mess)

# entry_de   = tkinter.Entry (width=32, font=entry_font)
# entry_en   = tkinter.Entry (width=32, font=entry_font)
# entry_desc = tkinter.Entry (width=72, font=entry_font)
# set_entry_text (word_entry, word_hist[word_hist_index])
# word_entry.bind ("<Return>", go_on_return)
# word_entry.bind ("<Up>",     entry_up)
# word_entry.bind ("<Down>",   entry_down)
# entry_de.pack(side="top", anchor="w")
# entry_en.pack(side="top", anchor="w")
# entry_desc.pack(side="top", anchor="w")


class Page:
    db           = None
    page_addcard = None
    page_main    = None
    root         = None

    # To frame_main_bottom add a button, that invokes adding a card
    def __init__ (self, frame_main_bottom, page_main, root, bg_image, db):
        self.db        = db
        self.page_main = page_main
        self.root      = root
        button_cardadd = Button (frame_main_bottom, text="Add card", command=self.show_page_cmd)
        button_cardadd.pack()

    def show_page_cmd (self):
        print ("--- show_page_cmd")
        f = Frame (self.root)
        mess_headline   = Label (f, text="Add a card.", font=message_font)
        mess_de         = Label (f, text="German",      font=message_font)
        mess_en         = Label (f, text="English",     font=message_font)
        mess_desc       = Label (f, text="Description", font=message_font)
        self.mess_err   = Label (f, text="<>",          font=message_font)
        self.entry_de   = Entry (f, width=32, font=entry_font)
        self.entry_en   = Entry (f, width=32, font=entry_font)
        self.entry_desc = Entry (f, width=72, font=entry_font)
        button_add      = Button (f, text="Add",  command=self.add_word_cmd)
        button_back     = Button (f, text="Back", command=self.back_cmd)
        self.entry_de.bind   ("<Return>", self.add_word_event)
        self.entry_en.bind   ("<Return>", self.add_word_event)
        self.entry_desc.bind ("<Return>", self.add_word_event)
        mess_headline.pack()
        mess_de.pack(anchor="w")
        self.entry_de.pack(side="top", anchor="w")
        mess_en.pack(anchor="w")
        self.entry_en.pack(side="top", anchor="w")
        mess_desc.pack(anchor="w")
        self.entry_desc.pack(side="top", anchor="w")
        button_add.pack()
        button_back.pack()
        self.mess_err.pack()
        self.page_main.pack_forget()
        f.pack(expand=True)
        self.page_addcard = f

    def add_word_cmd(self):
        de   = self.entry_de.get ()
        en   = self.entry_en.get ()
        desc = self.entry_desc.get ()
        print ("--- add card: <",de,">  <",en,">   <",desc,">")
        de = check_word (de)
        en = check_word (en)
        id = check (self.db, de, en)
        if de == None:
            label_say (self.mess_err, "Strange input for DE.")
            self.entry_de.focus()
        if en == None:
            label_say (self.mess_err, "Strange input for EN.")
            self.entry_en.focus()
        if id != None: label_say (self.mess_err, "Word is allready in dataset. ID = "+ str(id))
        if (id == None) and (de != None) and (en != None):
            self.db.add_word (de, en, desc)
            self.db.save()
            label_say (self.mess_err, "Added   German: " + de+ "   English: "+ en+"   Description: " + desc)
            set_entry_text (self.entry_de, "")
            set_entry_text (self.entry_en, "")
            set_entry_text (self.entry_desc, "")
            self.entry_de.focus()
            print ("--- add_word_cmd: done")
        else: print ("--- add_word_cmd: strange input or word already in dataset")

    def add_word_event (self, event):
        self.add_word_cmd ()

    def back_cmd(self):
        print ("--- cmd: back")
        self.page_addcard.pack_forget()
        self.page_main.pack(expand=True)

#     def next_tab (self, w):
#         res = None
#         if   w == self.entry_de:   res = self.entry_en
#         elif w == self.entry_en:   res = self.entry_desc
#         elif w == self.entry_desc: res = self.entry_de
#         else: res = self.entry_de
#         print ("--- next_tab")
#         return res

#     def tab_cmd(self, event):
#         (self.next_tab (self.root.focus())).focus()


def main():
        db = Database (data_file)
        add_word (db)


if __name__ == "__main__":
        main()


# :file: END
