from tkinter import*
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter
from student import student_info
from train_data import Train
from recognization import F_recoginition
from attendance import Attendance
from developer import Developer
from hlp import Help_Desk
from tkinter import Tk

class Face_recognization_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition system")

        #background image
        img=Image.open(r"E:\python projects\face attendence\project images\back.jpg")
        img=img.resize((1350,700),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)

        #help desk image
        img1=Image.open(r"E:\python projects\face attendence\project images\desk.jpg")
        img1=img1.resize((180,180),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)
        b4=Button(bg_img,command=self.desk,image=self.photo1,cursor="hand2")
        b4.place(x=1050,y=100)

        #student attendance image
        img2=Image.open(r"E:\python projects\face attendence\project images\attn1.jpg")
        img2=img2.resize((180,180),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)
        b3=Button(bg_img,command=self.attnd,image=self.photo2,cursor="hand2")
        b3.place(x=450,y=100)

        #face recognization image
        img3=Image.open(r"E:\python projects\face attendence\project images\face1.jpg")
        img3=img3.resize((180,180),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)
        b2=Button(bg_img,command=self.recog,image=self.photo3,cursor="hand2")
        b2.place(x=750,y=100)
        
        #student information image
        img4=Image.open(r"E:\python projects\face attendence\project images\student1.jpg")
        img4=img4.resize((180,180),Image.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photo4,cursor="hand2",command=self.student_details)
        b1.place(x=150,y=100)

        #photos stock image
        img5=Image.open(r"E:\python projects\face attendence\project images\photos.jpg")
        img5=img5.resize((180,180),Image.LANCZOS)
        self.photo5=ImageTk.PhotoImage(img5)
        b5=Button(bg_img,command=self.open_img,image=self.photo5,cursor="hand2")
        b5.place(x=150,y=390)

        # treening image
        img6=Image.open(r"E:\python projects\face attendence\project images\trening.jpg")
        img6=img6.resize((180,180),Image.LANCZOS)
        self.photo6=ImageTk.PhotoImage(img6)
        b6=Button(bg_img,command=self.train_data1,image=self.photo6,cursor="hand2")
        b6.place(x=450,y=390)

        # developer image
        img7=Image.open(r"E:\python projects\face attendence\project images\developerjpg.jpg")
        img7=img7.resize((180,180),Image.LANCZOS)
        self.photo7=ImageTk.PhotoImage(img7)
        b7=Button(bg_img,command=self.dvl,image=self.photo7,cursor="hand2")
        b7.place(x=750,y=390)

        # exit image
        img8=Image.open(r"E:\python projects\face attendence\project images\exit.jpg")
        img8=img8.resize((180,180),Image.LANCZOS)
        self.photo8=ImageTk.PhotoImage(img8)
        b8=Button(bg_img,command=self.exit_win,image=self.photo8,cursor="hand2")
        b8.place(x=1050,y=390)
        
        #main top title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        #student detail title
        lbl_1=Label(bg_img,text="Student Details",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_1.place(x=150,y=290,width=185,height=40)

        #student attendance title
        lbl_2=Label(bg_img,text="Attendance",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_2.place(x=450,y=290,width=185,height=40)

        #Face recognization title
        lbl_3=Label(bg_img,text="Face Recognition",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_3.place(x=750,y=290,width=185,height=40)

        #chat bot title
        lbl_4=Label(bg_img,text="Help Desk",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_4.place(x=1050,y=290,width=185,height=40)

        #photos title
        lbl_5=Label(bg_img,text="Photos",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_5.place(x=150,y=578,width=185,height=40)

        #train data title
        lbl_6=Label(bg_img,text="Train Data",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_6.place(x=450,y=578,width=185,height=40)

        #developer title
        lbl_7=Label(bg_img,text="Developer",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_7.place(x=750,y=578,width=185,height=40)

        #developer title
        lbl_8=Label(bg_img,text="Exit",font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl_8.place(x=1050,y=578,width=185,height=40)

#===========open stock images folder function====================
    def open_img(self):
        os.startfile("data")


        #==============function buttons click on student details and go to other window==============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student_info(self.new_window)

        #==============function buttons click on train data and go to other window==============
    def train_data1(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

        #==============function buttons click on face recognition and go to other window==============
    def recog(self):
        self.new_window=Toplevel(self.root)
        self.app=F_recoginition(self.new_window)

        #==============function buttons click on attendanve and go to other window==============
    def attnd(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

        #==============function buttons click on developer and go to other window==============
    def dvl(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

        #==============function buttons click on  and go to other window==============
    def desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help_Desk(self.new_window)

        #=============exit function===============================

    def exit_win(self):
        self.exit_win=tkinter.messagebox.askyesno("Exit","Are you sure exit this project!",parent=self.root)
        if self.exit_win>0:
            self.root.destroy()
        else:
            return





    
if __name__=="__main__":
    root=Tk()
    obj=Face_recognization_system(root)
    root.mainloop()

