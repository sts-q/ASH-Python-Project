# beolingus-tk.py  --  Try to use beolingus.py from tk.


# TODO
# * make keyword-args for dict.show_query(...)
# * a lot


import tkinter

from beolingus import Beolingus


win = tkinter.Tk()
win.title ("ASH  beo test&try")
win.minsize (width=400, height=400)

desc_label = tkinter.Label (text="word: ", font=("Arial", 24, "bold"))
desc_label.pack(side="top")



def main():
    print ("============  beolingus-tk")
    dict = Beolingus()
#     dict.info ("Desire", ignorecase=False)
#     mess = "hallo"
    text = dict.show_query ("Netzpython", True, True, True, True, True)
    print (text)
    text_label = tkinter.Label (text=text, font=("Arial",12,"bold"))
    text_label.pack(side="top")
    win.mainloop()
    print ("============  done")

if __name__ == "__main__":
        main()

# file END

