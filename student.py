from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import mysql.connector
import cv2
from timetable import Time_Table
from tkinter import messagebox
#from help import Help_Desk
#from developer import develop



class student:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Student")
        S_w=root.winfo_screenwidth()
        S_h=root.winfo_screenheight()
        if S_w > 1280:
            w = S_w / 1280
        else:
            w = 1 / (1280 / S_w) 
        if S_h > 720:
            h = S_h / 720
        else:
            h = 1 / (720 / S_h)

        self.var_Department=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_Student_Id=StringVar()
        self.var_Student_Name=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Gender=StringVar()
        self.var_dob=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Email=StringVar()
        self.var_radio1=StringVar()
        self.var_Photo=StringVar()
        self.var_usertype=StringVar()
        

    # first image
        img1=Image.open(r"Image Content\XYZins.jpg")
        img1=img1.resize((int(130*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        
        f_lbl.place(x=0*w,y=0*h,width=130*w,height=130*h)
        

    # second image
        img2=Image.open(r"Image Content\main1.jpg")
        img2=img2.resize((int(1000*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=130*w,y=0*h,width=1000*w,height=130*h)
    
    # Third image
        img3=Image.open(r"Image Content\main2.png")
        img3=img3.resize((int(150*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1130*w,y=0*h,width=150*w,height=130*h)

    # Background image
        img4=Image.open(r"Image Content\bgimage.jpg")
        img4=img4.resize((int(1280*w),int(590*h)),Image.Resampling.NEAREST)
        
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0*w,y=130*h,width=1280*w,height=590*h)
        

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Segoe Print",int(28*w),"bold"),bg="red",fg="white")
        title_lbl.place(x=0*w,y=0*h,width=1280*w,height=35*h)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10*w,y=50*h,width=1250*w,height=480*h)

    #Left Lable Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",int(12*w),"bold"))
        Left_frame.place(x=2*w,y=5*h,width=610*w,height=470*h)

        img_left=Image.open(r"Image Content\face3.jpg")
        img_left=img_left.resize((int(590*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_img_lbl=Label(Left_frame,image=self.photoimg_left)
        f_img_lbl.place(x=5*w,y=0*h,width=590*w,height=100*h)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",int(12*w),"bold"))
        current_course_frame.place(x=5*w,y=110*h,width=580*w,height=100*h)

        
        #department
        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",int(12*w),"bold"),bg="white")
        dep_lable.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Department,font=("times new roman",int(12*w),"bold"),width=int(14*w),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)



        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",int(12*w),"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",int(12*w),"bold"),width=int(14*w),state="readonly")
        course_combo["values"]=("Select Course","BSc","BCA","BE","TE","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)


        #year
        Year_label=Label(current_course_frame,text="Year",font=("times new roman",int(12*w),"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=5,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",int(12*w),"bold"),width=int(14*w),state="readonly")
        Year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=0,pady=10,sticky=W)


        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",int(12*w),"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Semester,font=("times new roman",int(12*w),"bold"),width=int(14*w),state="readonly")
        semester_combo["values"]=("Select Semester","Semester - 1","Semester - 2","Semester - 3","Semester - 4","Semester - 5","Semester - 6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        student_frame.place(x=5*w,y=220*h,width=580*w,height=210*h)


        #student id
        studentId_label=Label(student_frame,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        studentId_entry=ttk.Entry(student_frame,textvariable=self.var_Student_Id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #student name
        studentName_label=Label(student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_Student_Name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        #student roll
        roll_no_label=Label(student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        roll_no_entry=ttk.Entry(student_frame,textvariable=self.var_Roll_No,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=0,column=5,padx=5,pady=10,sticky=W)

        #gender
        gender_label=Label(student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),width=int(12*w),state="readonly")
        gender_combo["values"]=("Select Gender","MALE","FEMALE","OTHERS")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        #dob
        dob_label=Label(student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=5,sticky=W)

        #phone
        phone_label=Label(student_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=1,column=4,padx=5,pady=10,sticky=W)

        phone_entry=ttk.Entry(student_frame,textvariable=self.var_Phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=1,column=5,padx=5,pady=10,sticky=W)

        #email address
        email_label=Label(student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        email_entry=ttk.Entry(student_frame,textvariable=self.var_Email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=10,sticky=W)

        #address
        address_label=Label(student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=5,pady=10,sticky=W)

        address_entry=ttk.Entry(student_frame,textvariable=self.var_Address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=3,padx=5,pady=10,sticky=W)


        #photo
        
        Radiobutton1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=4,column=0,padx=10,pady=10)

        #no photo
        Radiobutton2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=4,column=1,padx=10,pady=10)

        #button frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=20,y=180,width=800,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=30,y=240,width=780,height=35)

        take_photo_btn=Button(btn_frame1,text="TAKE PHOTO SAMPLE",command=self.generate_dataset,width=42,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="UPDATE PHOTO SAMPLE",width=42,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        
















    #Right Lable Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Search Details",font=("times new roman",int(12*w),"bold"))
        Right_frame.place(x=620*w,y=5*h,width=620*w,height=470*h)

        img_right=Image.open(r"Image Content\face6.jpg")
        img_right=img_right.resize((int(590*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_img_lbl=Label(Right_frame,image=self.photoimg_right)
        f_img_lbl.place(x=5*w,y=0*h,width=590*w,height=100*h)

        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5*w,y=110*h,width=590*w,height=50*h)

        search_label=Label(Search_frame,text="Search Bar",font=("times new roman",12,"bold"),bg="Red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        # ==========Search System===========
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),width=int(14*w),state="readonly")
        search_combo["values"]=("Select Course","Roll","Phone","Stu_Id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        search_btn=Button(Search_frame,text="Search",command=self.search_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5,sticky=W)

        showAll_btn=Button(Search_frame,text="Show All",command=self.fetch_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5,sticky=W)


        #===============table frame===============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5*w,y=160*h,width=590*w,height=270*h)


        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Student Id","Student Name","Roll No","Gender","Dob","Phone","Email","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student Id",text="Student Id")
        self.student_table.heading("Student Name",text="Student Name")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Dob",text="D.o.b")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student Id",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #==========function declaration=========
    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Student_Name.get()=="" or self.var_Student_Id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_Department.get(),
                                                                            self.var_Course.get(),
                                                                            self.var_Year.get(),
                                                                            self.var_Semester.get(),
                                                                            self.var_Student_Id.get(),
                                                                            self.var_Student_Name.get(),
                                                                            self.var_Roll_No.get(),
                                                                            self.var_Gender.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_Phone.get(),
                                                                            self.var_Email.get(),
                                                                            self.var_Address.get(),
                                                                            self.var_radio1.get()
                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==========fetch data===============

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #====get cursor=======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_Department.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Student_Id.set(data[4]),
        self.var_Student_Name.set(data[5]),
        self.var_Roll_No.set(data[6]),
        self.var_Gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_Phone.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Address.set(data[11]),
        self.var_radio1.set(data[12])


    #=============update==========
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Student_Name.get()=="" or self.var_Student_Id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        else:
            try:
                update=messagebox.askyesno("Update","Do You Want To Update This Student Details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Stu_name=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Photosample=%s where Stu_Id=%s",(
                                                                                                                                            self.var_Department.get(),
                                                                                                                                            self.var_Course.get(),
                                                                                                                                            self.var_Year.get(),
                                                                                                                                            self.var_Semester.get(),
                                                                                                                                            
                                                                                                                                            self.var_Student_Name.get(),
                                                                                                                                            self.var_Roll_No.get(),
                                                                                                                                            self.var_Gender.get(),
                                                                                                                                            self.var_dob.get(),
                                                                                                                                            self.var_Phone.get(),
                                                                                                                                            self.var_Email.get(),
                                                                                                                                            self.var_Address.get(),
                                                                                                                                            self.var_radio1.get(),
                                                                                                                                            self.var_Student_Id.get(),
                                                                                                                                            
                                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
    

    def delete_data(self):
        if self.var_Student_Id.get()=="":
            messagebox.showerror("Error","Student Id Should Be Requried",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Remove This Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Stu_Id=%s"
                    val=(self.var_Student_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Student_Id.set("")
        self.var_Student_Name.set("")
        self.var_Roll_No.set("")
        self.var_Gender.set("")
        self.var_dob.set("")
        self.var_Phone.set("")
        self.var_Email.set("")
        self.var_Address.set("")
        self.var_Photo.set("")
        self.var_radio1.set("")


    # search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)



    #========Generate Data Set or Photo Sample==========
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Student_Name.get()=="" or self.var_Student_Id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Stu_name=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Photosample=%s where Stu_Id=%s",(
                                                                                                                                            self.var_Department.get(),
                                                                                                                                            self.var_Course.get(),
                                                                                                                                            self.var_Year.get(),
                                                                                                                                            self.var_Semester.get(),
                                                                                                                                            
                                                                                                                                            self.var_Student_Name.get(),
                                                                                                                                            self.var_Roll_No.get(),
                                                                                                                                            self.var_Gender.get(),
                                                                                                                                            self.var_dob.get(),
                                                                                                                                            self.var_Phone.get(),
                                                                                                                                            self.var_Email.get(),
                                                                                                                                            self.var_Address.get(),
                                                                                                                                            self.var_radio1.get(),
                                                                                                                                            self.var_Student_Id.get()==id+1
                                                                                                                                            
                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========= load predefined data on face
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                #======scaling factor=1.3
                #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets Completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

        



if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    
    root.mainloop()