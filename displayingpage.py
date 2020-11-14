from tkinter import *
from tkinter import messagebox
import sqlite3
class patient_page:
    def  __init__(self,master):
        self.name=StringVar()
        self.address=StringVar()
        self.customerid=StringVar()
        self.age=StringVar()
        self.contactno=StringVar()
        self.problem=StringVar()
        self.master=master
        self.top=Frame(master, width=1300, height=100, bg='#008080')#808000#CD5C5C#008080'#FFA07A
        self.top.pack(side=TOP)

        self.left = Frame(master, width=200, height=590, bg='black')#here left is variable name for frame
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=1100, height=590, bg='#808000')
        self.right.pack(side=RIGHT)
        nameofhosp=Label(self.top,text='E-HEALTH CARE CENTER',font=('Times_New_Roman 30 bold'), fg='black',bg='#808080')
        nameofhosp.place(x=400,y=0)
        nameofhosp=Label(self.right,text='Welcome to E-HEALTH CARE CENTER',font=('Times_New_Roman 30 bold'), fg='black',bg='#808080')
        nameofhosp.place(x=150,y=200)
    #def __init__(self,master):
        remdet=Button(self.left,text='EXIT',height=5,width=27,command=master.destroy,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        remdet.place(x=0,y=510)
        
    def buttonact(self):
        prescription=Button(self.left ,text ='Book_Appointment',height=5,width=27,command=self.entriesforpatient,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        prescription.place(x=0,y=0)
        patients=Button(self.left,text='Show_Patients',height=5,width=27,command=self.displaydatapatient,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        patients.place(x=0,y=85)
        updation=Button(self.left,text='Update',height=5,width=27,command=self.update,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        updation.place(x=0,y=170)

        #after this
        de=Button(self.left,text='Delete',height=5,width=27,command=self.delpatient,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        de.place(x=0,y=255)
        se=Button(self.left,text='Search',height=5,width=27,command=self.search,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        se.place(x=0,y=425)
        #button for message
        msbtt=Button(self.left,text='Message',height=5,width=27,command=self.message,bg='#454545',font=('Times_New_Roman 9 bold'),fg='white')
        msbtt.place(x=0,y=340)
    def entriesforpatient(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        l1=Label(self.right,text='Patient_Id',font=('Times_New_Roman 18 bold'), fg='black')
        l1.place(x=20,y=20)
        self.l11=Entry(self.right,textvariable=self.customerid,width=60)
        self.l11.place(x=200,y=25,height=30)

        l6=Label(self.right,text='Name',font=('Times_New_Roman 18 bold'), fg='black')
        l6.place(x=20,y=80)
        self.l66=Entry(self.right,textvariable=self.name,width=60)
        self.l66.place(x=200,y=80,height=30)
        
        l5=Label(self.right,text='Problem',font=('Times_New_Roman 18 bold'), fg='black')
        l5.place(x=20,y=160)
        self.l55=Entry(self.right,textvariable=self.problem,width=60)#first arguement is telling where to put the info
        self.l55.place(x=200,y=160,height=30)
        
        l2=Label(self.right,text='Age',font=('Times_New_Roman 18 bold'), fg='black')
        l2.place(x=20,y=240)
        self.l22=Entry(self.right,textvariable=self.age,width=60)#first arguement is telling where to put the info
        self.l22.place(x=200,y=240,height=30)

        l3=Label(self.right,text='Contact No.',font=('Times_New_Roman 18 bold'), fg='black')
        l3.place(x=20,y=320)
        self.l33=Entry(self.right,textvariable=self.contactno,width=60)
        self.l33.place(x=200,y=320,height=30)

        l4=Label(self.right,text='Address',font=('Times_New_Roman 18 bold'), fg='black')
        l4.place(x=20,y=400)
        self.l44=Entry(self.right,textvariable=self.address,width=60)
        self.l44.place(x=200,y=400,height=30)

        saving=Button(self.right,text='Save',font=('Times_New_Roman 18 bold'),command=self.adddetails)
        saving.place(x=300,y=500)

#making a funtion for adding to database
    def adddetails(self):
        customerid2=int(self.customerid.get())
        name2=self.name.get()
        
        problem2=self.problem.get()
        age2=int(self.age.get())
        #customerid2=self.customerid.get()
        contactno2=int(self.contactno.get())
        address2=self.address.get()
        l1=[]
        l2=[]
        t1=()
        l1.append(customerid2)
        l1.append(name2)
        
        l1.append(problem2)
        l1.append(age2)
        l1.append(contactno2)
        l1.append(address2)
        t1=tuple(l1)#format is tuple in list for database 
        l2.append(t1)
        print(l2)
        #l1.append(x)
        #l1=[('Hello',)]
        #print(l1)
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        #c.execute('''CREATE TABLE patientinfo1 (customerid  int primary key,name text,problem text,age int,contactno2 number(10),address text)''')
        c.executemany('''INSERT INTO patientinfo1 values(?,?,?,?,?,?)''',l2)
        conn.commit()
        conn.close()
        self.l11.delete(0,END)
        self.l66.delete(0,END)
        self.l22.delete(0,END)
        self.l33.delete(0,END)
        self.l44.delete(0,END)
        self.l55.delete(0,END)
        
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

        #for updation
    

    #part that amritesh has sent for the project

    
    
# new functions   
    def update(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        #conn=sqlite3.connect('hos.db')
        #c=conn.cursor()
        l1=Label(self.right,text="UPDATE THE INFORMATION OF Patient",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l1.place(x=200,y=0)
        l1=Label(self.right,text="Select the information to be updated : ",font=('Times_New_Roman 15 bold'), bg='lightyellow')
        l1.place(x=200,y=50)
        self.v1=StringVar()
        self.id1=IntVar()
        self.updatev=StringVar()
        
        self.updatedv=StringVar()
        self.e1=Entry(self.right,textvariable=self.id1,width=50)
        self.e1.place(x=400,y=150,height=30)
        #self.e1=Entry(self.right,variable=self.updatev)
        #self.e1.pack(x=100,y=200)
        l2=Label(self.right,text="ENTER Patient_ID : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l2.place(x=100,y=150)
        self.e2=Entry(self.right,textvariable=self.updatedv,width=50)
        self.e2.place(x=600,y=300,height=30)
        l3=Label(self.right,text="ENTER Patient NAME/PHONE No.: ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l3.place(x=100,y=300)
        rb1=Radiobutton(self.right,text="NAME   ",font=('Times_New_Roman 15 bold'),variable=self.v1, value="name", bg='lightyellow')
        rb1.place(x=100,y=100)
        rb1=Radiobutton(self.right,text="CONTACT NUMBER : ",font=('Times_New_Roman 15 bold'),variable=self.v1, value="phno", bg='lightyellow')
        rb1.place(x=250,y=100)
        
        upd=Button(self.right,text="Update",command=self.newup,height=5,width=27)
        upd.place(x=100,y=500)
    def newup(self):
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        if self.v1.get()=='name':
            print("good")
            l1=[]
            l1.append(self.updatedv.get())
            l1.append(self.id1.get())
            data=tuple(l1)
            tata = """UPDATE patientinfo1 set name=? where customerid=?"""
            c.execute(tata,data)
            conn.commit()
            conn.close()
        elif self.v1.get()=='phno':
            print('sup')
            l1=[]
            l1.append(int(self.updatedv.get()))
            l1.append(self.id1.get())
            data=tuple(l1)
            tata = """UPDATE patientinfo1 set contactno2=? where customerid=?"""
            c.execute(tata,data)
            conn.commit()
            conn.close()
        messagebox.showinfo("SUCESS","RECORD UPDATED ")
        self.e1.delete(0,END)
        self.e2.delete(0,END)
    def delpatient(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.deld=IntVar()
        l2=Label(self.right,text="ENTER Patient_ID TO BE DELETED : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l2.place(x=100,y=150)
        self.e1=Entry(self.right,textvariable=self.deld,width=50)
        self.e1.place(x=400,y=300,height=30)
        upd=Button(self.right,text="DELETE",command=self.delrec,height=5,width=27)
        upd.place(x=100,y=500)
    def delrec(self):
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        tata='''DELETE from patientinfo1 where customerid=? '''
        l1=[]
        l1.append(self.deld.get())
        data=tuple(l1)
        c.execute(tata,data)
        conn.commit()
        conn.close()
        messagebox.showinfo("SUCESS","RECORD DELETED" )
        self.e1.delete(0,END)
    '''def search(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.deld=IntVar()
        l2=Label(self.right,text="ENTER Patient_ID TO BE SEARCHED : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
        l2.place(x=100,y=150)
        self.e1=Entry(self.right,textvariable=self.deld,width=50)
        self.e1.place(x=400,y=300,height=30)
        upd=Button(self.right,text="SEARCH",command=self.serrec,height=5,width=27)
        upd.place(x=100,y=500)'''
    def search(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        self.deld=StringVar()
        l2=Label(self.right,text="ENTER DOCTOR Specialisation TO BE SEARCHED : ",font=('Times_New_Roman 20 bold'), bg='lightyellow')
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
        id1=str(self.deld.get())
        l1=[]
        l1.append(id1)
        l1=tuple(l1)
        #l2=[]
        #l2.append(l1)
        c.execute('''SELECT * from dod2 where spec=?''',l1)
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
        upd=Button(self.right,text="SEARCH",command=self.link2,height=5,width=27)
        upd.place(x=100,y=500)
    def link2(self):
        self.ptid=StringVar()
        self.doid=StringVar()
        for widget in self.right.winfo_children():
            widget.destroy()
        lb1=Label(self.right,text="Enter patient id: ", bg='lightyellow')
        lb1.place(x=10,y=100)
        self.pat=Entry(self.right,textvariable=self.ptid)
        self.pat.place(x=200,y=100)
        lb1=Label(self.right,text="Enter doctor id: ", bg='lightyellow')
        lb1.place(x=10,y=200)
        self.doc=Entry(self.right,textvariable=self.doid)
        self.doc.place(x=200,y=200)
        print(self.ptid.get())
        self.medc=StringVar()
        self.tests=StringVar()
        #st=int(1)
        #l1=[]
        #l1.append(st)
        #l1.append(st)
        butt=Button(self.right,text="Connect",command=self.upd)
        butt.place(x=100,y=50)
        butt1=Button(self.right,text="View prescription",command=self.seepres)
        butt1.place(x=200,y=50)
    def upd(self):
        l1=[]
        l1.append(int(self.doid.get()))
        l1.append(int(self.ptid.get()))
        l1.append("")
        l1.append("")
        l1.append("")
        t1=tuple(l1)
        l2=[]
        l2.append(t1)
        print(l2)
        #data=tuple(l1)
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        c.executemany('''INSERT INTO docpat values(?,?,?,?,?)''',l2)
        #tata = """UPDATE docpat set dodidv=? where patid=?"""
        #c.execute(tata,data)
        conn.commit()
        messagebox.showinfo("SUCESS","DOCTOR "+ " Connected to patient" )
        conn.close()
    def seepres(self):
        for widget in self.right.winfo_children():
            widget.destroy()
        butt=Button(self.right,text="Confirm",command=self.displaypat)
        butt.place(x=100,y=50)
        l1=Label(self.right,text="Give ID:", bg='lightyellow')
        l1.place(x=10,y=100)
        docid=Entry(self.right,textvariable=self.ptid)
        docid.place(x=100,y=100)
    def displaypat(self):
        for widget in self.right.winfo_children():
            widget.destroy()   
        conn=sqlite3.connect('hos.db')
        c=conn.cursor()
        l1=[]
        l1.append(int(self.ptid.get()))
        data=tuple(l1)
        tata="""SELECT * from docpat where patid=?"""
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
            #l5=Label(self.right,text=record[4],font=('Times_New_Roman 15 bold'), fg='red', bg='orange',width=wid)
            #l5.place(x=700,y=10+pos)
            #l6=Label(self.right,text=record[5],font=('Times_New_Roman 15 bold'), fg='red', bg='brown',width=wid)
            #l6.place(x=900,y=10+pos)
            count=count+1
            pos=pos+40
        #print(c.fetchall())
        #conn.commit()
       # print("********************************",count,"****************************************")
        conn.close()
#messaege function
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
            val=("Patient: "+self.reply.get())
            f=open(self.name,"w")
            print(f.write(val))
        #print(f.write(rangenge(0,10)))
        val=("Patient: "+self.reply.get())
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
root.title('Appointment')
obj1=patient_page(root)
obj1.buttonact()
#obj1.entries()
root.geometry('1300x720+0+0')
root.resizable(False,False)


root.mainloop()


        
