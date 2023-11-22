from tkinter import *
from tkinter import filedialog
from tkinter import Tk
from PIL import Image,ImageTk
import os
from stegano import *
from stego_lsb import *


root=Tk()
root.title("steganography")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def Showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG File","*.jpg"),("All file",".txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img    
def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)
    
def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)
    
def Save():
    secret.save("hidden.png")


f=Frame(root,bd=3,bg="black",width=340,height=300,relief=GROOVE)
f.place(x=10,y=70)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="open image",width=10,height=2,font="arial 14 bold",command=Showimage).place(x=20,y=20)
Button(frame3,text="save image",width=10,height=2,font="arial 14 bold",command=Save).place(x=180,y=30)
Label(frame3,text="picture,image,photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="show data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="picture,image,photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)




root.mainloop()