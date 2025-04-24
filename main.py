from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import student
from face_recognition import face_recognitions
from timetable import Time_Table
from tkinter import messagebox
from attendance import Attendance
from developer import Developer
#from train import train
import os
import cv2
import numpy as np
#from help import Help_Desk
#from developer import develop



class Face_Recognition_System:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")
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
        

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Segoe Print",int(28*w),"bold"),bg="navy blue",fg="white")
        title_lbl.place(x=0*w,y=0*h,width=1280*w,height=35*h)

    # Student Button
        img5=Image.open(r"Image Content\student.png")
        img5=img5.resize((int(50*w),int(h*50)),Image.Resampling.NEAREST)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,command=self.student_details,cursor="hand1")
        #b1.grid(padx=50,pady=50)
        b1.place(x=50*w,y=50*h,width=50*w,height=50*h)
        b1_1=Button(bg_lbl,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        b1_1.place(x=125*w,y=50*h,width=500*w,height=50*h)

    # Detect Face Button
        img6=Image.open(r"Image Content\faced.jpg")
        img6=img6.resize((int(w*75),int(75*h)),Image.Resampling.NEAREST)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_lbl,image=self.photoimg6,command=self.face_recog)
        b2.place(x=50*w,y=150*h,width=50*w,height=50*h)
        b2_2=Button(bg_lbl,text="FACE DETECT",command=self.face_recog,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        b2_2.place(x=125*w,y=150*h,width=500*w,height=50*h)

    # Attendance
        img7=Image.open(r"Image Content\atten.jpg")
        img7=img7.resize((int(w*75),int(h*75)),Image.Resampling.NEAREST)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_lbl,image=self.photoimg7,command=self.att)
        b3.place(x=50*w,y=250*h,width=50*w,height=50*h)
        b3_3=Button(bg_lbl,text="ATTENDANCE",command=self.att,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        b3_3.place(x=125*w,y=250*h,width=500*w,height=50*h)

    # Photo Gallery
        img8=Image.open(r"Image Content\gal.png")
        img8=img8.resize((int(w*75),int(h*75)),Image.Resampling.NEAREST)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_lbl,image=self.photoimg8,command=self.open_img)
        b4.place(x=50*w,y=350*h,width=50*w,height=50*h)
        b4_4=Button(bg_lbl,text="PHOTO GALLARY",command=self.open_img,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        b4_4.place(x=125*w,y=350*h,width=500*w,height=50*h)

    # Time Table
        img9=Image.open(r"Image Content\timetable.jpg")
        img9=img9.resize((int(w*75),int(h*75)),Image.Resampling.NEAREST)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_lbl,image=self.photoimg9,command=self.time_table)
        b5.place(x=50*w,y=450*h,width=50*w,height=50*h)
        b5_5=Button(bg_lbl,text="TIME TABLE",command=self.time_table,font=("times new roman",int(28*w),"bold"),bg="navy blue",fg="white")
        b5_5.place(x=125*w,y=450*h,width=500*w,height=50*h)



    # Train Image
        img10_1=Image.open(r"Image Content\train.jpg")
        img10_1=img10_1.resize((int(w*150),int(h*150)),Image.Resampling.NEAREST)
        self.photoimg10_1=ImageTk.PhotoImage(img10_1)

        b6_1=Button(bg_lbl,image=self.photoimg10_1,command=self.train_classifier)
        b6_1.place(x=750*w,y=100*h,width=150*w,height=150*h)
        b6_6_1=Button(bg_lbl,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",int(18*w),"bold"),bg="navy blue",fg="white")
        b6_6_1.place(x=750*w,y=250*h,width=150*w,height=50*h)

    # Help Desk
    #    img10=Image.open(r"Image Content\helpdesk.png")
    #    img10=img10.resize((int(w*150),int(h*150)),Image.Resampling.NEAREST)
    #    self.photoimg10=ImageTk.PhotoImage(img10)
#
    #    b6=Button(bg_lbl,image=self.photoimg10,command=self.help)
     #   b6.place(x=850*w,y=100*h,width=150*w,height=150*h)
    #    b6_6=Button(bg_lbl,text="HELP DESK",command=self.help,font=("times new roman",int(18*w),"bold"),bg="navy blue",fg="white")
    #    b6_6.place(x=850*w,y=250*h,width=150*w,height=50*h)

    #Developer Button
        img110=Image.open(r"Image Content\devel1.png")
        img110=img110.resize((int(w*150),int(h*150)),Image.Resampling.NEAREST)
        self.photoimg110=ImageTk.PhotoImage(img110)

        b61=Button(bg_lbl,image=self.photoimg110,command=self.devel)
        b61.place(x=950*w,y=100*h,width=150*w,height=150*h)
        b6_61=Button(bg_lbl,text="DEVELOPER",command=self.devel,font=("times new roman",int(17*w),"bold"),bg="navy blue",fg="white")
        b6_61.place(x=950*w,y=250*h,width=150*w,height=50*h)

    # Exit
        img11=Image.open(r"Image Content\exit.jpg")
        img11=img11.resize((int(w*150),int(h*150)),Image.Resampling.NEAREST)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_lbl,image=self.photoimg11,command=self.iexit)
        b7.place(x=850*w,y=350*h,width=150*w,height=150*h)
        b7_7=Button(bg_lbl,text="EXIT",command=self.iexit,font=("times new roman",int(18*w),"bold"),bg="navy blue",fg="white")
        b7_7.place(x=850*w,y=500*h,width=150*w,height=50*h)




    #==============FUNCTION BUTTONS===================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.s_d=student(self.new_window)

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.s_d=face_recognitions(self.new_window)

    def time_table(self):
        self.new_window=Toplevel(self.root)
        self.t_t=Time_Table(self.new_window)
    
    #def help(self):
        #self.new_window=Toplevel(self.root)
        #self.h=Help_Desk(self.new_window)

    def devel(self):
        self.new_window=Toplevel(self.root)
        self.dev=Developer(self.new_window)

    def att(self):
        self.new_window=Toplevel(self.root)
        self.atte=Attendance(self.new_window)

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno(title="Face Recognition", message="Do You Want to Exit - Then Get Lost",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return
        
    #=============train image==============

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')          #gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #==========train classifier and save=======

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSet Completed!!")
    
    def open_img(self):
        os.startfile("data")


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    
    root.mainloop()


    

