from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from showimg import show_Table
import tkinter



class Time_Table:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")
        S_w=root.winfo_screenwidth()
        S_h=root.winfo_screenheight()
        print (S_w, S_h)
        if S_w > 1280:
            w = S_w / 1280
        else:
            w = 1 / (1280 / S_w) 
        if S_h > 720:
            h = S_h / 720
        else:
            h = 1 / (720 / S_h)


    #=======================variables=====================
        self.var_shift=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()

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

        title_lbl=Label(bg_lbl,text="TIME TABLE",font=("times new roman",28,"bold"),bg="navy blue",fg="white")
        title_lbl.place(x=0*w,y=0*h,width=1280*w,height=35*h)

        

    #left label frame
        #Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="TIME TABLE",font=("times new roman",12,"bold"))
        #Left_frame.place(x=10,y=10,width=620,height=520)

        img_left=Image.open(r"Image Content\schedule.jpg")
        img_left=img_left.resize((int(610*w),int(100*h)),Image.Resampling.NEAREST)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(bg_lbl,image=self.photoimg_left)
        f_lbl.place(x=300*w,y=50*h,width=610*w,height=100*h)

    #shift
        current_course_frame=LabelFrame(bg_lbl,bd=2,bg="red",relief=RIDGE,text="Current Course Information",font=("times new roman",int(12*w),"bold"),fg="yellow")
        current_course_frame.place(x=300*w,y=160*h,width=600*w,height=160*h)

        dep_label=Label(current_course_frame,text="SHIFT",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_shift,font=("times new roman",int(12*w),"bold"),width=int(50*w),state="read")
        dep_combo["values"]=("Select SHIFT","MORNING SHIFT","DAY SHIFT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10)

    #course
        dep2_label=Label(current_course_frame,text="COURSE",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        dep2_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        dep2_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",int(12*w),"bold"),width=int(50*w),state="read")
        dep2_combo["values"]=("Select COURSE","B.A HONOURS","B.A GENERAL","B.COM HONOURS","B.COM GENERAL","B.B.A HONOURS","B.Sc COMPUTER SCIENCE HONOURS","B.Sc COMPUTER APPLICATION","B.Sc PHYSICS HONOURS","B.Sc CHEMISTRY HONOURS","B.Sc MATHEMATICS HONOURS","DEPARTMENT OF TELECOMUNICATION & TECHNOLOGY")
        dep2_combo.current(0)
        dep2_combo.grid(row=1,column=1,padx=3,pady=10)

    #semester
        dep3_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        dep3_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        dep3_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",int(12*w),"bold"),width=int(50*w),state="read")
        dep3_combo["values"]=("Select SEMESTER","SEMESTER 1","SEMESTER 2","SEMESTER 3","SEMESTER 4","SEMESTER 5","SEMESTER 6","SEMESTER 7","SEMESTER 8")
        dep3_combo.current(0)
        dep3_combo.grid(row=2,column=1,padx=3,pady=10)

    #submit button
        smit_btn=Button(bg_lbl,text="SHOW TIME TABLE",command=self.check_data,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        smit_btn.place(x=400*w,y=350*h,width=397*w,height=70*h)

    #Exit button
        
        smit_btn=Button(bg_lbl,text="Exit",command=self.iexit,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        smit_btn.place(x=550*w,y=450*h,width=102*w,height=70*h)

    


    
    #=====================function declaration========================
    
    
    def check_data(self):
        
        if self.var_shift.get()=="Select SHIFT" or self.var_course.get()=="Select COURSE" or self.var_sem.get()=="Select SEMESTER":
            messagebox.showerror(title="Error", message="All Fields are Required",parent=self.root)
        else:
            self.new_window=Toplevel(self.root)
            self.t_t=show_Table(self.new_window)


    def show_table(self):
        self.new_window=Toplevel(self.root)
        self.t_t=show_Table(self.new_window)

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno(title="Face Recognition", message="Are You Want to Exit",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return





if __name__ == "__main__":
    root=Tk()
    obj=Time_Table(root)
    root.mainloop()