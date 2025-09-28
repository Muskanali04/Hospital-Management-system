from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root 
        self.root.title('Hospital Management System')
        self.root.geometry('1540x800+0+0')

        #====================VARIABLES====================
        self.Nameoftablet = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NoofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.Storage = StringVar()
        self.DrivingUsingmachine = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientId = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAdress = StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text= 'HOSPITAL MANAGEMENT SYSTEM',fg='red',bg='white',font=('times new roman',50,'bold'))
        lbltitle.pack(side=TOP,fill=X)

            #=================DATA FRAME===================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text='Patient Information',font=('times new roman',12,'bold'))
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,text='Prescription',font=('times new roman',12,'bold'))
        DataFrameRight.place(x=990,y=5,width=480,height=350)

            #=================BUTTON FRAME===================
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

            #=================DETAIL FRAME===================
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #=================DATA FRAME LEFT===================
        lblNameTablet = Label(DataframeLeft,text='Names of tablet',font=('arial',12,'bold'),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablet ,font=('arial',10,'bold'),width=33)
        comNametablet['values']= ('Nice','Corona Vaccine','Acetaminophen','Ibuprofen','Paracetamol','Amoxicillin','Ciprofloxacin','Azithromycin','Metformin','Omeprazole')
        comNametablet.grid(row=0,column=1)

        reflabel = Label(DataframeLeft,text='Reference Number',font=('arial',12,'bold'),padx=2)
        reflabel.grid(row=1,column=0,sticky=W)
        txtref = Entry (DataframeLeft,textvariable=self.Ref,font=('arial',10,'bold'),width=35)
        txtref.grid(row=1,column=1)

        doselabel = Label(DataframeLeft,text='Dose',font=('arial',12,'bold'),padx=2,pady=4)
        doselabel.grid(row=2,column=0,sticky=W)
        txtdose = Entry(DataframeLeft,textvariable=self.Dose,font=('arial',10,'bold'),width=35)
        txtdose.grid(row=2,column=1)

        lblNoofTablets = Label(DataframeLeft,font=('arial',12,'bold'),text='No of Tablets',padx=2,pady=6)
        lblNoofTablets.grid(row=3,column=0,sticky=W)
        txtNOofTablets = Entry(DataframeLeft,textvariable=self.NoofTablets,font=('arial',10,'bold'),width=35)
        txtNOofTablets.grid(row=3,column=1)

        lbllot = Label(DataframeLeft,text='Lot: ',font=('arial',12,'bold'),padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot = Entry(DataframeLeft,textvariable=self.Lot,font=('arial',10,'bold'),width=35)
        txtlot.grid(row=4,column=1)

        lblissuedate = Label(DataframeLeft,text='Issue Date',font=('arial',12,'bold'),padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate = Entry(DataframeLeft,textvariable=self.IssueDate,font=('arial',10,'bold'),width=35)
        txtissuedate.grid(row=5,column=1)

        lblExpirydate = Label(DataframeLeft,text='Expiry Date',font=('arial',12,'bold'),padx=2,pady=6)
        lblExpirydate.grid(row=6,column=0,sticky=W)
        txtExpirydate = Entry(DataframeLeft,textvariable=self.ExpDate,font=('arial',10,'bold'),width=35)
        txtExpirydate.grid(row=6,column=1)

        lblDailyDose = Label(DataframeLeft,text='Daily Dose',font=('arial',12,'bold'),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtdailDose = Entry(DataframeLeft,textvariable=self.DailyDose,font=('arial',10,'bold'),width=35)
        txtdailDose.grid(row=7,column=1)

        lblSideeffect = Label(DataframeLeft,text='Side Effect',font=('arial',12,'bold'),padx=2,pady=6)
        lblSideeffect.grid(row=8,column=0,sticky=W)
        txtSiideEffect = Entry(DataframeLeft,textvariable=self.SideEffect,font=('arial',10,'bold'),width=35)
        txtSiideEffect.grid(row=8,column=1)

        lblFurtherinfo = Label(DataframeLeft,text='Further Information',font=('arial',12,'bold'),padx=2,pady=6)
        lblFurtherinfo.grid(row=0 ,column=2,sticky=W)
        txtFurtherInfo = Entry(DataframeLeft,textvariable=self.FurtherInfo,font=('arial',10,'bold'),width=50)
        txtFurtherInfo.grid(row=0,column=3)

        lblDrvingMachine = Label(DataframeLeft,text='Blood Pressure',font=('arial',12,'bold'),padx=2,pady=6)
        lblDrvingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine =Entry(DataframeLeft,textvariable=self.DrivingUsingmachine,font=('arial',10,'bold'),width=50)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage = Label(DataframeLeft,text='Storage Advice',font=('arial',12,'bold'),padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataframeLeft,textvariable=self.Storage,font=('arial',10,'bold'),width=50)
        txtStorage.grid(row=2,column=3)

        lblMedicine = Label(DataframeLeft,text='Medication',font=('arial',12,'bold'),padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataframeLeft,textvariable=self.HowtoUseMedication,font=('arial',10,'bold'),width=50)
        txtMedicine.grid(row=3,column=3)

        lblPatientId= Label(DataframeLeft,text='Patient Id',font=('arial',12,'bold'),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId= Entry(DataframeLeft,textvariable=self.PatientId,font=('arial',10,'bold'),width=50)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber = Label(DataframeLeft,text='NHS Number',font=('arial',12,'bold'),padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataframeLeft,textvariable=self.NhsNumber,font=('arial',10,'bold'),width=50)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName= Label(DataframeLeft,text='Patient Name',font=('arial',12,'bold'),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientname = Entry(DataframeLeft,textvariable=self.PatientName,font=('arial',10,'bold'),width=50)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth = Label(DataframeLeft,text='Date of Birth',font=('arial',12,'bold'),padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth = Entry(DataframeLeft,textvariable=self.DateOfBirth,font=('arial',10,'bold'),width=50)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAdress = Label(DataframeLeft,text='Patient Adress',font=('arial',12,'bold'),padx=2,pady=6)
        lblPatientAdress.grid(row=8,column=2,sticky=W)
        txtPatientAdress = Entry(DataframeLeft,textvariable=self.PatientAdress,font=('arial',10,'bold'),width=50)
        txtPatientAdress.grid(row=8,column=3)

        #=================DATA FRAME RIGHT===================
        self.txtPrescription = Text(DataFrameRight,font=('arial',10,'bold'),width=60,height=19,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #=================BUTTONS===================
        btnPrescription = Button(Buttonframe,text='Prescription',bg='green',fg='white',font=('arial',12,'bold'),width=23,padx=2,pady=6,command=self.iprescription)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe,text='Prescription Data',bg='green',fg='white',font=('arial',12,'bold'),width=23,padx=2,pady=6,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate = Button(Buttonframe,text='Update',bg='green',fg='white',font=('arial',12,'bold'),width=23,padx=2,pady=6,command=self.update)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(Buttonframe,text='Delete',bg='green',fg='white',font=('arial',12,'bold'),width=23,padx=2,pady=6,command=self.iDelete)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(Buttonframe,text='Clear',bg='green',fg='white',font=('arial',12,'bold'),width=23,padx=2,pady=6,command=self.clear)
        btnClear.grid(row=0,column=4)

        btnExit = Button(Buttonframe,text='Exit',bg='green',fg='white',font=('arial',12,'bold'),width=23,padx=2,pady=6,command=self.iExit)
        btnExit.grid(row=0,column=5)

        #-----------------TABLE-------------------------
        #=================sCROLL BAR===================
        scroll_x =ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe,column=('nametablet','ref','dose','nooftablets','lot','issuedate','expdate','dailydose','storage','nhsnumber','pname','dob','adress'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading('nametablet',text='Names of Tablet')
        self.hospital_table.heading('ref',text='Reference No.')
        self.hospital_table.heading('dose',text='Dose')
        self.hospital_table.heading('nooftablets',text='No of Tablets')
        self.hospital_table.heading('lot',text='Lot')
        self.hospital_table.heading('issuedate',text='Issue Date')
        self.hospital_table.heading('expdate',text='Exp Date')
        self.hospital_table.heading('dailydose',text='Daily Dose')
        self.hospital_table.heading('storage',text='Storage')
        self.hospital_table.heading('nhsnumber',text='NHS Number')
        self.hospital_table.heading('pname',text='Patient Name')
        self.hospital_table.heading('dob',text='DOB')
        self.hospital_table.heading('adress',text='Address')

        self.hospital_table['show']='headings'

        self.hospital_table.column('nametablet',width=100)
        self.hospital_table.column('ref',width=100)
        self.hospital_table.column('dose',width=100)
        self.hospital_table.column('nooftablets',width=100)
        self.hospital_table.column('lot',width=100)
        self.hospital_table.column('issuedate',width=100)
        self.hospital_table.column('expdate',width=100)
        self.hospital_table.column('dailydose',width=100)
        self.hospital_table.column('storage',width=100)
        self.hospital_table.column('nhsnumber',width=100)
        self.hospital_table.column('pname',width=100)
        self.hospital_table.column('dob',width=100)
        self.hospital_table.column('adress',width=100)


        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind('<ButtonRelease-1>',self.get_cursor)


        self.fetch_data()


    #=================Functionality declaration===================
    def iPrescriptionData(self):
        if self.Nameoftablet.get()== '' or self.Ref.get()=='':
            messagebox.showerror('Error' ,'All fields are required')
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='Test123',database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute('insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.Nameoftablet.get(),
                                                                                                     self.Ref.get(),
                              self.Dose.get(),
                              self.NoofTablets.get(),
                              self.Lot.get(),
                              self.IssueDate.get(),
                              self.ExpDate.get(),
                              self.DailyDose.get(),
                              self.Storage.get(),
                              self.NhsNumber.get(),
                              self.PatientName.get(),
                              self.DateOfBirth.get(),
                              self.PatientAdress.get()
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Success', 'Record inserted successfully')

    def update(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Test123',database='mydata')
        my_cursor= conn.cursor()
        my_cursor.execute('update hospital set Name_of_Tablet=%s,dose=%s,numberoftablet=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,stoarge=%s,nhsnumber=%s,patientname=%s,dob=%s,adress=%s where refrenceno=%s',(
                                                                                                    self.Nameoftablet.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NoofTablets.get(),
                              self.Lot.get(),
                              self.IssueDate.get(),
                              self.ExpDate.get(),
                              self.DailyDose.get(),
                              self.Storage.get(),
                              self.NhsNumber.get(),
                              self.PatientName.get(),
                              self.DateOfBirth.get(),
                              self.PatientAdress.get(),
                              self.Ref.get(),
        
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo('Success', 'Data has been updated successfully')



    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Test123',database='mydata')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from hospital')
        rows= my_cursor.fetchall()
        if len(rows)!=0 :
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row= content["values"]
        self.Nameoftablet.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NoofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Storage.set(row[8])
        self.NhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAdress.set(row[12])
      
      #===========Function for Prescription button=============
    def iprescription(self):
        self.txtPrescription.insert(END , 'Name of Tablets:\t\t\t'+ self.Nameoftablet.get()+'\n')
        self.txtPrescription.insert(END , 'Reference No:\t\t\t'+ self.Ref.get()+'\n')
        self.txtPrescription.insert(END , 'Dose:\t\t\t'+ self.Dose.get()+ '\n')
        self.txtPrescription.insert(END , 'Number of Tablets:\t\t\t'+ self.NoofTablets.get()+'\n')
        self.txtPrescription.insert(END , 'Lot:\t\t\t'+ self.Lot.get()+'\n')
        self.txtPrescription.insert(END , 'Issue Date:\t\t\t'+ self.IssueDate.get()+'\n')
        self.txtPrescription.insert(END , 'Exp Date:\t\t\t'+ self.ExpDate.get()+'\n')
        self.txtPrescription.insert(END , 'Daily Dose:\t\t\t'+ self.DailyDose.get()+'\n')
        self.txtPrescription.insert(END , 'Side Effect:\t\t\t'+ self.SideEffect.get()+'\n')
        self.txtPrescription.insert(END , 'Further Information:\t\t\t'+ self.FurtherInfo.get()+'\n')
        self.txtPrescription.insert(END , 'Storage Advice:\t\t\t'+ self.Storage.get()+'\n')
        self.txtPrescription.insert(END , 'DrivingUsingMachine:\t\t\t'+ self.DrivingUsingmachine.get()+'\n')
        self.txtPrescription.insert(END , 'Pattient Id:\t\t\t'+ self.PatientId.get()+'\n')
        self.txtPrescription.insert(END , 'NHSNumber:\t\t\t'+ self.NhsNumber.get()+'\n')
        self.txtPrescription.insert(END , 'Patient Name:\t\t\t'+ self.PatientName.get()+'\n')
        self.txtPrescription.insert(END , 'Date of Birth:\t\t\t'+ self.DateOfBirth.get()+'\n')
        self.txtPrescription.insert(END , 'Patient Adress:\t\t\t'+ self.PatientAdress.get()+'\n')


    def iDelete(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Test123',database='mydata')
        my_cursor = conn.cursor()
        #new way of writing query
        query = 'delete from hospital where refrenceno=%s'
        value = (self.Ref.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo('Delete', 'Patient record has been deleted succesfully')

    def clear(self):
        self.Nameoftablet.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NoofTablets.set('')
        self.Lot.set('')
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.SideEffect.set("")
        self.FurtherInfo.set("")
        self.Storage.set("")
        self.DrivingUsingmachine.set("")
        self.HowtoUseMedication.set("")
        self.PatientId.set("")
        self.PatientName.set("")
        self.PatientAdress.set("")
        self.DateOfBirth.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return



root= Tk()
ob= Hospital(root)
root.mainloop()