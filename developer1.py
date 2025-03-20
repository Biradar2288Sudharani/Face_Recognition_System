from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x768+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # Title name given
        title_lbl=Label(self.root,text="Developer Information",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=55)
        
        # Background Image Creating
        img_bg=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\d.png")
        img_bg=img_bg.resize((1366,730))
        self.photoimage_bg=ImageTk.PhotoImage(img_bg)

        f_lbl=Label(self.root,image=self.photoimage_bg)
        f_lbl.place(x=0,y=55,width=1366,height=730)

        # Frame Creation 
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=890,y=0,width=475,height=648)

        img_top=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\sudha.jpg")
        img_top=img_top.resize((160,200))
        self.photoimage_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(main_frame,image=self.photoimage_top)
        f_lbl.place(x=0,y=0,width=160,height=200)

        # Developer Information
        dev_label=Label(main_frame,text="Hello ",font=("times new roman",15,"bold"),fg="white",bg="black")
        dev_label.place(x=180,y=10)

        dev_label=Label(main_frame,text="My name is ",font=("times new roman",16,"bold"),fg="white",bg="black")
        dev_label.place(x=180,y=40)

        dev_label=Label(main_frame,text="Biradar Sudharani",font=("times new roman",17,"bold"),fg="white",bg="black")
        dev_label.place(x=180,y=70)

        dev_label=Label(main_frame,text="I am fullstack developer",font=("times new roman",17,"bold"),fg="white",bg="black")
        dev_label.place(x=180,y=100)    

        dev_label=Label(main_frame,text="My qualification is BTech in,",font=("times new roman",17,"bold"),fg="white",bg="black")
        dev_label.place(x=180,y=130)

        dev_label=Label(main_frame,text="Computer Science",font=("times new roman",17,"bold"),fg="white",bg="black")
        dev_label.place(x=180,y=160)

        img1=Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\college_images\d2.png")
        img1=img1.resize((500,690))
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame,image=self.photoimage1)
        f_lbl.place(x=0,y=200,width=470,height=550)

if __name__== " __main__ ":
    root=Tk()
    obj=Developer(root)
    root.mainloop()