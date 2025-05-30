from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class face_recognitions:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Train Img")
        self.attendance_cooldown = 10  # Set the cooldown time to 60 seconds
        self.last_attendance_time = datetime.now()
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


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Segoe Print",int(28*w),"bold"),bg="red",fg="white")
        title_lbl.place(x=0*w,y=0*h,width=1280*w,height=35*h)

        img_top=Image.open(r"Image Content\img_detect.jpeg")
        img_top=img_top.resize((int(1280*w),int(300*h)),Image.Resampling.NEAREST)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_img_lbl=Label(self.root,image=self.photoimg_top)
        f_img_lbl.place(x=0*w,y=50*h,width=1280*w,height=250*h)

        b1_1=Button(self.root,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",30,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=0*w,y=320*h,width=1260*w,height=60*h)

        img_bottom=Image.open(r"Image Content\rec_pro.png")
        img_bottom=img_bottom.resize((int(1280*w),int(250*h)),Image.Resampling.NEAREST)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        ff_img_lbl=Label(self.root,image=self.photoimg_bottom)
        ff_img_lbl.place(x=0*w,y=400*h,width=1280*w,height=250*h)


    #====================face recognition==========
    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        time_difference = (now - self.last_attendance_time).total_seconds()

        if time_difference >= self.attendance_cooldown:
            with open("attendance.csv", "a", newline="\n") as f:
                dtString = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                f.write(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
                self.last_attendance_time = now



    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor=1.3,minNeighbors=5)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Arindrajit@6829783",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Stu_Name from student where Stu_Id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)
                #n="+".join(n)

                my_cursor.execute("select Roll from student where Stu_Id="+str(id))
                r=my_cursor.fetchone()
                r=str(r)
                #r="+".join(r)

                my_cursor.execute("select Dep from student where Stu_Id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)
                #d="+".join(d)


                my_cursor.execute("select Stu_Id from student where Stu_Id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)
                #i="+".join(i)



                if confidence>60:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)


                coord=[x,y,w,h]


            return coord
        



        def recognize(img,clf,faceCascade):
             coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
             return img
        

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        #clf=cv2.face.EigenFaceRecognizer_create()
        clf=cv2.face.LBPHFaceRecognizer.create()     # Create LBPH face recognizer
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)


            if cv2.waitKey(1)==13:
                break 
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=face_recognitions(root)
    root.mainloop()