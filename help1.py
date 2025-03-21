from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql
import os

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # Title name given
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=55)
        
        # Top Left Image Creating
        top_left_img=Image.open(r"C:college_images\hd.png")
        top_left_img=top_left_img.resize((683,325))
        self.photoimage_top_left=ImageTk.PhotoImage(top_left_img)

        f_lbl=Label(self.root,image=self.photoimage_top_left)
        f_lbl.place(x=0,y=55,width=683,height=325)

        # Call logo inserted into top left image
        call_logo_img=Image.open(r"C:college_images\c.png")
        call_logo_img=call_logo_img.resize((40,40))
        self.photoimage_call_logo=ImageTk.PhotoImage(call_logo_img)

        f_lbl=Label(self.root,image=self.photoimage_call_logo)
        f_lbl.place(x=250,y=195,width=40,height=40)

        # Phone number inserted in top left imagen
        phone_num=Label(self.root,text="7709298002",font=("times new roman",20,"bold"),bg="black",fg="pink")
        phone_num.place(x=300,y=190,width=150,height=25)

        phone_num=Label(self.root,text="9686171763",font=("times new roman",20,"bold"),bg="black",fg="pink")
        phone_num.place(x=300,y=215,width=150,height=25)

        # Top Right Image Creating
        top_right_img=Image.open(r"C:college_images\hd.png")
        top_right_img=top_right_img.resize((683,325))
        self.photoimage_top_right=ImageTk.PhotoImage(top_right_img)

        f_lbl=Label(self.root,image=self.photoimage_top_right)
        f_lbl.place(x=683,y=55,width=683,height=325)

        # Linkdin logo inserted into top right image
        linkdin_logo_img=Image.open(r"C:college_images\l.png")
        linkdin_logo_img=linkdin_logo_img.resize((40,40))
        self.photoimage_linkdin_logo=ImageTk.PhotoImage(linkdin_logo_img)

        f_lbl=Label(self.root,image=self.photoimage_linkdin_logo)
        f_lbl.place(x=850,y=198,width=40,height=40)

        # Linkdin ID inserted in top right image
        linkdin_id=Label(self.root,text="https://www.linkedin.com",font=("times new roman",20,"bold"),bg="black",fg="orange")
        linkdin_id.place(x=900,y=175,width=300,height=25)

        linkdin_id=Label(self.root,text="/in/sudharani-biradar",font=("times new roman",20,"bold"),bg="black",fg="orange")
        linkdin_id.place(x=900,y=200,width=300,height=25)

        linkdin_id=Label(self.root,text="-40b280278",font=("times new roman",20,"bold"),bg="black",fg="orange")
        linkdin_id.place(x=900,y=225,width=300,height=25)

        # Bottom Right Image Creating
        bottom_left_img=Image.open(r"C:college_images\hd.png")
        bottom_left_img=bottom_left_img.resize((683,325))
        self.photoimage_bottom_left=ImageTk.PhotoImage(bottom_left_img)

        f_lbl=Label(self.root,image=self.photoimage_bottom_left)
        f_lbl.place(x=0,y=380,width=683,height=325)

        # GitHub logo inserted into bottom right image
        github_logo_img=Image.open(r"C:college_images\g.png")
        github_logo_img=github_logo_img.resize((50,50))
        self.photoimage_github_logo=ImageTk.PhotoImage(github_logo_img)

        f_lbl=Label(self.root,image=self.photoimage_github_logo)
        f_lbl.place(x=180,y=515,width=50,height=50)

        # GitHub ID inserted in top right image
        github_id=Label(self.root,text="https://github.com/",font=("times new roman",20,"bold"),bg="black",fg="blue")
        github_id.place(x=240,y=515,width=270,height=25)

        github_id=Label(self.root,text="Biradar2288Sudharani",font=("times new roman",20,"bold"),bg="black",fg="blue")
        github_id.place(x=240,y=540,width=270,height=25)

        # Bottom Right Image Creating
        bottom_right_img=Image.open(r"C:college_images\hd.png")
        bottom_right_img=bottom_right_img.resize((683,325))
        self.photoimage_bottom_right=ImageTk.PhotoImage(bottom_right_img)

        f_lbl=Label(self.root,image=self.photoimage_bottom_right)
        f_lbl.place(x=683,y=380,width=683,height=325)

        # Email logo inserted into bottom right image
        email_logo_img=Image.open(r"C:college_images\e2.png")
        email_logo_img=email_logo_img.resize((40,40))
        self.photoimage_email_logo=ImageTk.PhotoImage(email_logo_img)

        f_lbl=Label(self.root,image=self.photoimage_email_logo)
        f_lbl.place(x=880,y=525,width=40,height=40)

        # Email ID inserted in top right image
        email_id=Label(self.root,text="sudharanibiradar970",font=("times new roman",20,"bold"),bg="black",fg="purple")
        email_id.place(x=930,y=520,width=250,height=25)

        email_id=Label(self.root,text="@gmail.com",font=("times new roman",20,"bold"),bg="black",fg="purple")
        email_id.place(x=930,y=545,width=250,height=25)      

   
        
if __name__== " __main__ ":
    root=Tk()
    obj=Help(root)
    root.mainloop()