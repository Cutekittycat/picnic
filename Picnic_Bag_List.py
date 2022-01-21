from tkinter import *
import random

root=Tk()
root.title("Picnic Bag List")
root.geometry("400x400")

picnic_list_display = Label(root)
picnic_random_number = Label(root)

def picnic():
    List1=['Phone','PicnicBasket','Food','Water','Cake','Mum','Dad',]
    picnic["text"] = "listed_items : " + str(picnic)



root.mainloop()
