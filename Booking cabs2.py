from tkinter import *
import sqlite3
import tkinter.messagebox
root = Tk()
def forget_password():
   global root
   root.destroy()
   root=Tk()
   eme = StringVar()
   passw=StringVar()
   def forget():
         em=eme.get()
         if em=="":
             tkinter.messagebox.showinfo("sorry", "enter the email")
             return
         print(em)
         with sqlite3.connect("create_form6.db") as db:
             cursor = db.cursor()
         find_user=("SELECT Password,Reg  FROM new_form  WHERE  Email=?  ")
         cursor.execute(find_user,[em])
         result=cursor.fetchall()
         print(str(result))
         if result:
             tkinter.messagebox.showinfo("successfull", "OTP send on email")
             forget_password()
         else:
               tkinter.messagebox.showinfo("sorry", "This email did not registered")
            

   
   Label(root, text="enter the email id ", width=20,fg="black" ).grid(row=6,pady=10,ipady=10, column=4)
   Entry(root,textvar=eme, width=40).grid(row=7,column=4,pady=5,ipady=4)
   Label(root,text="",width=40).grid(row=8,column=4)
   Button(root, text=' send', width=10, fg="white", bg="skyblue", bd=1, font=('arial', 10, 'bold'),command=forget).grid(row=7, column=5,sticky=W,ipady=4,padx=1,pady=0,columnspan=4)
   Button(root, text=' login ', width=10, fg="white", bg="blue", bd=1, font=('arial', 10, 'bold'),command=login_page).grid(row=1, column=5,sticky=W,ipady=4,padx=1,pady=0,columnspan=4)


def check_cab():
   global root
   root.destroy()
   root =Tk()
   mobile_no=StringVar()
   name=StringVar()
   email=StringVar()
   begin=StringVar()
   to =StringVar()
   fare =StringVar()
   day=StringVar()
   time=StringVar()
   def data_base():
       Mobile_no=mobile_no.get()
       Name=name.get()
       Email=email.get()
       Begin=begin.get()
       To=to.get()
       Fare=fare.get()
       Day=day.get()
       Time=time.get()
       if Mobile_no=="" and Name=="":
           tkinter.messagebox.showinfo("sorry", "enter the full detail")
           return
       if Mobile_no=="":
           tkinter.messagebox.showinfo("sorry", "enter the mobile no")
           return
       if len(Mobile_no)!=10:
           tkinter.messagebox.showinfo("sorry", "invalid mobile no.")
     
       if To=="":
           tkinter.messagebox.showinfo("sorry", "enter the location")
           return
       if Name=="":
           tkinter.messagebox.showinfo("sorry","enter the name")
           return
       tkinter.messagebox.showinfo("success","your booking  is confirmned")
          
           
   Label(root, text='Boking request', width=30, fg="black", font=('arial', 12, 'bold')).grid(row=0, column=0, padx=4,pady=2,columnspan=2)        
   Button(root, text='logout', fg="white", bg="#aa0ee8", bd=1, width=30, font=('arial', 10, 'bold'),command=login_page).grid(row=0,column=5,sticky=W, ipady=4,pady=2,columnspan=2)

   Label(root,text="").grid(row=1,pady=10)
   
   Label(root,text="name*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=2,column=0,sticky=E)
   Entry(root,textvar=name,width=40).grid(row=2,column=1,pady=3,ipady=3,sticky=W)

   Label(root,text="mobile no*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=3,column=0)
   Entry(root,textvar=mobile_no,width=40).grid(row=3,column=1,sticky=W,pady=3,ipady=3)
   
   Label(root,text="From*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=4,column=0)
   Entry(root,textvar=begin,width=40).grid(row=4,column=1,sticky=W,pady=3,ipady=3)
   
   Label(root,text="To*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=5,column=0)
   Entry(root,textvar=to,width=40).grid(row=5,column=1,sticky=W,pady=3,ipady=3)
   
   Label(root,text="Fare*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=6,column=0)
   Entry(root,textvar=fare,width=40,bg="white").grid(row=6,column=1,sticky=W,pady=3,ipady=3)
   Label(root,text="don't fill").grid(row=6,column=2,sticky=W)
   
   Label(root,text="Day*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=7,column=0)
   Entry(root,textvar=day,width=40).grid(row=7,column=1,sticky=W,pady=3,ipady=3)
   
   Label(root,text="Time*",width=20,fg="skyblue",font=('arial',12 , 'bold')).grid(row=9,column=0)
   Entry(root,textvar=time,width=40).grid(row=9,column=1,sticky=W,pady=3,ipady=3)
   
   Button(root, text='Book', fg="white", bg="blue", bd=1, width=30, font=('arial', 10, 'bold'),command=data_base).grid(row=10,column=1,sticky=W, ipady=4,pady=2,columnspan=2)
   
def Register():
   global root
   root.destroy()
   root =Tk()
   reg=StringVar()
   name=StringVar()
   email=StringVar()
   address=StringVar()
   mobile_no=StringVar()
   password=StringVar()

   def database():
    
       Name=name.get()
       Reg=reg.get()
       Address=address.get()
       Mobile_no=mobile_no.get()
       Password=password.get()
       Email=email.get()
       with sqlite3.connect("create_form6.db") as db:
             cursor = db.cursor()
       find_user=("SELECT *  FROM new_form  WHERE  Email=? or Reg=?  ")
       cursor.execute(find_user,[(Email),(Reg)])
       result=cursor.fetchall()
       print(str(result))
       if result:
            tkinter.messagebox.showinfo("sorry", "ENTER FULL DETAIL")
            return
       elif Name=="" :
            tkinter.messagebox.showinfo("sorry", "enter full detail")
            return
       elif Reg=="" :
            tkinter.messagebox.showinfo("sorry", "enter full detail")
            return
       elif Address=="" :
            tkinter.messagebox.showinfo("sorry", "enter full detail")
            return
       elif Mobile_no=="":
            tkinter.messagebox.showinfo("sorry", "enter full detail")
            return
       elif Password=="":
            tkinter.messagebox.showinfo("sorry", "enter full detail \n password have minimum 8 char and use @ ,int ,char ")
            return
       elif Email=="":
           tkinter.messagebox.showinfo("sorry", "enter full detail")
           return
       elif Password.find('@')<0 :
           tkinter.messagebox.showinfo("sorry", "password must contain char, @, int")
           return
       conn=sqlite3.connect("create_form6.db")
       conn.execute("create table if not exists new_form(Name varchar(50),Reg text,Address text,Mobile_no text, Email text,Password text);")
       conn.execute("insert into new_form(Name,Reg,Address,Mobile_no,Email,Password)values(?,?,?,?,?,?)",(Name,Reg,Address,Mobile_no,Email,Password,))
       conn.commit()
       tkinter.messagebox.showinfo("successfully submission", "click login button")
       
    
   Label(root,text="SignUp page",font=('arial',20,'bold')).grid(row=0,column=0,columnspan=2)
   Label(root,text="Registration no.").grid(row=1,column=0)
   Entry(root,textvar=reg).grid(row=1,column=1)
   Label(root,text="name").grid(row=2,column=0)
   Entry(root,textvar=name).grid(row=2,column=1)

   Label(root,text="email").grid(row=3,column=0)
   Entry(root,textvar=email).grid(row=3,column=1)
   Label(root,text="address").grid(row=4,column=0)
   Entry(root,textvar=address).grid(row=4,column=1)
   Label(root,text="mobile no").grid(row=5,column=0)
   Entry(root,textvar=mobile_no).grid(row=5,column=1)
   Label(root,text="password").grid(row=6,column=0)
   Entry(root,textvar=password).grid(row=6,column=1)
   Button(root,text="login page",fg="white",bg="green",font=('arial',10,'bold'),width=20,command=login_page).grid(row=3,column=4,rowspan=2,columnspan=2)
   Button(root,text="submit",fg="white",bg="blue",font=('arial',10,'bold'),width=20,command=database).grid(row=7,column=4,rowspan=2,columnspan=2)
   Button(root,text="Cancel",fg="white",bg="red",font=('arial',10,'bold'),width=20,command=quit).grid(row=7,column=1)



def login_page():
   global root 
   root.destroy() 
   root=Tk()
   password=StringVar()
   reg=StringVar()
   def databse():
       Reg=reg.get()
       Password=password.get()
       with sqlite3.connect("create_form6.db") as db:
             cursor = db.cursor()
       find_user=("SELECT *  FROM new_form  WHERE  Reg=?  ")
       cursor.execute(find_user,[Reg])
       result=cursor.fetchall()
       print(str(result))
       if Reg=="" and Password=="":
            tkinter.messagebox.showinfo("sorry", "enter the full detail")
       elif result:
            check_cab()
       else:
           tkinter.messagebox.showinfo("sorry", "registration no invalid")
           login_page()
           return
   Label(root, text='Log in', width=30, fg="black", font=('arial', 12, 'bold')).grid(row=0, column=0,sticky=W, padx=4,pady=2,columnspan=2)        
   Button(root, text='Register', fg="white", bg="#aa0ee8", bd=1, width=30, font=('arial', 10, 'bold'),command=Register).grid(row=0,column=5,sticky=W, ipady=4,pady=2,columnspan=2)

   Label(root, text=" ", width=20, ).grid(row=1, column=0)
   Label(root, text="user login ", fg="#088", width=20, font=('arial', 20, 'bold')).grid(row=2, column=1, ipady=10)
   Label(root, text="Username ", width=20,fg="darkblue",font=('arial',12 , 'bold') ).grid(row=5, column=0,sticky=S)
   e1 = Entry(root,textvar=reg, width=40)
   Label(root, text="Password ", width=20,fg="darkblue",font=('arial', 12, 'bold') ).grid(row=7,ipadx=10, column=0,sticky=S)
   e2 = Entry(root,textvar=password, width=40)
   
   e1.grid(row=5, column=1, ipady=2, pady=4)
   e2.grid(row=7, column=1, ipady=2, pady=4)
   Button(root, text='login Now', fg="white", bg="red", bd=1, width=5, font=('arial', 10, 'bold'),command=databse).grid(row=10,column=1,ipadx=30, pady=4)
   Button(root, text='Forget password', fg="white", bg="green", bd=1, width=5, font=('arial', 10, 'bold'),command=forget_password).grid(row=10,column=5,ipadx=30, pady=4)
   
login_page()
root.mainloop()
