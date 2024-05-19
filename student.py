from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class student_info:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Student Information")

        #=================declair veriables===============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_Id=StringVar()
        self.var_std_name=StringVar()
        self.var_f_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_radio=StringVar()
        self.var_srch=StringVar()
        self.var_srch_entry=StringVar()


        #background image
        img=Image.open(r"E:\python projects\face attendence\project images\back.jpg")
        img=img.resize((1350,700),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)

        #main top title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        # main_frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=8,y=50,width=1335,height=640)

        #student data label frame left side
        left_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="red")
        left_frame.place(x=15,y=10,width=640,height=615)

        #students top image left side
        lbl_img=Image.open(r"E:\python projects\face attendence\project images\std.jpg")
        lbl_img=lbl_img.resize((625,120),Image.LANCZOS)
        self.photo_left=ImageTk.PhotoImage(lbl_img)
        L_lbl=Label(left_frame,image=self.photo_left)
        L_lbl.place(x=5,y=0,width=625,height=120)

        #current course information left side frame
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),fg="red")
        current_frame.place(x=1,y=120,width=630,height=140)

        # department label set in left side frame
        dep_lbl=Label(current_frame,text="Department:",font=("times new roman",12,"bold"),bg="white",fg="black")
        dep_lbl.place(x=20,y=15)

        #department combobox
        dep_comb=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_comb["values"]=("Select Department","Computer","English","Math","Urdu","Chemistry")
        dep_comb.current(0)
        dep_comb.place(x=125,y=15)

        # course label set in left side frame
        crs_lbl=Label(current_frame,text="Course:",font=("times new roman",12,"bold"),bg="white",fg="black")
        crs_lbl.place(x=340,y=15)

        #course combobox
        crs_comb=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        crs_comb["value"]=("Select Course","Bs","MA","MCS")
        crs_comb.current(0)
        crs_comb.place(x=425,y=15)

        # year label set in left side frame
        year_lbl=Label(current_frame,text="Year:",font=("times new roman",12,"bold"),bg="white",fg="black")
        year_lbl.place(x=20,y=70)

        #year combobox
        year_comb=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_comb["value"]=("Select Year","2020-24","2024-28","2028-32")
        year_comb.current(0)
        year_comb.place(x=125,y=70)

        # semester label set in left side frame
        smstr_lbl=Label(current_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white",fg="black")
        smstr_lbl.place(x=340,y=70)

        #semester combobox
        smstr_comb=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        smstr_comb["value"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        smstr_comb.current(0)
        smstr_comb.place(x=425,y=70)

        #student class information label frame left side
        cls_info=LabelFrame(left_frame,text="Student Class Information",font=("times new roman",12,"bold"),bg="white",fg="red",bd=2,relief=RIDGE)
        cls_info.place(x=1,y=260,width=630,height=328)

        #studentID label
        sID_lbl=Label(cls_info,text="StudentID No:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sID_lbl.place(x=20,y=10)

        #studentID Entry box
        s_Entry=Entry(cls_info,textvariable=self.var_std_Id,width=27,bd=2,relief=RIDGE)
        s_Entry.place(x=135,y=10)

        #student name label
        sName_lbl=Label(cls_info,text="Student Name:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sName_lbl.place(x=20,y=40)

        #student Name Entry box
        name_Entry=Entry(cls_info,textvariable=self.var_std_name,width=27,bd=2,relief=RIDGE)
        name_Entry.place(x=135,y=40)

        #student Father name label
        Fname_lbl=Label(cls_info,text="Father Name:",font=("times new roman",12,"bold"),fg="black",bg="white")
        Fname_lbl.place(x=20,y=70)

        #student father Name Entry box
        Fname_Entry=Entry(cls_info,textvariable=self.var_f_name,width=27,bd=2,relief=RIDGE)
        Fname_Entry.place(x=135,y=70)

        #student Roll NO label
        sRoll_lbl=Label(cls_info,text="Student Roll No:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sRoll_lbl.place(x=20,y=100)

        #student roll no Entry box
        Rno_Entry=Entry(cls_info,textvariable=self.var_roll,width=27,bd=2,relief=RIDGE)
        Rno_Entry.place(x=135,y=100)

        #student Gender label
        sGndr_lbl=Label(cls_info,text="Gender:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sGndr_lbl.place(x=340,y=10)

        #student gender combobox
        gender_comb=ttk.Combobox(cls_info,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_comb["value"]=("Select Gender","Male","Female")
        gender_comb.current(0)
        gender_comb.place(x=420,y=10)

        #student E-Mail label
        sMail_lbl=Label(cls_info,text="E-Mail:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sMail_lbl.place(x=340,y=40)

        #student E-Mail Entry box
        mail_Entry=Entry(cls_info,textvariable=self.var_email,width=27,bd=2,relief=RIDGE)
        mail_Entry.place(x=420,y=40)

        #student phone no label
        sPH_lbl=Label(cls_info,text="Phone No:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sPH_lbl.place(x=340,y=70)

        #student phone no Entry box
        ph_Entry=Entry(cls_info,textvariable=self.var_phone,width=27,bd=2,relief=RIDGE)
        ph_Entry.place(x=420,y=70)


        #student Address label
        sAddress_lbl=Label(cls_info,text="Address:",font=("times new roman",12,"bold"),fg="black",bg="white")
        sAddress_lbl.place(x=340,y=100)

        #student address Entry box
        adrs_Entry=Entry(cls_info,textvariable=self.var_address,width=27,bd=2,relief=RIDGE)
        adrs_Entry.place(x=420,y=100)


        #student photo radio button
        radiobutton1=ttk.Radiobutton(cls_info,variable=self.var_radio,text="Take Photo Image",value="yes")
        radiobutton1.place(x=20,y=140)

        #student No photo radio button
        radiobutton2=ttk.Radiobutton(cls_info,variable=self.var_radio,text="No Take Photo Image",value="no")
        radiobutton2.place(x=150,y=140)

        #buttons frame
        btn_frm=Frame(cls_info,width=620,height=130,bd=2,relief=RIDGE,bg="white")
        btn_frm.place(x=3,y=170)

        #save button     
        save_btn=Button(btn_frm,command=self.add_data,text="Save",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,width=16,bg="darkblue",fg="white")
        save_btn.place(x=0,y=0)

        #update button
        update_btn=Button(btn_frm,command=self.update_data,text="Update",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,width=16,bg="darkblue",fg="white")
        update_btn.place(x=155,y=0)

        #delete button
        dlt_btn=Button(btn_frm,command=self.delete_data,text="Delete",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,width=16,bg="darkblue",fg="white")
        dlt_btn.place(x=307,y=0)

        #reset button
        reset_btn=Button(btn_frm,command=self.reset_data,text="Reset",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,width=16,bg="darkblue",fg="white")
        reset_btn.place(x=461,y=0)

        #add photo sample button
        addPhoto_btn=Button(btn_frm,command=self.generate_dataset,text="Add Photo Sample",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,width=33,bg="darkblue",fg="white")
        addPhoto_btn.place(x=0,y=35)

        #update photo sample button
        reset_btn=Button(btn_frm,text="Update Photo Sample",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,width=33,bg="darkblue",fg="white")
        reset_btn.place(x=309,y=35)
        
        #button frame end image 1
        end_img=Image.open(r"E:\python projects\face attendence\project images\end3.jpg")
        end_img=end_img.resize((625,60),Image.LANCZOS)
        self.photo_end=ImageTk.PhotoImage(end_img)
        E_lbl=Label(btn_frm,image=self.photo_end)
        E_lbl.place(x=0,y=70,width=625,height=60)
        



        #======================================================================================

        #student data label frame right side

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="red")
        right_frame.place(x=670,y=10,width=640,height=615)

        #right side frame top image
        right_image=Image.open(r"E:\python projects\face attendence\project images\end.jpg")
        right_image=right_image.resize((630,180),Image.LANCZOS)
        self.photo_Right=ImageTk.PhotoImage(right_image)
        R_lbl=Label(right_frame,image=self.photo_Right)
        R_lbl.place(x=3,y=0,width=630,height=180)

        #view student detail and search label frame
        view_lbl=LabelFrame(right_frame,bd=2,relief=RIDGE,text="View Student Details & Search",font=("times new roman",12,"bold"),fg="red",bg="white")
        view_lbl.place(x=3,y=180,width=630,height=70)

        #label of (search by)
        srch_lbl=Label(view_lbl,text="Search By",font=("times new roman",15,"bold"),bg="darkred",fg="white")
        srch_lbl.place(x=5,y=5)

        #combobox of (search by)
        comb_srch=ttk.Combobox(view_lbl,textvariable=self.var_srch,width=16,state="readonly",font=("times new roman",12,"bold"))
        comb_srch["value"]=("Select Option","Roll NO","Phone NO","StudentID")
        comb_srch.current(0)
        comb_srch.place(x=100,y=7)

        #entry box of (search by)
        srch_entry=Entry(view_lbl,textvariable=self.var_srch_entry,width=18,font=("times new roman",12),bd=2,relief=RIDGE,bg="white")
        srch_entry.place(x=260,y=7)

        #search button in right side frame
        srch_btn=Button(view_lbl,command=self.search_data,width=8,text="Search",font=("times new roman",13,"bold"),bg="darkblue",fg="white",bd=2,relief=RIDGE)
        srch_btn.place(x=430,y=4)

        #show all button in right side frame
        show_btn=Button(view_lbl,command=self.fetch_data,width=8,text="Show All",font=("times new roman",13,"bold"),bg="darkblue",fg="white",bd=2,relief=RIDGE)
        show_btn.place(x=530,y=4)

        #===============table frame================
        tbl_frm=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        tbl_frm.place(x=3,y=255,width=630,height=333)
        #==============scrol bar==================
        
        scroll_x=ttk.Scrollbar(tbl_frm,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frm,orient=VERTICAL)

        #============tree view====================
        self.student_table=ttk.Treeview(tbl_frm,column=("dep","course","year","sem","name","f_name","id","roll","gender","phone","address","mail","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("f_name",text="F_Name")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("mail",text="Email")
        self.student_table.heading("photo",text="Photo_Status")
        

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("f_name",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("mail",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_data)
        self.fetch_data()

#===================storing data function====================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_address.get()=="" or self.var_course.get()=="Select Course" or self.var_email.get()=="" or self.var_f_name.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_roll.get()=="" or self.var_semester.get()=="Select Semester" or self.var_std_Id.get()=="" or self.var_std_name.get()=="" or self.var_year.get()=="Select Year" or self.var_radio.get() not in ["yes", "no"]:
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="?????????", username="????", password="?????????????", database="??????????????????")
                my_cursor = conn.cursor()

                query = ("INSERT INTO face1 SET "
                        "Department = %s, "
                        "course = %s, "
                        "year = %s, "
                        "semester = %s, "
                        "S_name = %s, "
                        "F_name = %s, "
                        "StudentID = %s, "
                        "S_Roll = %s, "
                        "gender = %s, "
                        "phone = %s, "
                        "address = %s, "
                        "email = %s, "
                        "photo = %s ")

                data = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_f_name.get(),
                    self.var_std_Id.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_radio.get()
                    
                )

                my_cursor.execute(query, data)
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)


#=====================fetch data from data base and show on table===========
    def fetch_data(self):
        conn = mysql.connector.connect(host="?????????", username="????", password="?????????????", database="??????????????????")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from face1")
        data1=my_cursor.fetchall()

        if len(data1)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data1:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()





#========================search query====================
    def search_data(self):
        if self.var_srch.get() == "Select Option" or self.var_srch_entry.get() == "":
            messagebox.showerror("Error", "Please select a search option and enter a value.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="?????????", username="????", password="?????????????", database="??????????????????")
                my_cursor = conn.cursor()

                # Determine the column based on the selected search option
                search_option = self.var_srch.get().lower()
                if search_option == "roll no":
                    column = "S_Roll"
                elif search_option == "phone no":
                    column = "phone"
                elif search_option == "studentid":
                    column = "StudentID"
                else:
                    messagebox.showerror("Error", "Invalid search option", parent=self.root)
                    return

                # Perform the search
                query = f"SELECT * FROM face1 WHERE {column} LIKE %s"
                value = (f"%{self.var_srch_entry.get()}%",)
                my_cursor.execute(query, value)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Result", "No matching records found.", parent=self.root)

                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)


#==============================Get Function for Update Button=================
    def get_data(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data2=content["values"]

        self.var_dep.set(data2[0])
        self.var_course.set(data2[1])
        self.var_year.set(data2[2])
        self.var_semester.set(data2[3])
        self.var_std_name.set(data2[4])
        self.var_f_name.set(data2[5])
        self.var_std_Id.set(data2[6])
        self.var_roll.set(data2[7])
        self.var_gender.set(data2[8])
        self.var_phone.set(data2[9])
        self.var_address.set(data2[10])
        self.var_email.set(data2[11])
        self.var_radio.set(data2[12].lower())

#================update function===================
    
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_address.get() == ""
            or self.var_course.get() == "Select Course"
            or self.var_email.get() == ""
            or self.var_f_name.get() == ""
            or self.var_gender.get() == "Select Gender"
            or self.var_phone.get() == ""
            or self.var_roll.get() == ""
            or self.var_semester.get() == "Select Semester"
            or self.var_std_Id.get() == ""
            or self.var_std_name.get() == ""
            or self.var_year.get() == "Select Year"
            or self.var_radio.get() not in ["yes", "no"]
    ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
            # Ask for confirmation
                update1 = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update1:
                    conn = mysql.connector.connect(host="?????????",username="????",password="?????????????",database="??????????????????")                
                    my_cursor = conn.cursor()

                # Use UPDATE query instead of INSERT
                    query = (
                        "UPDATE face1 SET "
                        "Department = %s, "
                        "course = %s, "
                        "year = %s, "
                        "semester = %s, "
                        "S_name = %s, "
                        "F_name = %s, "
                        "S_Roll = %s, "
                        "gender = %s, "
                        "phone = %s, "
                        "address = %s, "
                        "email = %s, "
                        "photo = %s "
                        "WHERE StudentID = %s"
                )

                    data = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_f_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_radio.get(),
                        self.var_std_Id.get()
                        
                )

                    my_cursor.execute(query, data)
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                        
                    
                else:
                # If the user clicks 'No', do nothing
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #========================Delete Function=========================
    def delete_data(self):
        if self.var_std_Id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete1=messagebox.askyesno("Student Delete page","Do you want to delete",parent=self.root)
                if delete1 >0:
                    conn = mysql.connector.connect(host="?????????",username="????",password="?????????????",database="??????????????????")                
                    my_cursor = conn.cursor()
                    sql="delete from face1 WHERE StudentID = %s"
                    val=(self.var_std_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete1:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)  

    #======================reset function=========================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_address.set("")
        self.var_course.set("Select Course")
        self.var_email.set("")
        self.var_f_name.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set("")
        self.var_roll.set("")
        self.var_semester.set("Select Semester")
        self.var_std_Id.set("")
        self.var_std_name.set("")
        self.var_year.set("Select Year")
        self.var_radio.set("")  



#==========================generate data set or take a photo sample====================
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_address.get() == ""
            or self.var_course.get() == "Select Course"
            or self.var_email.get() == ""
            or self.var_f_name.get() == ""
            or self.var_gender.get() == "Select Gender"
            or self.var_phone.get() == ""
            or self.var_roll.get() == ""
            or self.var_semester.get() == "Select Semester"
            or self.var_std_Id.get() == ""
            or self.var_std_name.get() == ""
            or self.var_year.get() == "Select Year"
            or self.var_radio.get() not in ["yes", "no"]
    ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="?????????",username="????",password="?????????????",database="??????????????????")                
                my_cursor = conn.cursor()
                my_cursor.execute("select * from face1")
                result=my_cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                query = (
                    "UPDATE face1 SET "
                    "Department = %s, "
                    "course = %s, "
                    "year = %s, "
                    "semester = %s, "
                    "S_name = %s, "
                    "F_name = %s, "
                    "S_Roll = %s, "
                    "gender = %s, "
                    "phone = %s, "
                    "address = %s, "
                    "email = %s, "
                    "photo = %s "
                    "WHERE StudentID = %s"
                )

                data = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_f_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_radio.get(),
                    self.var_std_Id.get(),
                    id+1
                )                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===========load predefiend data on face frontal from OPENCV=============

                face_classification = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                #============
                def face_croper(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classification.detectMultiScale(gray, 1.3, 5)

                    #scaling factor=1.3
                    #minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_croper=img[y:y+h,x:x+w]
                        return face_croper
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croper(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croper(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
                        cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Error:{str(es)}",parent=self.root)














if __name__=="__main__":
    root=Tk()
    obj=student_info(root)
    root.mainloop()
