from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")






        self.var_Department=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_Student_Id=StringVar()
        self.var_Student_Name=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Teacher_Name=StringVar()
        self.var_Photo=StringVar()
        self.var_usertype=StringVar()
    
































        img=Image.open(r"D:\Facial Recognition attendace\Image Content\XYZins.jpg")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)


        img1=Image.open(r"D:\Facial Recognition attendace\Image Content\main1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)


        img2=Image.open(r"D:\Facial Recognition attendace\Image Content\main2.png")
        img2=img2.resize((400,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=400,height=130)




        img3=Image.open(r"D:\Facial Recognition attendace\Image Content\bgimage.jpg")
        img3=img3.resize((1530,570),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=570)




        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=45,width=1500,height=460)


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=580)


        img_left=Image.open(r"D:\Facial Recognition attendace\Image Content\bgimage.jpg")
        img_left=img_left.resize((590,100),Image.ANTIALIAS)
        self.PhotoImage_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.PhotoImage_left)
        f_lbl.place(x=5,y=0,width=590,height=100)

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=105,width=590,height=100)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Department,font=("times new roman",13,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Bachelor Of Computer Application","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)



        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BCA","BE","TE","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)



        Year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=5,sticky=W)
        

        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),state="readonly")
        Year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=0,pady=10,sticky=W)



        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)
        

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester - 1","Semester - 2","Semester - 3","Semester - 4","Semester - 5","Semester - 6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)





        student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        student_frame.place(x=5,y=210,width=590,height=210)

        studentId_label=Label(student_frame,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)

        studentId_entry=ttk.Entry(student_frame,textvariable=self.var_Student_Id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,sticky=W)



        studentName_label=Label(student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,sticky=W)

        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_Student_Name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,sticky=W)



        roll_no_label=Label(student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=5,sticky=W)

        roll_no_entry=ttk.Entry(student_frame,textvariable=self.var_Roll_No,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=5,sticky=W)




        teacher_label=Label(student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=1,column=2,padx=5,sticky=W)

        teacher_entry=ttk.Entry(student_frame,textvariable=self.var_Teacher_Name,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=1,column=3,padx=5,sticky=W)



        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=4,column=0)

        Radiobutton2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=4,column=1)

        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=80,width=580,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        btn_frame1=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=120,width=580,height=100)



        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)



        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


 



















        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=625,height=580)




        img_Right=Image.open(r"")
        img_Right=img_Right.resize((610,100),Image.ANTIALIAS)
        self.PhotoImage_Right=ImageTk.PhotoImage(img_Right)

        f_lbl=Label(Right_frame,image=self.PhotoImage_Right)
        f_lbl.place(x=5,y=0,width=610,height=100)



        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=110,width=610,height=70)

        search_label=Label(search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Student Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)


        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)






        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)


        showall_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)






        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=185,width=610,height=230)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Student Id","Student Name","Roll No","Teacher Name","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

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
        self.student_table.heading("Teacher Name",text="Teacher Name")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student Id",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Teacher Name",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    


    

if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()