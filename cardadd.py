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


from database import Database


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

def add_word (dataset_filename):
        """Add a word to dataset."""

        db = Database (dataset_filename)
        de   = input ("german word:  ")
        en   = input ("english word: ")
        desc = input ("description:  ")
        id = check (db, de, en)
        if id == None:
            db.add_word (de, en, desc)
        else: print ("Word is allready in dataset. ID =", id)
        db.save()

def main():
        add_word ("temp_dataset.json")


if __name__ == "__main__":
        main()


# :file: END
