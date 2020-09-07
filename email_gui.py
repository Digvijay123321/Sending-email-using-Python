from tkinter import *
import os
import feat2 
from tkinter import filedialog as fd

filename=[]
def choose():
   filename.append(fd.askopenfilename())

def back():
   e2.delete(0,END)
   e1.delete(0,END)
   textarea.delete(1.0,END)


def submit():
    sub = e2.get()
    to = e1.get()
    body = textarea.get(1.0,END)

    feat2.mail(sub, to, body, filename)
    print("Mail sent.")
    back()

m=Tk()
m.geometry("780x600")

m.iconbitmap(r'path_of_you_ico_file')

m.title("New Message")
l1=Label(m,text="To").place(x=40,y=10)
l2=Label(m,text="Subject").place(x=10,y=40)
e1=Entry(m,bd=5)
e1.grid(row=0,column=1)
e1.place(x=60,y=10,width=180)
e2=Entry(m,bd=5)
e2.grid(row=1,column=1)
e2.place(x=60,y=40,width=180)
textarea=Text()
textarea.place(x=10,y=90)
b1=Button(m,text="Send",width=12,height=2, command = submit).place(x=680,y=190)

b2=Button(m,text="Attach",width=12,height=2, command = choose)
b2.place(x=10,y=500)


m.mainloop()
