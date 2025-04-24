from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class show_Table:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")
        S_w=root.winfo_screenwidth()
        S_h=root.winfo_screenheight()
        if S_w > 1280:
            wd = S_w / 1280
        else:
            wd = 1 / (1280 / S_w) 
        print (wd)

        if S_h > 720:
            hd = S_h / 720
        else:
            hd = 1 / (720 / S_h) 
        print (hd)



    
    # Background image
        img4=Image.open(r"Image Content\time_table.jpg")
        img4=img4.resize((int(1280*wd),int(720*hd)),Image.Resampling.NEAREST)
        
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=0,width=1280*wd,height=720*hd)

        title_lbl=Label(bg_lbl,text="TIME TABLE",font=("times new roman",28,"bold"),bg="navy blue",fg="white")
        title_lbl.place(x=0,y=0,width=1280*wd,height=35*hd)




















if __name__ == "__main__":
    root=Tk()
    obj=show_Table(root)
    root.mainloop()