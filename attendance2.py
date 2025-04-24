from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
#from train import train
import os
import csv
from tkinter import filedialog

#from help import Help_Desk
#from developer import develop


mydata=[]
class Attendance:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


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

        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0*w,y=130*h,width=1280*w,height=590*h)
        

        title_lbl=Label(bg_lbl,text="ATTENDANCE SYSTEM SOFTWARE",font=("Segoe Print",int(28*w),"bold"),bg="navy blue",fg="white")
        title_lbl.place(x=0*w,y=0*h,width=1280*w,height=35*h)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=5*w,y=45*h,width=1260*w,height=440*h)

      #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student's Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10*w,y=10*h,width=630*w,height=425*h)

        img_left=Image.open(r"Image Content\main2.png")
        img_left=img_left.resize((615,100),Image.Resampling.NEAREST)
        self.PhotoImage_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.PhotoImage_left)
        f_lbl.place(x=5*w,y=0*h,width=615*w,height=100*h)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0*w,y=105*h,width=625*w,height=295*h)

        attendanceId_label=Label(left_inside_frame,text="Attendance Id :",font=("comicsansns",int(11*w),"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)


        rollLabel=Label(left_inside_frame,text="Roll :",font=("comicsansns",int(11*w),"bold"),bg="white")
        rollLabel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"))
        atten_roll.grid(row=1,column=1,padx=5,pady=5,sticky=W)


        nameLabel=Label(left_inside_frame,text="Name :",font=("comicsansns",int(11*w),"bold"),bg="white")
        nameLabel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"))
        atten_name.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        depLabel=Label(left_inside_frame,text="Department :",font=("comicsansns",int(11*w),"bold"),bg="white")
        depLabel.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"))
        atten_dep.grid(row=3,column=1,padx=5,pady=5,sticky=W)



        timeLabel=Label(left_inside_frame,text="Time :",font=("comicsansns",int(11*w),"bold"),bg="white")
        timeLabel.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"))
        atten_time.grid(row=4,column=1,padx=5,pady=5,sticky=W)



        dateLabel=Label(left_inside_frame,text="Date :",font=("comicsansns",int(11*w),"bold"),bg="white")
        dateLabel.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"))
        atten_date.grid(row=5,column=1,padx=5,pady=5,sticky=W)





        attendanceLabel=Label(left_inside_frame,text="Attendance Status :",font=("comicsansns",int(11*w),"bold"),bg="white")
        attendanceLabel.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=int(20*w),font=("comicsansns",int(11*w),"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=6,column=1,padx=5,pady=5,sticky=W)



        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=7*w,y=250*h,width=605*w,height=30*h)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=int(16*w),font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=int(16*w),font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=int(16*w),font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=int(16*w),font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)









        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=645*w,y=10*h,width=600*w,height=425*h)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5*w,y=5*h,width=587*w,height=395*h)

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



   #=============fetch data=========

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
          14:15






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