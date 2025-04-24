from tkinter import*
from PIL import Image,ImageTk
from tkinter import*

from PIL import Image,ImageTk





class Developer:
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
        

        title_lbl=Label(bg_lbl,text="DEVELOPER",font=("Segoe Print",int(28*w),"bold"),bg="navy blue",fg="white")
        title_lbl.place(x=0*w,y=0*h,width=1280*w,height=35*h)


        



        img2=Image.open(r"Image Content\sumon.jpg")
        img2=img2.resize((int(200*w),int(280*h)),Image.Resampling.NEAREST)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(bg_lbl,image=self.photoimg2)
        f_lbl.place(x=550*w,y=50*h,width=200*w,height=280*h)

        #devel level
        dev_label=Label(bg_lbl,text="Name - Sumon Karar.",font=("comicsansns",int(15*w),"bold"),bg="white")
        dev_label.place(x=500*w,y=350*h)

        dev1_label=Label(bg_lbl,text="Address - Alamohan Das Road , Howrah 711105.",font=("comicsansns",int(13*w),"bold"),bg="white")
        dev1_label.place(x=500*w,y=380*h)

        dev2_label=Label(bg_lbl,text="CONTACT DETAILS :- Gmail - Kararsumon23@gmail.com",font=("comicsansns",int(13*w),"bold"),bg="white")
        dev2_label.place(x=500*w,y=410*h)
        dev4_label=Label(bg_lbl,text="Phone - +916289833021",font=("comicsansns",int(13*w),"bold"),bg="white")
        dev4_label.place(x=675*w,y=433*h)

        dev5_label=Label(bg_lbl,text="DEGREE :- BCA",font=("comicsansns",int(13*w),"bold"),bg="white")
        dev5_label.place(x=500*w,y=470*h)
        dev6_label=Label(bg_lbl,text="COLLEGE :- Techno India, Saltlake",font=("comicsansns",int(13*w),"bold"),bg="white")
        dev6_label.place(x=500*w,y=500*h)















if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()