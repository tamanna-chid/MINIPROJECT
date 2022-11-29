from tkinter import*
import datetime
from PIL import ImageTk,Image
root=Tk()
x=datetime.datetime.now()
y=x.hour
bg=Image.open("C:\\Users\\LENOVO\\OneDrive\\Documents\\night.jpg")
bg1=Image.open("C:\\Users\\LENOVO/OneDrive\\Documents\\day.jpg")
if (y-18)>0:
    bg = Image.open("C:\\Users\\LENOVO\\OneDrive\\Documents\\night.jpg")
    b1=ImageTk.PhotoImage(bg)
    root.geometry("300x300")
    lbl=Label(root,image=b1)
    lbl.place(x=0,y=0)
else:
    bg1 = Image.open("C:\\Users\\LENOVO/OneDrive\\Documents\\day.jpg")
    b2=ImageTk.PhotoImage(bg1)
    root.geometry("300x300")
    lbl1=Label(root,image=b2)
    lbl1.place(x=0,y=0)
label=Label(root,text="Click to Select Place",highlightcolor='black',anchor=CENTER)
label.pack(pady=50)
clicked=StringVar()
main_menu=OptionMenu(root,clicked,"Bangalore","Delhi","Kolkata","Jaipur","Shimla","Chennai")
main_menu.pack()
root.mainloop()
