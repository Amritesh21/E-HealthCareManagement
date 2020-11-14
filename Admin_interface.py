from tkinter import *
import sqlite3
from tkinter import messagebox
#pythonCopyimport tkinter as tk
class doctor_page:
    def __init__(self,master):
        self.name=StringVar()
        self.age=StringVar()
        self.addr=StringVar()
        self.phno=StringVar()
        self.doidv=StringVar()
        self.spe=StringVar()
        self.master = master
        self.passwd=StringVar()
        self.top=Frame(master,width=1500,height=100,bg='lightgreen')
        self.top.pack(side=TOP)
        self.left = Frame(master, width=200, height=600, bg='lightblue')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=1300, height=600, bg='lightyellow')
        self.right.pack(side=RIGHT)
        head=Label(self.top,text='E-HEALTH CARE CENTER',font=('Times_New_Roman 30 bold'), fg='red', bg='lightgreen')
        head.place(x=400,y=0)
        
        
        Welmsg=Label(self.right,text='WELCOME TO E-HEALTH CARE CENTER',font=('Times_New_Roman 40 bold'), fg='red', bg='lightyellow')
        Welmsg.place(x=90,y=300)
        self.c=Canvas(self.right,height=250,width=500, bg='lightyellow')
        self.c.place(x=350,y=0)
        self.photo=PhotoImage(master=self.c,file='ehealthcare.gif')
        self.c.create_image(250,150,image=self.photo)
        
        
        remdet=Button(self.left,text='Click_to_EXIT',height=5,width=27,command=master.destroy,activebackground='red')
        remdet.place(x=0,y=510)
    def buttonact(self):
        presc=Button(self.left,text='Click_to_add_doctor',height=5,width=27,command=self.display,activebackground='aqua')
        presc.place(x=0,y=0)
        addet=Button(self.left,text='Click_to_show_all_doctor',height=5,width=27,command=self.showdet,activebackground='aqua')
        addet.place(x=0,y=85)
        upd=Button(self.left,text='Click_to_Update',height=5,width=27,command=self.updat,activebackground='aqua')
        upd.place(x=0,y=255)
        de=Button(self.left,text='Click_to_Delete',height=5,width=27,command=self.deldoc,activebackground='aqua')
        de.place(x=0,y=170)
        se=Button(self.left,text='Click_to_Search_doctor',height=5,width=27,command=self.ser,activebackground='aqua')
        se.place(x=0,y=340)
        pt=Button(self.left,text='Click_to_Show_all_Patients ',height=5,width=27,command=self.displaydatapatient,activebackground='aqua')
        pt.place(x=0,y=425)
###################################### FUNCTIONS TO ADD DOCOTOR ##########################################################
    def display(self):
        #self.right.pack_forget()
        #self.right.grid_forget()
        for widget in self.right.winfo_children():
            widget.destroy()
        self.c=Canvas(self.right,height=400,width=500)
        self.c.place(x=700,y=0)
        self.photo=PhotoImage(master=self.c,file='doctor.gif')
        self.c.create_image(250,150,image=self.photo)

        
        l1=Label(self.right,text="Doctor's Name",font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l1.place(x=0,y=10)
        self.name1=Entry(self.right,textvariable=self.name,width=50)
        self.name1.place(x=250,y=10,height=30)
        
        l2=Label(self.right,text='Experience',font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l2.place(x=0,y=70)
        self.age=Entry(self.right,textvariable=self.age,width=50)
        self.age.place(x=250,y=70,height=30)
        l2=Label(self.right,text='years',font=('Times_New_Roman 10 bold'), fg='red', bg='lightyellow')
        l2.place(x=570,y=70)
        
        l3=Label(self.right,text='Contact Number',font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l3.place(x=0,y=130)
        self.phno=Entry(self.right,textvariable=self.phno,width=50)
        self.phno.place(x=250,y=130,height=30)

        l4=Label(self.right,text='Specilization',font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l4.place(x=0,y=190)
        self.spec=Entry(self.right,textvariable=self.spe,width=50)
        self.spec.place(x=250,y=190,height=30)

        
        l5=Label(self.right,text='Doctor id',font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l5.place(x=0,y=240)
        self.doid=Entry(self.right,textvariable=self.doidv,width=50)
        self.doid.place(x=250,y=240,height=30)
        
        l5=Label(self.right,text='Address',font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l5.place(x=0,y=300)
        self.ad=Entry(self.right,textvariable=self.addr,width=50)
        self.ad.place(x=250,y=300,height=30)

        l6=Label(self.right,text='Password',font=('Times_New_Roman 20 bold'), fg='red', bg='lightyellow')
        l6.place(x=0,y=360)
        self.pas=Entry(self.right,show="*",textvariable=self.passwd,width=50)
        self.pas.place(x=250,y=360,height=30)
        
        save=Button(self.right,text="Save",height=3,width=27,bg='red',command=self.addet)
        save.place(x=170,y=400)
    def addet(self):
        name2=self.name.get()
        addr2=self.addr.get()
        phno2=self.phno.get()
        doidv2=self.doidv.get()
        age2=self.age.get()
        spe2=self.spe.get()
        try:
            phno=int(phno2)
            doidv2=int(doidv2)
            age=int(age2)
        except ValueError:
            phno=''
            doidv2=''
            age=''
            messagebox.showinfo("ERROR","PLEASE FILL ALL ENTRIES CORRECTLY")
            return
            
        l1=[]
        l2=[]
        t1=()
        #print("*****************************",len(l2[0]))
        l1.append(doidv2)
        l1.append(name2)
        l1.append(addr2)
        l1.append(phno2)
        l1.append(age2)
        l1.append(spe2)
        l1.append(self.passwd.get())
        t1=tuple(l1)
        l2.append(t1)
        print(l2)
        #l1.append(x)
        #l1=[('Hello',)]
        #print(l1)
        print("*****************************",len(l2))
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        #c.execute('''ALTER TABLE dod2 ADD PASSWORD TEXT''')
        #c.execute('''CREATE TABLE dod2 (dodidv int primary key,name text,addr text,phno int,age int, spec text)''')
        c.executemany('''INSERT INTO dod2 values(?,?,?,?,?,?,?)''',l2)
        conn.commit()
        messagebox.showinfo("SUCESS","DOCTOR "+ name2+ " HAS JOINED OUR HOSPITAL" )
        conn.close()
        self.name1.delete(0,END)
        self.phno.delete(0,END)
        self.doid.delete(0,END)
        self.spec.delete(0,END)
        self.age.delete(0,END)
        self.ad.delete(0,END)
        self.pas.delete(0,END)
########################  DISPLAY ALL DOCTORS  ##############################################################################
    def showdet(self):
        for widget in self.right.winfo_children():
            widget.destroy()   
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        c.execute('''SELECT * from dod2''')
        records=c.fetchall()#ROW FETCHED AS TUPLE AND TABLE AS LIST
        print(records)
        pos=0
        wid=15
        l1=Label(self.right,text='ID',font=('Times_New_Roman 15 bold'), fg='red', bg='blue',width=10)
        l1.place(x=0,y=10+pos)
            #t1=Text(self.right,=p_rec)
            #t1.pack()
        l2=Label(self.right,text='NAME',font=('Times_New_Roman 15 bold'), fg='red', bg='pink',width=wid)
        l2.place(x=100,y=10+pos)
        l3=Label(self.right,text='ADDRESS',font=('Times_New_Roman 15 bold'), fg='red', bg='green',width=wid)
        l3.place(x=300,y=10+pos)
        l4=Label(self.right,text='PHNO',font=('Times_New_Roman 15 bold'), fg='red', bg='grey',width=wid)
        l4.place(x=500,y=10+pos)
        l5=Label(self.right,text='EXPERIENCE',font=('Times_New_Roman 15 bold'), fg='red', bg='orange',width=wid)
        l5.place(x=700,y=10+pos)
        l6=Label(self.right,text='SPECIL',font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
        l6.place(x=900,y=10+pos)
        l7=Label(self.right,text='PASSWORD',font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
        l7.place(x=1100,y=10+pos)
        count=0
        pos=40
        wid=15
        for record in records:
            #p_rec=''
            #p_rec += str(record[0])+"  "+ str(record[1])+"  "+ str(record[2])+"  "+ str(record[3])+"  "+ str(record[4])+"  "+ str(record[5])+"\n" 
            l1=Label(self.right,text=record[0],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=10)
            l1.place(x=0,y=10+pos)
            #t1=Text(self.right,=p_rec)
            #t1.pack()
            l2=Label(self.right,text=record[1],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l2.place(x=100,y=10+pos)
            l3=Label(self.right,text=record[2],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l3.place(x=300,y=10+pos)
            l4=Label(self.right,text=record[3],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l4.place(x=500,y=10+pos)
            l5=Label(self.right,text=record[4],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l5.place(x=700,y=10+pos)
            l6=Label(self.right,text=record[5],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l6.place(x=900,y=10+pos)
            l7=Label(self.right,text=record[6],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l7.place(x=1100,y=10+pos)
            count=count+1
            pos=pos+40
        #print(c.fetchall())
        #conn.commit()
       # print("********************************",count,"****************************************")
        conn.close()
        #scroll=Scrollbar(self.right)
        #scroll.pack(side=RIGHT)
        
##################################### UPDATING RECORD  ##############################################################
    def updat(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        l1=Label(self.right,text="UPDATE THE INFORMATION OF DOCTOR",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l1.place(x=200,y=0)
        l1=Label(self.right,text="Select the information to be updated : ",font=('Times_New_Roman 15 bold'), bg='lightyellow')
        l1.place(x=200,y=50)
        #self.v1=StringVar()
        self.v1=IntVar()
        #self.v1=''
        self.id1=IntVar()
        self.updatev=StringVar()
        self.updatedv=StringVar()
        self.e1=Entry(self.right,textvariable=self.id1,width=50)
        self.e1.place(x=400,y=150,height=30)
        #self.e1=Entry(self.right,variable=self.updatev)
        #self.e1.pack(x=100,y=200)
        l2=Label(self.right,text="ENTER DOCTOR ID : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l2.place(x=100,y=150)
        self.e2=Entry(self.right,textvariable=self.updatedv,width=50)
        self.e2.place(x=750,y=300,height=30)
        l3=Label(self.right,text="ENTER DOCTOR ADDRESS/PHONE No.: ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l3.place(x=100,y=300)
        rb1=Radiobutton(self.right,text="Address  ",font=('Times_New_Roman 15 bold'),variable=self.v1, value=1, bg='lightyellow')
        rb1.place(x=100,y=100)
        rb2=Radiobutton(self.right,text="CONTACT NUMBER : ",font=('Times_New_Roman 15 bold'),variable=self.v1, value=2, bg='lightyellow')
        rb2.place(x=250,y=100)
        rb2=Radiobutton(self.right,text="PASSWORD : ",font=('Times_New_Roman 15 bold'),variable=self.v1, value=3, bg='lightyellow')
        rb2.place(x=500,y=100)
        upd=Button(self.right,text="Update",command=self.newup,height=5,width=27)
        upd.place(x=100,y=500)
    def newup(self):
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        #l.config(text=self.v1)
        if self.v1.get()==1:
            print("good")
            l1=[]
            l1.append(self.updatedv.get())
            l1.append(self.id1.get())
            data=tuple(l1)
            tata = """UPDATE dod2 set addr=? where dodidv=?"""
            c.execute(tata,data)
            conn.commit()
            conn.close()
        elif self.v1.get()==2:
            print('sup')
            l1=[]
            l1.append(int(self.updatedv.get()))
            l1.append(self.id1.get())
            data=tuple(l1)
            tata = """UPDATE dod2 set phno=? where dodidv=?"""
            c.execute(tata,data)
            conn.commit()
            conn.close()
        elif self.v1.get()==3:
            print('sup')
            l1=[]
            l1.append(self.updatedv.get())
            l1.append(self.id1.get())
            data=tuple(l1)
            tata = """UPDATE dod2 set password=? where dodidv=?"""
            c.execute(tata,data)
            conn.commit()
            conn.close()
        messagebox.showinfo("SUCESS","RECORD UPDATED ")
        self.e1.delete(0,END)
        self.e2.delete(0,END)
######################################   DELETING RECORD   ################################################
    def deldoc(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.deld=IntVar()
        l2=Label(self.right,text="ENTER DOCTOR ID TO BE DELETED : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l2.place(x=100,y=150)
        self.e1=Entry(self.right,textvariable=self.deld,width=50)
        self.e1.place(x=400,y=300,height=30)
        upd=Button(self.right,text="DELETE",command=self.delrec,height=5,width=27)
        upd.place(x=100,y=500)
    def delrec(self):
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        tata='''DELETE from dod2 where dodidv=? '''
        l1=[]
        l1.append(self.deld.get())
        data=tuple(l1)
        c.execute(tata,data)
        conn.commit()
        conn.close()
        messagebox.showinfo("SUCESS","RECORD DELETED" )
        self.e1.delete(0,END)
######################################       SEARCHING RECORD      ##############################################
    def ser(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.deld=IntVar()
        l2=Label(self.right,text="ENTER DOCTOR ID TO BE SEARCHED : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l2.place(x=100,y=150)
        self.e1=Entry(self.right,textvariable=self.deld,width=50)
        self.e1.place(x=400,y=300,height=30)
        upd=Button(self.right,text="SEARCH",command=self.serrec,height=5,width=27)
        upd.place(x=100,y=500)
    def serrec(self):
        for widget in self.right.winfo_children():
            widget.destroy()   
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        id1=int(self.deld.get())
        l1=[]
        l1.append(id1)
        l1=tuple(l1)
        #l2=[]
        #l2.append(l1)
        c.execute('''SELECT * from dod2 where dodidv=?''',l1)
        records=c.fetchall()
        print(records)
        pos=0
        wid=15
        l1=Label(self.right,text='ID',font=('Times_New_Roman 15 bold'), fg='red', bg='blue',width=10)
        l1.place(x=0,y=10+pos)
            #t1=Text(self.right,=p_rec)
            #t1.pack()
        l2=Label(self.right,text='NAME',font=('Times_New_Roman 15 bold'), fg='red', bg='pink',width=wid)
        l2.place(x=100,y=10+pos)
        l3=Label(self.right,text='ADDRESS',font=('Times_New_Roman 15 bold'), fg='red', bg='green',width=wid)
        l3.place(x=300,y=10+pos)
        l4=Label(self.right,text='PHNO',font=('Times_New_Roman 15 bold'), fg='red', bg='grey',width=wid)
        l4.place(x=500,y=10+pos)
        l5=Label(self.right,text='EXPERIENCE',font=('Times_New_Roman 15 bold'), fg='red', bg='orange',width=wid)
        l5.place(x=700,y=10+pos)
        l6=Label(self.right,text='SPECIL',font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
        l6.place(x=900,y=10+pos)
        l7=Label(self.right,text='PASSWORD',font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
        l7.place(x=1100,y=10+pos)
        count=0
        pos=40
        wid=15
        for record in records:
            #p_rec=''
            #p_rec += str(record[0])+"  "+ str(record[1])+"  "+ str(record[2])+"  "+ str(record[3])+"  "+ str(record[4])+"  "+ str(record[5])+"\n" 
            l1=Label(self.right,text=record[0],font=('Times_New_Roman 15 bold'), fg='red', bg='blue',width=10)
            l1.place(x=0,y=10+pos)
            #t1=Text(self.right,=p_rec)
            #t1.pack()
            l2=Label(self.right,text=record[1],font=('Times_New_Roman 15 bold'), fg='red', bg='pink',width=wid)
            l2.place(x=100,y=10+pos)
            l3=Label(self.right,text=record[2],font=('Times_New_Roman 15 bold'), fg='red', bg='green',width=wid)
            l3.place(x=300,y=10+pos)
            l4=Label(self.right,text=record[3],font=('Times_New_Roman 15 bold'), fg='red', bg='grey',width=wid)
            l4.place(x=500,y=10+pos)
            l5=Label(self.right,text=record[4],font=('Times_New_Roman 15 bold'), fg='red', bg='orange',width=wid)
            l5.place(x=700,y=10+pos)
            l6=Label(self.right,text=record[5],font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
            l6.place(x=900,y=10+pos)
            l7=Label(self.right,text=record[6],font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
            l7.place(x=1100,y=10+pos)
            count=count+1
            pos=pos+40
        #print(c.fetchall())
        #conn.commit()
       # print("********************************",count,"****************************************")
        conn.close()
        upd=Button(self.right,text="SEARCH",command=self.ser,height=5,width=27)
        upd.place(x=100,y=500)
##################       DISPLAYING PATIENTS RECORDS   ########################################################
    def displaydatapatient(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        c.execute('''SELECT * from patientinfo1''')
        records=c.fetchall()
        print(records)
        pos=0
        wid=15
        
        l1=Label(self.right,text='Patient_Id',font=('Times_New_Roman 15 bold'), fg='black',width=11)
        l1.place(x=0,y=10+pos)
        l2=Label(self.right,text='Name',font=('Times_New_Roman 15 bold'), fg='black',width=13)
        l2.place(x=120,y=10+pos)
        l3=Label(self.right,text='Problem',font=('Times_New_Roman 15 bold'), fg='black',width=wid)
        l3.place(x=300,y=10+pos)
        l4=Label(self.right,text='Age',font=('Times_New_Roman 15 bold'), fg='black',width=wid)
        l4.place(x=500,y=10+pos)
        l5=Label(self.right,text='Contact No.',font=('Times_New_Roman 15 bold'), fg='black',width=wid)
        l5.place(x=700,y=10+pos)
        l6=Label(self.right,text='Address',font=('Times_New_Roman 15 bold'), fg='black',width=wid)
        l6.place(x=900,y=10+pos)

        pos=40
        wid=15
        for record in records:
            l1=Label(self.right,text=record[0],font=('Times_New_Roman 15 bold'), fg='black',width=10)
            l1.place(x=0,y=10+pos)
            l2=Label(self.right,text=record[1],font=('Times_New_Roman 15 bold'), fg='black',width=wid)
            l2.place(x=100,y=10+pos)
            l3=Label(self.right,text=record[2],font=('Times_New_Roman 15 bold'), fg='black',width=wid)
            l3.place(x=300,y=10+pos)
            l4=Label(self.right,text=record[3],font=('Times_New_Roman 15 bold'), fg='black',width=wid)
            l4.place(x=500,y=10+pos)
            l5=Label(self.right,text=record[4],font=('Times_New_Roman 15 bold'), fg='black',width=wid)
            l5.place(x=700,y=10+pos)
            l6=Label(self.right,text=record[5],font=('Times_New_Roman 15 bold'), fg='black',width=wid)
            l6.place(x=900,y=10+pos)
            pos=pos+40
        conn.close()

root=Tk()
root.geometry('1500x700+0+0')
root.resizable(False,False)
root.title('Admin Interface')
ob1=doctor_page(root)
ob1.buttonact()
#ob1.display()
root.mainloop()
