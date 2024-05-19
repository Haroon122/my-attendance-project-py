from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import PhotoImage
import os
import mysql.connector
import cv2
import numpy as np
import csv
from tkinter import filedialog
from tkinter import messagebox

my_Data=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Attendance")

    #==========veriables===============
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_atnd=StringVar()
        self.var_date=StringVar()




    #==============Background image==============
        img=Image.open(r"E:\python projects\face attendence\project images\bk.jpg")
        img=img.resize((1350,700),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        lbl=Label(self.root,image=self.photo)
        lbl.place(x=0,y=0,width=1350,height=700)

        #=============Top image 1==============
        imgtp=Image.open(r"E:\python projects\face attendence\project images\atnd7.png")
        imgtp=imgtp.resize((450,180),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(imgtp)
        lbl_tpp=Label(lbl,image=self.photo1)
        lbl_tpp.place(x=0,y=0,width=450,height=180)

        #=============Top image 2==============
        imgtp1=Image.open(r"E:\python projects\face attendence\project images\atndd5.jpg")
        imgtp1=imgtp1.resize((450,180),Image.LANCZOS)
        self.photo11=ImageTk.PhotoImage(imgtp1)
        lbl_tpp=Label(lbl,image=self.photo11)
        lbl_tpp.place(x=450,y=0,width=450,height=180)


        #=============Top image 3==============
        imgtp2=Image.open(r"E:\python projects\face attendence\project images\atnd6.jpg")
        imgtp2=imgtp2.resize((450,180),Image.LANCZOS)
        self.photo12=ImageTk.PhotoImage(imgtp2)
        lbl_tpp=Label(lbl,image=self.photo12)
        lbl_tpp.place(x=900,y=0,width=450,height=180)

        #=======main frame=====================
        main_frm=Frame(lbl,bd=3,relief=RIDGE,bg="white")
        main_frm.place(x=1,y=182,width=1345,height=512)

        #=======main top title===============
        tp_lbl=Label(main_frm,text="Attendance Managment System",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        tp_lbl.place(x=0,y=0,width=1340,height=40)

        #=========left side student details attendance details label frame============
        lbl_L=LabelFrame(main_frm,bd=3,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"),fg="red")
        lbl_L.place(x=15,y=40,width=640,height=460)

        #=========left frame top image 1=========
        imgt=Image.open(r"E:\python projects\face attendence\project images\atndL.jpg")
        imgt=imgt.resize((310,120),Image.LANCZOS)
        self.photoL=ImageTk.PhotoImage(imgt)
        lbl_tp=Label(lbl_L,image=self.photoL)
        lbl_tp.place(x=0,y=0,width=310,height=120)       

        #=========left frame top image 2=========
        imgL=Image.open(r"E:\python projects\face attendence\project images\atnd4.jpg")
        imgL=imgL.resize((310,120),Image.LANCZOS)
        self.photoA=ImageTk.PhotoImage(imgL)
        lbl_tp1=Label(lbl_L,image=self.photoA)
        lbl_tp1.place(x=320,y=0,width=310,height=120) 


        #==========labels and etrybox frame===============

        min_frm=Frame(lbl_L,bd=3,relief=RIDGE,bg="white")
        min_frm.place(x=2,y=120,width=630,height=315)

        #==========student id label=============
        S_lbl=Label(min_frm,text="Student ID:",font=("times new roman",15,"bold"),bg="white",fg="black")
        S_lbl.place(x=20,y=20)

        #==========student name label=============
        N_lbl=Label(min_frm,text="Name:",font=("times new roman",15,"bold"),bg="white",fg="black")
        N_lbl.place(x=20,y=60)

        #==========student time label=============
        T_lbl=Label(min_frm,text=" Time:",font=("times new roman",15,"bold"),bg="white",fg="black")
        T_lbl.place(x=15,y=100)

        #==========student roll no label=============
        R_lbl=Label(min_frm,text=" Roll No:",font=("times new roman",15,"bold"),bg="white",fg="black")
        R_lbl.place(x=300,y=20)

        #==========student department label=============
        D_lbl=Label(min_frm,text=" Department:",font=("times new roman",15,"bold"),bg="white",fg="black")
        D_lbl.place(x=300,y=60)

        #==========student date label=============
        DT_lbl=Label(min_frm,text=" Date:",font=("times new roman",15,"bold"),bg="white",fg="black")
        DT_lbl.place(x=300,y=100)

        #==========student attendance status label=============
        AT_lbl=Label(min_frm,text=" Attendance Status:",font=("times new roman",15,"bold"),bg="white",fg="black")
        AT_lbl.place(x=20,y=140)

        #=============StudentId EntryBox=============
        id_entr=Entry(min_frm,bd=2,textvariable=self.var_id,relief=RIDGE,bg="white",font=("times new roman",13))
        id_entr.place(x=130,y=20,width=150)

        #=============Student name EntryBox=============
        s_entr=Entry(min_frm,bd=2,textvariable=self.var_name,relief=RIDGE,bg="white",font=("times new roman",13))
        s_entr.place(x=130,y=60,width=150)

        #=============time EntryBox=============
        t_entr=Entry(min_frm,bd=2,textvariable=self.var_time,relief=RIDGE,bg="white",font=("times new roman",13))
        t_entr.place(x=130,y=100,width=150)

        #=============Student roll no EntryBox=============
        R_entr=Entry(min_frm,bd=2,textvariable=self.var_roll,relief=RIDGE,bg="white",font=("times new roman",13))
        R_entr.place(x=440,y=20,width=150)

        #=============Student dep EntryBox=============
        id_entr=Entry(min_frm,bd=2,textvariable=self.var_dep,relief=RIDGE,bg="white",font=("times new roman",13))
        id_entr.place(x=440,y=60,width=150)

        #=============date EntryBox=============
        id_entr=Entry(min_frm,bd=2,textvariable=self.var_date,relief=RIDGE,bg="white",font=("times new roman",13))
        id_entr.place(x=440,y=100,width=150)

        #=============attendance status combox==============
        At_comb=ttk.Combobox(min_frm,textvariable=self.var_atnd,font=("times new roman",13),width=20,state="readonly")
        At_comb["value"]=("Status","Present","Absent","Leave")
        At_comb.current(0)
        At_comb.place(x=200,y=140)

        #============import CSV Button==============
        I_btn=Button(min_frm,bd=3,relief=RIDGE,command=self.import_csv,text="Import CSV",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        I_btn.place(x=20,y=200,width=130)



        #============export CSV Button==============
        I_btn=Button(min_frm,bd=3,relief=RIDGE,command=self.export_csv,text="Export CSV",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        I_btn.place(x=170,y=200,width=130)


        #============update Button==============
        I_btn=Button(min_frm,command=self.update_data,bd=3,relief=RIDGE,text=" Update",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        I_btn.place(x=325,y=200,width=130)


        #============reset Button==============
        I_btn=Button(min_frm,bd=3,command=self.reset,relief=RIDGE,text=" Reset",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        I_btn.place(x=480,y=200,width=130)


              
        #=========right side  attendance details label frame============
        lbl_R=LabelFrame(main_frm,bd=3,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),fg="red")
        lbl_R.place(x=680,y=40,width=640,height=460)
        #==============scrol bar==================
        
        scroll_x=ttk.Scrollbar(lbl_R,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(lbl_R,orient=VERTICAL)

        #========Right side frame treeview==============
        self.A_Table=ttk.Treeview(lbl_R,column=("id","roll","name","dep","time","date","attnd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.A_Table.xview)
        scroll_y.config(command=self.A_Table.yview)

        self.A_Table.heading("id",text="StudentId")
        self.A_Table.heading("roll",text="Roll No")
        self.A_Table.heading("name",text="Name")
        self.A_Table.heading("dep",text="Department")
        self.A_Table.heading("time",text="Time")
        self.A_Table.heading("date",text="Date")
        self.A_Table.heading("attnd",text="Attendance")

        self.A_Table["show"]="headings"

        self.A_Table.column("id",width=100)
        self.A_Table.column("roll",width=100)
        self.A_Table.column("name",width=100)
        self.A_Table.column("dep",width=100)
        self.A_Table.column("time",width=100)
        self.A_Table.column("date",width=100)
        self.A_Table.column("attnd",width=100)

        self.A_Table.pack(fill=BOTH,expand=1)

        self.A_Table.bind("<ButtonRelease>",self.get_cursor)

        #==============fetch data==========

    def fetch_data(self,rows):
        self.A_Table.delete(*self.A_Table.get_children())
        for i in rows:
            self.A_Table.insert("",END,values=i)
    #==============import csv===========
    def import_csv(self):
        global my_Data
        my_Data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                my_Data.append(i)
            self.fetch_data(my_Data)
            self.reset()
    #=============export csv============
    def export_csv(self):
        try:
            if len(my_Data)<1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if not fln:
                return
            with open(fln,mode="w",newline="") as myfile:
                exportcsv=csv.writer(myfile,delimiter=",")
                for i in my_Data:
                    exportcsv.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"  + os.path.basename(fln)+ "Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)

    

    def get_cursor(self,event=""):
        cur=self.A_Table.focus()
        content=self.A_Table.item(cur)
        rows=content["values"]
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_atnd.set(rows[6])


    #===================update csv=========================
    def update_data(self):
        cur = self.A_Table.focus()
        content = self.A_Table.item(cur)
        selected_row = content["values"]

        if not selected_row:
            messagebox.showerror("Error", "No row selected for update", parent=self.root)
            return

        # Update individual fields in the selected row
        selected_row = list(selected_row)
        selected_row[0] = self.var_id.get() if self.var_id.get() else selected_row[0]
        selected_row[1] = self.var_roll.get() if self.var_roll.get() else selected_row[1]
        selected_row[2] = self.var_name.get() if self.var_name.get() else selected_row[2]
        selected_row[3] = self.var_dep.get() if self.var_dep.get() else selected_row[3]
        selected_row[4] = self.var_time.get() if self.var_time.get() else selected_row[4]
        selected_row[5] = self.var_date.get() if self.var_date.get() else selected_row[5]
        selected_row[6] = self.var_atnd.get() if self.var_atnd.get() else selected_row[6]

        # Update the Treeview
        self.A_Table.item(cur, values=tuple(selected_row))

        # Update the data in my_Data list
        selected_index = my_Data.index(list(content["values"]))
        my_Data[selected_index] = selected_row


        # Export the updated data to the CSV file
        self.export_csv()

        # Reset the form
        self.reset() 

    #========reset function===========
    def reset(self):

        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atnd.set("") 

    



       

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
