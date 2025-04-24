from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from main import Face_Recognition_System
from tkinter import messagebox
import ast



class sign_up:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("925x500+100+200")
        self.root.title("Face Recognition System")
        root.configure(bg='#fff')
        root.resizable(False,False)




        def signup():
            username=user.get()
            password=code.get()
            confirm=ccode.get()

            if password==confirm:
                try:
                    file=open('datasheet.txt','r+')
                    d=file.read()
                    r=ast.literal_eval(d)

                    dict2={username:password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file=open('datasheet.txt','w')
                    w=file.write(str(r))
                    messagebox.showinfo('SignUp','Successfully Signed Up')


                except:

                    file=open('datasheet.txt','w')
                    pp=str({'username':'password'})
                    file.write(pp)
                    file.close()
            else:
                messagebox.showerror('Invalid','Both Password Should be Same')

        def sign():
            self.root.destroy()





        img11=Image.open(r"Image Content\login.png")
        img11=img11.resize((int(400),int(350)),Image.Resampling.NEAREST)
        self.photoimg11=ImageTk.PhotoImage(img11)

        f_lbl=Label(self.root,image=self.photoimg11)
        
        f_lbl.place(x=50,y=50,width=400,height=350)


        frame=Frame(root,width=350,height=550,bg='white')
        frame.place(x=480,y=70)
        
        heading=Label(frame,text='Sign UP',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)

 #########------------------------------
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')
        user=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=108)
##########------------------------------
        

        def on_enter(e):
            code.delete(0,'end')
        def on_leave(e):
            name=code.get()
            if name=='':
                code.insert(0,'Password')
        code=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
        code.place(x=30,y=150)
        code.insert(0,'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)
        

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=178)

##########----------------------------------

        def on_enter(e):
            ccode.delete(0,'end')
        def on_leave(e):
            name=ccode.get()
            if name=='':
                ccode.insert(0,'Password')
        ccode=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
        ccode.place(x=30,y=220)
        ccode.insert(0,'Confirm Password')
        ccode.bind('<FocusIn>', on_enter)
        ccode.bind('<FocusOut>', on_leave)
        

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=249)

########-------------------------------

        Button(frame,width=40,pady=7,text='SIGN UP',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=300)
        label=Label(frame,text="Have an Account?",fg='black',font=('Microsoft YaHei UI Light',10))
        label.place(x=75,y=350)

        sign_up=Button(frame,width=6,text='Sign In',border=0,command=self.login,bg='white',cursor='hand2',fg='#57a1f8')
        sign_up.place(x=215,y=350)




    def login(self):
        self.new_window=Toplevel(self.root)
        self.t_t=login_page(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=sign_up(root)
    
    root.mainloop()


from login2 import login_page