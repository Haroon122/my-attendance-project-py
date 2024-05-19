from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np





class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Train Data")


        bk_img=Image.open(r"E:\python projects\face attendence\project images\bk.jpg")
        bk_img=bk_img.resize((1350,700),Image.LANCZOS)
        self.photo_bk=ImageTk.PhotoImage(bk_img)
        lbl_bk=Label(self.root,image=self.photo_bk)
        lbl_bk.place(x=0,y=0,width=1350,height=700)

        #===================main title===========================
        main_title=Label(lbl_bk,text="Train Data Set",font=("times new roman",30,"bold"),bg="white",fg="red")
        main_title.place(x=0,y=0,width=1350,height=45)


        #===================top image=========================
        tp_img=Image.open(r"E:\python projects\face attendence\project images\top_img.jpg")
        tp_img=tp_img.resize((1350,300),Image.LANCZOS)
        self.tp_photo=ImageTk.PhotoImage(tp_img)
        lbl_tp=Label(lbl_bk,image=self.tp_photo)
        lbl_tp.place(x=0,y=0,width=1350,height=300)


        #=====================train data button================
        train_btn=Button(lbl_bk,text="Train Data",command=self.train_clssi,bd=2,relief=RIDGE,font=("times new roman",40,"bold"),bg="#091930",fg="white")
        train_btn.place(x=0,y=307,width=1350,height=90) 

        #=============botom image============================
        bt_img=Image.open(r"E:\python projects\face attendence\project images\botom.jpg")
        bt_img=bt_img.resize((1350,300),Image.LANCZOS)
        self.bt_photo=ImageTk.PhotoImage(bt_img)
        lbl_bt=Label(lbl_bk,image=self.bt_photo)
        lbl_bt.place(x=0,y=400,width=1350,height=300)




        #=====================train classifier (train data) function=================
    def train_clssi(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')   #convert to gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)

            cv2.waitKey(1)  # Changed line to properly capture key press
            if cv2.waitKey(1) == 13:
                break
            #cv2.waitKey(1)==13
        ids=np.array(ids)

            #==============Train classifier and save the data================

        clf=cv2.face.LBPHFaceRecognizer_create()


        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set completed!!!",parent=self.root)









if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()