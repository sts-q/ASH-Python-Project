# beolingus-tk.py  --  Try to use beolingus.py from tk.


# TODO
# * make keyword-args for dict.show_query(...)
# * a lot


import tkinter

from beolingus import Beolingus

entry_font   = ("Courier",         16, "normal")
button_font  = ("Arial",           18, "bold")
message_font = ("Times New Roman", 16, "normal")

dict = Beolingus()
word_hist = ["Desire", "Netzpython"]
word_hist_index = 0

def w_next():
    global word_hist_index
    if word_hist_index < len(word_hist) - 1:
        word_hist_index += 1
    else: word_hist_index = 0
    return word_hist_index

def w_prev():
    global word_hist_index
    if word_hist_index > 0:
        word_hist_index -= 1
    else: word_hist_index = len(word_hist) - 1
    return word_hist_index

def w_insert (word):
    word_hist.append (word)

def go():
    word = word_entry.get()
    print (word)
    w_insert (word)
    res = dict.show_query (word, True, True, True, True, False)
    print (res)
    message_box["text"] = res

def go_on_return (event):
    go()

def set_entry_text (e, text):
    e.delete (0,"end")
    e.insert (0,text)

def entry_up (event):
    print ("entry_up")
    print (w_prev())
    set_entry_text (word_entry, word_hist[word_hist_index])

def entry_down (event):
    print ("entry_down")
    print (w_next())
    set_entry_text (word_entry, word_hist[word_hist_index])

def halt():
    print ("------------  quit")
    quit()

win = tkinter.Tk()
win.title ("ASH  beo test&try")
win.minsize (width=600, height=400)

quit_button = tkinter.Button (text="Quit", command=halt, font=button_font)
quit_button.pack()

go_button = tkinter.Button (text="GO", command=go, font=button_font)
go_button.pack()

word_entry = tkinter.Entry (width=30, font=entry_font)
word_entry.bind ("<Return>", go_on_return)
word_entry.bind ("<Up>",     entry_up)
word_entry.bind ("<Down>",   entry_down)
word_entry.pack()

message_box = tkinter.Message(text="<no-text-so-far>", font=("Times New Roman",16,"bold"))
message_box.pack()


def main():
    print ("============  beolingus-tk")
    win.mainloop()
    print ("============  done")

if __name__ == "__main__":
        main()

# file END

