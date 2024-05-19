from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Tk
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Developer")

    #==============Background image==============
        img=Image.open(r"E:\python projects\face attendence\project images\developer.jpg")
        img=img.resize((1350,700),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        lbl=Label(self.root,image=self.photo)
        lbl.place(x=0,y=0,width=1350,height=700)

    #==================pic frame=============
        lbl_L=Frame(lbl,bd=3,bg="white",relief=RIDGE)
        lbl_L.place(x=470,y=130,width=500,height=400)        
    #=============my image==============
        imgtp=Image.open(r"E:\python projects\face attendence\project images\my.jpg")
        imgtp=imgtp.resize((300,200),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(imgtp)
        lbl_tpp=Label(lbl_L,image=self.photo1)
        lbl_tpp.place(x=90,y=0,width=300,height=200)

    #=====top label================
        name_lbl=Label(lbl,text="Developer",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        name_lbl.place(x=0,y=0,width=1350,height=48)

    #========labels=============

        name_lbl=Label(lbl_L,text="Hello!!!",font=("times new roman",25,"bold"),bg="white",fg="black")
        name_lbl.place(x=180,y=180)

        name_lbl=Label(lbl_L,text="My Name Is Haroon",font=("times new roman",25,"bold"),bg="white",fg="black")
        name_lbl.place(x=90,y=230)

        name_lbl=Label(lbl_L,text="I AM FULL STACK DEVELOPER",font=("times new roman",20,"bold"),bg="white",fg="black")
        name_lbl.place(x=40,y=280)
  
      

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()