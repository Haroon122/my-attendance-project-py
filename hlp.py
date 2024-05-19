from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Tk

class Help_Desk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Developer")

    #==============Background image==============
        img=Image.open(r"E:\python projects\face attendence\project images\back.jpg")
        img=img.resize((1350,700),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        lbl=Label(self.root,image=self.photo)
        lbl.place(x=0,y=0,width=1350,height=700)

    #==================help frame=============
        lbl_L=Frame(lbl,bd=3,bg="white",relief=RIDGE)
        lbl_L.place(x=470,y=130,width=500,height=400)        
    #=============my image==============
        imgtp=Image.open(r"E:\python projects\face attendence\project images\hlp.jpg")
        imgtp=imgtp.resize((300,250),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(imgtp)
        lbl_tpp=Label(lbl_L,image=self.photo1)
        lbl_tpp.place(x=90,y=0,width=300,height=250)

    #=====top label================
        name_lbl=Label(lbl,text="Help Desk",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        name_lbl.place(x=0,y=0,width=1350,height=48)

    #========labels=============

        name_lbl=Label(lbl_L,text="haroonhafeez0302@gmail.com",font=("times new roman",25,"bold"),bg="white",fg="black")
        name_lbl.place(x=30,y=250)

        name_lbl=Label(lbl_L,text="Contact: 0302-1578572",font=("times new roman",25,"bold"),bg="white",fg="black")
        name_lbl.place(x=30,y=300)
        




if __name__=="__main__":
    root=Tk()
    obj=Help_Desk(root)
    root.mainloop()