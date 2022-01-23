from tkinter import *
import random

root=Tk()
root.title("Picnic Bag List")
root.geometry("500x500")

label1 = Label(root)
label2 = Label(root)

List1=['Phone','PicnicBasket','Food','Water','Cake','Mum','Dad','Necklace','Mat']
label1['text'] = "Listed_items :  " + str(List1)

def bag_contents():
    
    random_list = random.sample(range(0,8),2)
    label2['text'] = "Put items no " + str(random_list) + "In bag"
   
    
label1.place(relx=0.5,rely=0.4,anchor=CENTER)

btn = Button(root, text="Which item to put in bag?",command = bag_contents,bg="cyan",fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)


label2.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
