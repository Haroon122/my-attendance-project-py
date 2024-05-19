from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage
from PIL import  Image,ImageTk
from time import strftime
from datetime import datetime
import os 
import mysql.connector
import cv2
import numpy as np
import csv



class F_recoginition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Recoginition")

#================back ground image======================
        img1=Image.open(r"E:\python projects\face attendence\project images\face_recog.jpg")
        img1=img1.resize((1350,697),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img1)
        lbl_photo=Label(self.root,image=self.photo)
        lbl_photo.place(x=0,y=0,width=1350,height=697)

#================top main label============================
        top_lbl=Label(lbl_photo,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        top_lbl.place(x=0,y=0,width=1350,height=50)


#==================face recognition button================
        btn=Button(lbl_photo,text="Face Recognition",command=self.detuct,font=("times new roman",20,"bold"),bg="#046264",fg="white",bd=2,relief=RIDGE)
        btn.place(x=548,y=540)


#=========Attendance function===============
    def mart_attend(self,i,r,n,d):
        #with open("attendance.csv","r+",newline="\n") as f:
        with open(r"E:\python projects\face attendence\Attendance Details\attendance.csv", "r+", newline="\n") as f:

            my_data_list=f.readlines()
            name_list=[]
            for line in my_data_list:
                entry1=line.split((","))
                name_list.append(entry1[0])
            if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dt},{d1},present")


    #================detuct function========================
    def detuct(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                roi_gray = gray_img[y:y + h, x:x + w]

                id, confidence = clf.predict(roi_gray)

                conn = mysql.connector.connect(host="localhost", username="root", password="h@Roon#123Abc", database="face_recognization")
                my_cursor = conn.cursor()

                my_cursor.execute("select S_name from face1 where StudentID=" + str(id))
                n = my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"

                my_cursor.execute("select S_Roll from face1 where StudentID=" + str(id))
                r = my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"

                my_cursor.execute("select Department from face1 where StudentID=" + str(id))
                d = my_cursor.fetchone()
                d = str(d[0]) if d else "Unknown"

                my_cursor.execute("select StudentID from face1 where StudentID=" + str(id))
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"

                confidence_percentage = int((1 - confidence / 300) * 100)

                if confidence_percentage > 60:
                    cv2.putText(img, f"Name: {n}", (x, y - 85), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Student ID: {i}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll No: {r}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    self.mart_attend(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap = cv2.VideoCapture(0)

        while True:
            ret, img = videocap.read()
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        videocap.release()
        cv2.destroyAllWindows()




'''
#================face detuction process=====================
    def detuct(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="h@Roon#123Abc", database="face_recognization")
                my_cursor = conn.cursor()


                my_cursor.execute("select S_name from face1 where StudentID="+str(id))
                n=my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"
                #n="+".join(n)

                my_cursor.execute("select S_Roll from face1 where StudentID="+str(id))
                r=my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"
                #r="+".join(r)

                my_cursor.execute("select Department from face1 where StudentID="+str(id))
                d=my_cursor.fetchone()
                d = str(d[0]) if d else "Unknown"
                #d="+".join(d)

                my_cursor.execute("select StudentID from face1 where StudentID="+str(id))
                i=my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"                


                if confidence> 60:
                    cv2.putText(img,f"Name:{n}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)
                    cv2.putText(img,f"Student ID:{i}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)
                    cv2.putText(img,f"Roll No:{r}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)
                    self.mart_attend(i,r,n,d)
                
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "UnKnown Face", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)


                coord=[x,y,w,h]
            return coord
        def recogni(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        videocap=cv2.VideoCapture(0)

        while True:
            ret,img=videocap.read()
            img=recogni(img,clf,faceCascade)
            cv2.imshow("Wellcome To Face Recognition",img)


            if cv2.waitKey(1)==13:

                break
        videocap.release()  # Release the camera
        cv2.destroyAllWindows()

            


'''

if __name__=="__main__":
    root=Tk()
    obj=F_recoginition(root)
    root.mainloop() 