from tkinter import*
import random
import time;

root= Tk()
root.geometry("1600x800+0+0")
root.title("PARKING MANAGEMENT SYSTEMS")

text_Input= StringVar()
operator =""

Tops= Frame(root, width=1600,height=50, bg="red",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
#--------------------------------------TIME---------------------------------------------------------------------------------------------------------------------
localtime=time.asctime(time.localtime(time.time()))
#------------------------------------------------------INFORMATION----------------------------------------------------------------------------------------------
lblInfo= Label(Tops, font=('algerian',50,'bold','underline'),text="PARKING MANAGEMENT SYSTEM",fg="black",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('broadway',20,'bold'),text=localtime,fg="red",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#------------------------------------------------------------------CALCULATOR-----------------------------------------------------------------------------------
def btnclick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    summation=str(eval(operator))
    text_Input.set(summation)
    operator=""

def Ref():
    x= random.randint(10000,800000)
    randomRef=str(x)
    rand.set(randomRef)

    CoFW=float(Fourwheeler.get())
    CoT=float(Truck.get())
    CoM=float(Motorbikes.get())
    CoPB=float(Public_Buses.get())
    CoTB=float(Tourist_Bus.get())

    TofFW=CoFW*20.00
    TofT=CoT*50.00
    TofM=CoM*15.00
    TofPB=CoPB*30.00
    TofTB=CoTB*40.00

    TicketCostW=int(TofFW+TofT+TofM+TofPB+TofTB)
    
    StateTaxW=int((TicketCostW*18)/100)
    
    ServiceChargeW=int(TicketCostW+150)

    TaxW=int(StateTaxW+((TicketCostW*5)/100))

    TotalW=int(TicketCostW+TaxW)

    SubTotalW=int(TotalW+ServiceChargeW)

    Sub_Total.set(SubTotalW)
    Total.set(TotalW)
    Service_Charge.set(ServiceChargeW)
    Tax.set(TaxW)
    Ticket_Cost.set(TicketCostW)
    StateTax.set(StateTaxW)










    import mysql.connector as w
    mydb=w.connect(host='localhost',user='root',passwd='root')
    y=mydb.cursor()
    y.execute('use mega')
    x=w.connect(host='localhost',user='root',passwd='root',database='mega')
    
    a=x.cursor()
    
    a1=rand.get()   # ref Ezio.emroz
    b1=Fourwheeler.get() 
    c1=Truck.get() 
    d1=Motorbikes.get() 
    e1=Public_Buses.get() 
    f1=Tourist_Bus.get() 
    g1=Sub_Total.get() 
    a.execute("insert into Gig(REFERENCE,FOURWHEELER,TRUCK,MOTORBIKE,PUBLIC_BUSES,TOURIST_BUSES,TOTAL)values('{}',{},{},{},{},{},{})".format(a1,b1,c1,d1,e1,f1,g1))
   
    x.commit()
    

def data():

    import mysql.connector as w
    mydb=w.connect(host='localhost',user='root',passwd='root')
    y=mydb.cursor()
    y.execute('create database mega')
    x=w.connect(host='localhost',user='root',passwd='root',database='PMS')
   
    a=x.cursor()
   
    a.execute('create table Gig(REFERENCE varchar(21),FOURWHEELER int(5),TRUCK int(5),MOTORBIKE int(5),PUBLIC_BUSES int(5),TOURIST_BUSES int(5),TOTAL int(11))')
   
    x.commit()

    
    '''import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234')
    mycursor=mydb.cursor()
    mycursor.execute('CREATE DATABASE PARKING_MANAGEMENT')
    x=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='go')
    x2=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='go')
    a=x.cursor()
    b=x2.cursor()
    a.execute('CREATE TABLE ENTRY(REFERENCE INTEGER(11),FOURWHEELER INTEGER(11),TRUCK(11),MOTORBIKE INTEGER (11),PUBLIC BUSES INTEGER(11),TOURIST BUSES(11))')
    b.execute('CREATE TABLE RESULT(SUB_TOTAL INTEGER(11),SERVICE CHARGE INTEGER(11),TAX INTEGER(11),TICKET_COST(11),STATE_TAX INTEGER(11))')
    x.commit()
    x2.commit()
    msg10.set('DATABASE IS CREATED')
    '''


def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fourwheeler.set("")
    Truck.set("")
    Motorbikes.set("")
    Sub_Total.set("")
    Total.set("")
    Service_Charge.set("")
    Public_Buses.set("")
    Tourist_Bus.set("")
    Tax.set("")
    Ticket_Cost.set("")
    StateTax.set("")

    
textdisplay=Entry(f2,font=('arial',18), textvariable=text_Input, bd=30,insertwidth=4,bg="white",justify='right')
textdisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='7' , bg="powder blue", command=lambda: btnclick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='8' , bg="powder blue", command=lambda: btnclick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='9' , bg="powder blue", command=lambda: btnclick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='+' , bg="powder blue", command=lambda: btnclick("+")).grid(row=2,column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='4' , bg="powder blue", command=lambda: btnclick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='5' , bg="powder blue", command=lambda: btnclick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='6' , bg="powder blue", command=lambda: btnclick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='-' , bg="powder blue", command=lambda: btnclick("-")).grid(row=3,column=3)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='1' , bg="powder blue", command=lambda: btnclick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='2' , bg="powder blue", command=lambda: btnclick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='3' , bg="powder blue", command=lambda: btnclick(3)).grid(row=4,column=2)

Multiplication=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='*' , bg="powder blue", command=lambda: btnclick("*")).grid(row=4,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='0' , bg="powder blue", command=lambda: btnclick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='C' , bg="powder blue", command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='=' , bg="powder blue", command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'), text='/' , bg="powder blue", command=lambda: btnclick("/")).grid(row=5,column=3)
#------------------------------------------------------------PARKING INFO 1-------------------------------------------------------------------------------------
rand=StringVar()
Fourwheeler=StringVar()
Truck=StringVar()
Motorbikes=StringVar()
Sub_Total=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Public_Buses=StringVar()
Tourist_Bus=StringVar()
Tax=StringVar()
Ticket_Cost=StringVar()
StateTax=StringVar()


lblreference = Label(f1,font=('arial',16,'bold'),text="REFERENCE", bd=16,anchor='w')
lblreference.grid(row=0,column=0)
txtreference=Entry(f1,font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4,bg="powder blue",justify= 'right')
txtreference.grid(row=0,column=1)


lblFourwheeler= Label(f1,font=('arial',16,'bold'),text="FOUR WHEELERS", bd=16,anchor='w')
lblFourwheeler.grid(row=1,column=0)
txtFourwheeler=Entry(f1,font=('arial',16,'bold'),textvariable=Fourwheeler, bd=10,insertwidth=4,bg="powder blue",justify= 'right')
txtFourwheeler.grid(row=1,column=1)


lblTruck=Label(f1,font=('arial',16,'bold'),text="TRUCK",bd=16,anchor='w')
lblTruck.grid(row=2,column=0)
txtTruck=Entry(f1,font=('arial',16,'bold'),textvariable=Truck, bd=16,insertwidth=4,bg="powder blue", justify='right')
txtTruck.grid(row=2,column=1)


lblMotorbikes=Label(f1,font=('arial',16,'bold'),text="MOTORBIKES",bd=16,anchor='w')
lblMotorbikes.grid(row=3,column=0)
txtMotorbikes=Entry(f1,font=('arial',16,'bold'),textvariable=Motorbikes, bd=16,insertwidth=4,bg="powder blue", justify='right')
txtMotorbikes.grid(row=3,column=1)


lblPublic_Buses=Label(f1,font=('arial',16,'bold'),text="PUBLIC BUSES",bd=16,anchor='w')
lblPublic_Buses.grid(row=4,column=0)
txtPublic_Buses=Entry(f1,font=('arial',16,'bold'),textvariable=Public_Buses, bd=16,insertwidth=4,bg="powder blue", justify='right')
txtPublic_Buses.grid(row=4,column=1)


lblTourist_Bus=Label(f1,font=('arial',16,'bold'),text="TOURIST BUSES",bd=16,anchor='w')
lblTourist_Bus.grid(row=5,column=0)
txtTourist_Bus=Entry(f1,font=('arial',16,'bold'),textvariable=Tourist_Bus, bd=16,insertwidth=4,bg="powder blue", justify='right')
txtTourist_Bus.grid(row=5,column=1)

#------------------------------------------------------------PARKING INFO 2-------------------------------------------------------------------------------------

lblSub_Total = Label(f1,font=('arial',16,'bold'),text="SUB_TOTAL", bd=16,anchor='w')
lblSub_Total.grid(row=0,column=2)
txtSub_Total=Entry(f1,font=('arial',16,'bold'),textvariable=Sub_Total, bd=10, insertwidth=4,bg="orange",justify= 'right')
txtSub_Total.grid(row=0,column=3)


lblTotal = Label(f1,font=('arial',16,'bold'),text="TOTAL", bd=16,anchor='w')
lblTotal.grid(row=1,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total, bd=10,insertwidth=4,bg="orange",justify= 'right')
txtTotal.grid(row=1,column=3)


lblService_Charge=Label(f1,font=('arial',16,'bold'),text="SERVICE CHARGE",bd=16,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge, bd=16,insertwidth=4,bg="orange", justify='right')
txtService_Charge.grid(row=2,column=3)


lblTax=Label(f1,font=('arial',16,'bold'),text="TAX",bd=16,anchor='w')
lblTax.grid(row=3,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax, bd=16,insertwidth=4,bg="orange", justify='right')
txtTax.grid(row=3,column=3)


lblTicket_Cost=Label(f1,font=('arial',16,'bold'),text="TICKET COST",bd=16,anchor='w')
lblTicket_Cost.grid(row=4,column=2)
txtTicket_Cost=Entry(f1,font=('arial',16,'bold'),textvariable=Ticket_Cost, bd=16,insertwidth=4,bg="orange", justify='right')
txtTicket_Cost.grid(row=4,column=3)


lblStateTax=Label(f1,font=('arial',16,'bold'),text="STATE TAX",bd=16,anchor='w')
lblStateTax.grid(row=5,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=StateTax, bd=16,insertwidth=4,bg="orange", justify='right')
txtStateTax.grid(row=5,column=3)
#----------------------------------------------------------------BUTTONS--------------------------------------------------------------------------------------------
btnTotal=Button(f1,padx=10,pady=8,bd=16,fg="black",font=('ariel',10,'bold'), width=10,
                text="TOTAL", bg="green",command=Ref).grid(row=7, column=0)
btnqExit=Button(f1,padx=10,pady=8,bd=16,fg="black",font=('ariel',10,'bold'), width=10,
                text="EXIT", bg="green",command=qExit).grid(row=7, column=1)
btnReset=Button(f1,padx=10,pady=8,bd=16,fg="black",font=('ariel',10,'bold'), width=10,
                text="RESET", bg="green",command=Reset).grid(row=7, column=2)
btnDatabase=Button(f1,padx=10,pady=8,bd=16,fg="black",font=('ariel',10,'bold'), width=10,
                text="DATABASE", bg="green",command=data).grid(row=7, column=3)
root.mainloop()
