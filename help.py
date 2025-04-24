from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox



class Help_Desk:

    

    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("HELP DESK")
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


        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_query=StringVar()
        

    # first image
        img1=Image.open(r"D:\Facial Recognition attendace\Image Content\XYZins.jpg")
        img1=img1.resize((int(130*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        
        f_lbl.place(x=0*w,y=0*h,width=130*w,height=130*h)
        

    # second image
        img2=Image.open(r"D:\Facial Recognition attendace\Image Content\main1.jpg")
        img2=img2.resize((int(1000*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=130*w,y=0*h,width=1000*w,height=130*h)
    
    # Third image
        img3=Image.open(r"D:\Facial Recognition attendace\Image Content\main2.png")
        img3=img3.resize((int(150*w),int(130*h)),Image.Resampling.NEAREST)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1130*w,y=0*h,width=150*w,height=130*h)
    

    # Background image
        img4=Image.open(r"D:\Facial Recognition attendace\Image Content\bgimage.jpg")
        img4=img4.resize((int(1280*w),int(590*h)),Image.Resampling.NEAREST)
        
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0*w,y=130*h,width=1280*w,height=590*h)

    #left label frame
        Left_frame=LabelFrame(bg_lbl,bd=2,bg="white",relief=RIDGE,text="Help Desk",font=("times new roman",int(12*w),"bold"))
        Left_frame.place(x=10*w,y=10*h,width=620*w,height=520*h)

        img_left=Image.open(r"D:\Facial Recognition attendace\Image Content\help.png")
        img_left=img_left.resize((int(610*w),int(100*h)),Image.Resampling.NEAREST)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5*w,y=0*h,width=610*w,height=100*h)

    #right label frame
        right_frame=LabelFrame(bg_lbl,bd=2,bg="white",relief=RIDGE,text="Questions & Queries",font=("times new roman",int(12*w),"bold"))
        right_frame.place(x=640*w,y=10*h,width=610*w,height=520*h)

        img_right=Image.open(r"D:\Facial Recognition attendace\Image Content\questions.jpg")
        img_right=img_right.resize((int(600*w),int(100*h)),Image.Resampling.NEAREST)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=4*w,y=0*h,width=600*w,height=100*h)

    #name
        current_course_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Details",font=("times new roman",int(12*w),"bold"))
        current_course_frame.place(x=10*w,y=110*h,width=580*w,height=290*h)

        name_tag=Label(current_course_frame,text="NAME",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        name_tag.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        name_combo=ttk.Entry(current_course_frame,textvariable=self.var_name,font=("times new roman",int(12*w),"bold"),width=int(50))
        name_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)


    #course
        dep2_label=Label(current_course_frame,text="COURSE",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        dep2_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        dep2_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",int(12*w),"bold"),width=int(50),state="read")
        dep2_combo["values"]=("Select COURSE","B.A HONOURS","B.A GENERAL","B.COM HONOURS","B.COM GENERAL","B.B.A HONOURS","B.Sc COMPUTER SCIENCE HONOURS","B.Sc COMPUTER APPLICATION","B.Sc PHYSICS HONOURS","B.Sc CHEMISTRY HONOURS","B.Sc MATHEMATICS HONOURS","DEPARTMENT OF TELECOMUNICATION & TECHNOLOGY")
        dep2_combo.current(0)
        dep2_combo.grid(row=1,column=1,padx=3,pady=10)

    #semester
        dep3_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        dep3_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        dep3_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",int(12*w),"bold"),width=int(50),state="read")
        dep3_combo["values"]=("Select SEMESTER","SEMESTER 1","SEMESTER 2","SEMESTER 3","SEMESTER 4","SEMESTER 5","SEMESTER 6","SEMESTER 7","SEMESTER 8")
        dep3_combo.current(0)
        dep3_combo.grid(row=2,column=1,padx=3,pady=10)

    #Query Details

        dep4_label=Label(current_course_frame,text="Query Details",font=("times new roman",int(12*w),"bold"),bg="blue",fg="yellow")
        dep4_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        query_combo=ttk.Entry(current_course_frame,textvariable=self.var_query,width=50,font=("times new roman",int(12*w),"bold"))
        query_combo.grid(row=3,column=1,padx=3,pady=10,sticky=W)

    
    #submit button
        btn_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=100*w,y=410*h,width=397*w,height=70*h)
        
        smit_btn=Button(btn_frame,text="   SUBMIT   QUERY   ",command=self.check_data,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        smit_btn.grid(row=0,column=0)

    









    #================function declaration============

    def check_data(self):
        
        if self.var_name.get()=="" or self.var_query.get()=="" or self.var_course.get()=="Select COURSE" or self.var_sem.get()=="Select SEMESTER":
            messagebox.showerror(title="Error", message="All Fields are Required",parent=self.root)
        else:
            pass
    
        




















if __name__ == "__main__":
    root=Tk()
    obj=Help_Desk(root)
    
    root.mainloop()
