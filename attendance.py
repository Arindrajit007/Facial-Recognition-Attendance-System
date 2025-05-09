from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        img=Image.open(r"C:\Users\SNEHA PANJA\OneDrive\Desktop\Face Recognition\college_images\smart-attendance.jpg")
        img=img.resize((620,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=620,height=150)


        img1=Image.open(r"C:\Users\SNEHA PANJA\OneDrive\Desktop\Face Recognition\college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((650,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=620,y=0,width=650,height=150)


        img3=Image.open(r"C:\Users\SNEHA PANJA\OneDrive\Desktop\Face Recognition\college_images\wp2551980.jpg")
        img3=img3.resize((1530,570),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=570)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=45,width=1260,height=440)


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student's Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=630,height=425)

        img_left=Image.open(r"C:\Users\SNEHA PANJA\OneDrive\Desktop\Face Recognition\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((615,100),Image.ANTIALIAS)
        self.PhotoImage_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.PhotoImage_left)
        f_lbl.place(x=5,y=0,width=615,height=100)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=105,width=625,height=295)

        attendanceId_label=Label(left_inside_frame,text="Attendance Id :",font=("comicsansns",11,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("comicsansns",11,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)


        rollLabel=Label(left_inside_frame,text="Roll :",font=("comicsansns",11,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("comicsansns",11,"bold"))
        atten_roll.grid(row=0,column=3,padx=5,sticky=W)


        nameLabel=Label(left_inside_frame,text="Name :",font=("comicsansns",11,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=25,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("comicsansns",11,"bold"))
        atten_name.grid(row=1,column=1,padx=5,sticky=W)


        depLabel=Label(left_inside_frame,text="Department :",font=("comicsansns",11,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=5,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns",11,"bold"))
        atten_dep.grid(row=1,column=3,padx=5,sticky=W)



        timeLabel=Label(left_inside_frame,text="Time :",font=("comicsansns",11,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=25,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("comicsansns",11,"bold"))
        atten_time.grid(row=2,column=1,padx=5,pady=5,sticky=W)



        dateLabel=Label(left_inside_frame,text="Date :",font=("comicsansns",11,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns",11,"bold"))
        atten_date.grid(row=2,column=3,padx=5,pady=5,sticky=W)





        attendanceLabel=Label(left_inside_frame,text="Attendance Status :",font=("comicsansns",11,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("comicsansns",11,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=5,pady=5,sticky=W)



        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=620,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)









        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=645,y=10,width=600,height=425)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=587,height=395)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)




        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)





    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)

    def importcsv(self):
       global mydata
       mydata.clear()
       fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
       with open(fln) as myfile:
          csvread=csv.reader(myfile,delimiter=",")
          for i in csvread:
             mydata.append(i)
          self.fetchData(mydata)







    def exportCsv(self):
       try:
          if len(mydata)<1:
             messagebox.showerror("No Data","No Data Found",parent=self.root)
             return False
          fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
          with open(fln,mode="w",newline="") as myfile:
             exp_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
                exp_write.writerow(i)
             messagebox.showinfo("Data Export","Data Exported To"+os.path.basename(fln)+"Successfully")
       except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
           
          
             
             
       














if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()