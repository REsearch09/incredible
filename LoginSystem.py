import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("Login System")# Başlığımız
root.geometry("320x250")# Ekranın ne kadarı gözükçğinni gözteriyor


userLabel = Label(root, width=20 , height=3,text="USERNAME    :",font="Times 10 bold")# Username Yazısı
userLabel.place(x=3,y=26)

passLabel = Label(root, width=20 , height=3,text="PASSWORD    :",font="Times 10 bold")# Password Yazısı
passLabel.place(x=4,y=66)


userEntry = Entry(root, width=15,font="Tiems 9 bold")
userEntry.place(x=140,y=40)

passEntry = Entry(root,width=15,font="Tiems 9 bold")
passEntry.place(x=140,y=80)

def userControl():
    if  userEntry.get() == "Ahmet Akif" and passEntry.get() == "pyhton":
        tk.messagebox.showinfo("Congralitaions!!", "True Information")
    else:
        tk.messagebox.showinfo("Try Again :( ", "Flase Information")
        
controlButton = Button(root,width=30,text="LOGIN",font="Times 11 bold",command=userControl)
controlButton.place(x=15,y=150)



root.mainloop()
