from tkinter import *
import sqlite3
from tkinter import messagebox
import os
class doctor_page:
    #from photo import pic
    def __init__(self,master):
        self.doidv=StringVar()
        self.spe=StringVar()
        self.medicines=StringVar()
        self.tests=StringVar()
        self.master = master
        self.top=Frame(master,width=1300,height=100,bg='lightgreen')
        self.top.pack(side=TOP)
        self.left = Frame(master, width=1300, height=90, bg='lightblue')
        self.left.pack(side=TOP)
        self.right = Frame(master, width=1300, height=520, bg='lightyellow')
        self.right.pack(side=RIGHT)
        head=Label(self.top,text='E-HEALTH CARE CENTER',font=('Times_New_Roman 30 bold'), fg='red', bg='lightgreen')
        head.place(x=400,y=0)

        Welmsg=Label(self.right,text='Welcome to E-HEALTH CARE CENTER',font=('Times_New_Roman 40 bold'), fg='red', bg='lightyellow')
        Welmsg.place(x=90,y=200)
        
        remdet=Button(self.left,text='Click_to_EXIT',height=5,width=65,command=master.destroy,fg='red')
        remdet.place(y=0,x=850)
    def buttonact(self):
        presc=Button(self.left,text='Click_to_message_patient',height=5,width=60,command=self.message,fg='red')
        presc.place(y=0,x=450)
        #addet=Button(self.left,text='Click_to_show_all_doctor',height=5,width=27)#,command=self.showdet)
        #addet.place(y=0,x=85)
        upd=Button(self.left,text='Click_to_Prepare_Report',height=5,width=65,command=self.linkwitdoctor,fg='red')
        upd.place(y=0,x=0)
##########################  Function to link view all requests by patients ######################################
    def linkwitdoctor(self):
        for widget in self.right.winfo_children():
            widget.destroy()   
        '''conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        records=c.fetchall()'''
        #self.displaypat()
        self.ptid=IntVar()
        self.doid=IntVar()
        #self.pat=Entry(self.right,textvariable=self.ptid)
        #self.pat.place(x=100,y=100)
        l1=Label(self.right,text="Enter your ID here:", bg='lightyellow')
        l1.place(x=10,y=100)
        self.docid=Entry(self.right,textvariable=self.doid)
        self.docid.place(x=300,y=100)
        butt=Button(self.right,text="CLICK TO VIEW ALL REQUESTS",command=self.displaypat,width=50)
        butt.place(x=100,y=200,height=50)
#########################        PLAN CHANGE ####################################################
    def link1(self):
        print(self.ptid.get())
        self.stat=0
        l1=[]
        l1.append(self.ptid.get())
        l1.append(self.doid.get())
        l1.append(self.medicines.get())
        l1.append(self.tests.get())
        #l1.append(self.stat)
        l1=tuple(l1)
        l2=[]
        l2.append(l1)
        print(l2)
       
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        c.execute('''DROP TABLE docpat''')
        c.execute('''CREATE TABLE docpat (dodidv int ,patid int,medicines text,tests text)''')
        c.executemany('''INSERT INTO docpat values(?,?,?,?,?)''',l2)
        conn.commit()
        messagebox.showinfo("SUCESS","DOCTOR "+ " Connected to patient" )
        conn.close()
######################### THIS IS THE INTER FACE WHERE THE DOCTOR PREPARES PRESCRIPTION FOR THE PATIENT ###################################################
    def link2(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        lb1=Label(self.right,text="Enter patient id: ", bg='lightyellow')
        lb1.place(x=10,y=100)
        self.pat=Entry(self.right,textvariable=self.ptid)
        self.pat.place(x=200,y=100)
        print(self.ptid.get())
        self.medc=StringVar()
        self.tests=StringVar()
        #st=int(1)
        #l1=[]
        l1=Label(self.right,text="Enter Medicine", bg='lightyellow')
        l1.place(x=100,y=150)
        self.med=Entry(self.right,textvariable=self.medc,width=100)
        self.med.place(x=100,y=200,height=100)
        #l1.append(st)
        l1=Label(self.right,text="Enter Tests to be performed", bg='lightyellow')
        l1.place(x=100,y=310)
        self.tes=Entry(self.right,textvariable=self.tests,width=100)
        self.tes.place(x=100,y=350,height=100)
        #l1.append(st)
        butt=Button(self.right,text="Click to generate report",command=self.upd)
        butt.place(x=100,y=50)
#######################  MEDICINES AND TESTS HAVE BEEN ADDED TO THE DATABASE ########################33
    def upd(self):
        l1=[]
        l1.append(self.medc.get())
        l1.append(self.ptid.get())
        data=tuple(l1)
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        tata = """UPDATE docpat set medicines=? where patid=?"""
        c.execute(tata,data)
        conn.commit()
        l1=[]
        l1.append(self.tests.get())
        l1.append(self.ptid.get())
        data=tuple(l1)
        tata = """UPDATE docpat set tests=? where patid=?"""
        c.execute(tata,data)
        conn.commit()
        messagebox.showinfo("SUCESS","DOCTOR "+ " Connected to patient" )
        conn.close()
##########################  THIS FUNCTION DISPLAYS ALL PATIENTS WHO HAVE MADE REQUEST TO THE DOCTOR  
    def displaypat(self):
        for widget in self.right.winfo_children():
            widget.destroy()   
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        l1=[]
        l1.append(self.doid.get())
        data=tuple(l1)
        tata="""SELECT * from docpat where dodidv=?"""
        c.execute(tata,data)
        records=c.fetchall()
        print(records)
        pos=0
        wid=15
        l1=Label(self.right,text='doid',font=('Times_New_Roman 15 bold'), fg='red', bg='blue',width=10)
        l1.place(x=0,y=10+pos)
            #t1=Text(self.right,=p_rec)
            #t1.pack()
        l2=Label(self.right,text='patid',font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
        l2.place(x=100,y=10+pos)
        l3=Label(self.right,text='medicines',font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid+20)
        l3.place(x=300,y=10+pos)
        l4=Label(self.right,text='tests',font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid+20)
        l4.place(x=800,y=10+pos)
        #l5=Label(self.right,text='status',font=('Times_New_Roman 15 bold'), fg='red', bg='orange',width=wid)
        #l5.place(x=700,y=10+pos)
        #l6=Label(self.right,text='status',font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
        #l6.place(x=900,y=10+pos)
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
            l2=Label(self.right,text=record[1],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid)
            l2.place(x=100,y=10+pos)
            l3=Label(self.right,text=record[2],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid+20)
            l3.place(x=300,y=10+pos)
            l4=Label(self.right,text=record[3],font=('Times_New_Roman 15 bold'), fg='red', bg='lightyellow',width=wid+20)
            l4.place(x=800,y=10+pos)
            count=count+1
            pos=pos+40
        conn.close()
        butt=Button(self.right,text="Click here to generate report",command=self.link2,width=50)
        butt.place(x=900,y=450,height=70)
###################### DOCOTR CAN COMMUNICATE WITH PATIENT  ###############################
    def message(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.reply=StringVar()
        rep=Entry(self.right,textvariable=self.reply,width=100)
        rep.place(x=500,y=150,height=100)
        self.lb2=Label(self.right,text='Enter your reply: ', bg='lightyellow')
        self.lb2.place(x=500,y=100)
        self.lb1=Label(self.right,text='', bg='lightyellow')
        self.lb1.place(x=500,y=300)
        send=Button(self.right,text="send",command=self.writefile)
        send.place(x=10,y=300)
        self.dno=StringVar()
        self.pno=IntVar()
        self.lb2=Label(self.right,text='Enter doctor name: ', bg='lightyellow')
        self.lb2.place(x=0,y=100)
        dname=Entry(self.right,textvariable=self.dno)
        dname.place(x=200,y=100)
        self.lb3=Label(self.right,text='Enter patient id: ', bg='lightyellow')
        self.lb3.place(x=0,y=200)
        pname=Entry(self.right,textvariable=self.pno)
        pname.place(x=200,y=200)
        send=Button(self.right,text="End conversation",command=self.endc)
        send.place(x=100,y=300)
        rec=Button(self.right,text="Recieve reply",command=self.read)
        rec.place(x=300,y=300)
    def writefile(self):
        #for widget in self.right.winfo_children():
         #   widget.destroy()
        self.name=str(self.dno.get())+str(self.pno.get())+".txt"
        print(self.name)
        try:
            f=open(self.name,"r")
            val=f.read()
            self.pos=0
            self.lb1.config(text=val)
            f.close
        except FileNotFoundError:
            val=("doctor: "+self.reply.get())
            f=open(self.name,"w")
            print(f.write(val))
        #print(f.write(rangenge(0,10)))
        val=("doctor: "+self.reply.get())
        f=open(self.name,"w")
        print(f.write(val))
        f.close()
        f=open(self.name,"r")
        val=f.read()
        self.pos=0
        self.lb1.config(text=val)
        f.close
    def read(self):
        f=open(self.name,"r")
        val=f.read()
        self.pos=0
        self.lb1.config(text=val)
        f.close
    def endc(self):
        os.remove(self.name) 
root=Tk()
root.geometry('1300x720+0+0')
root.resizable(False,False)
root.title('Doctor Interface')
#presc=Button(root,text='click_to_message_patient',height=5,width=65,command=showimg)
#presc.pack()
ob1=doctor_page(root)
ob1.buttonact()
#ob1.display()

root.mainloop()
