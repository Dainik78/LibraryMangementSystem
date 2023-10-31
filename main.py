from tkinter import *
from tkinter import messagebox
from tkinter import ttk


w=Tk()
w.geometry("500x500")
w.config(bg="#00FFFF")
def display():
    messagebox.showinfo("success","Welcome to our Library")

def returnbook():

    def des():
        w.destroy()
    w=Tk()
    w.config(bg="#00FFFF")
    w.title("Return Book")
    w.geometry("500x500")
    l=Label(w,text="Return Book",font=("arialbold",25))
    l.place(x=180,y=40)
    l1=Label(w,text="Student ID",font=("arialblack",13))
    l1.place(x=20,y=120)
    e1=Entry(w,bd=3)
    e1.place(x=140,y=120)
    l1=Label(w,text="Book Name",font=("arialblack",13))
    l1.place(x=20,y=190)
    e3=Entry(w,bd=3)
    e3.place(x=140,y=190)
    l2=Label(w,text="Book ID",font=("arialblack",13))
    l2.place(x=20,y=260)
    e2=Entry(w,bd=3)
    e2.place(x=140,y=260)
    b1=Button(w,text="Delete book",width=18,height=2,activebackground="green")
    b1.place(x=20,y=360)
    b2=Button(w,text="Cancel",width=18,height=2,command=des,activebackground="green")
    b2.place(x=320,y=360)


def deletebook():

    def des():
        w.destroy()
    w=Tk()
    w.config(bg="#00FFFF")
    w.title("Delete Book")
    w.geometry("500x500")
    l=Label(w,text="Delete Book",font=("arialbold",25))
    l.place(x=180,y=40)
    l1=Label(w,text="Student ID",font=("arialblack",13))
    l1.place(x=20,y=120)
    e1=Entry(w,bd=3)
    e1.place(x=140,y=120)
    l1=Label(w,text="Book Name",font=("arialblack",13))
    l1.place(x=20,y=190)
    e3=Entry(w,bd=3)
    e3.place(x=140,y=190)
    l2=Label(w,text="Author Name",font=("arialblack",13))
    l2.place(x=20,y=260)
    e2=Entry(w,bd=3)
    e2.place(x=140,y=260)
    # l3=Label(w,text="Edition",font=("arialblack",13))
    # l3.grid(row=3,column=1)
    # n=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    # drp=ttk.Combobox(w,width=20,values=n)
    # drp.current("0")
    # drp.grid(row=3,column=2)
    l4=Label(w,text="Book ID",font=("arialblack",13))
    l4.place(x=20,y=310)
    e4=Entry(w,bd=3)
    e4.place(x=140,y=310)
    b1=Button(w,text="Delete book",width=18,height=2,activebackground="green")
    b1.place(x=20,y=360)
    b2=Button(w,text="Cancel",width=18,height=2,command=des,activebackground="green")
    b2.place(x=320,y=360)

def addbook():
    def des():
        w.destroy()
    w=Tk()
    w.config(bg="#00FFFF")
    w.title("add book details")
    w.geometry("500x500")
    l=Label(w,text="Issue Book",font=("arialbold",25))
    l.place(x=180,y=40)
    l1=Label(w,text="Book Name",font=("arialblack",13))
    l1.place(x=20,y=120)
    e1=Entry(w,bd=3)
    e1.place(x=140,y=120)
    l2=Label(w,text="Author Name",font=("arialblack",13))
    l2.place(x=20,y=190)
    e2=Entry(w,bd=3)
    e2.place(x=140,y=190)
    l3=Label(w,text="Edition",font=("arialblack",13))
    l3.place(x=20,y=260)
    n=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    drp=ttk.Combobox(w,width=20,values=n)
    drp.current("0")
    drp.place(x=140,y=260)
    l4=Label(w,text="Book ID",font=("arialblack",13))
    l4.place(x=20,y=330)
    e4=Entry(w,bd=3)
    e4.place(x=140,y=330)
    b1=Button(w,text="Add book",width=15,height=2,activebackground="green")
    b1.place(x=20,y=400)
    b2=Button(w,text="Cancel",width=15,height=2,command=des,activebackground="green")
    b2.place(x=150,y=400)
    


def issuebook():
    def des():
        w.destroy()
    w=Tk()
    w.config(bg="#00FFFF")
    w.title("issuebbok")
    w.geometry("500x500")
    l=Label(w,text="Issue Book",font=("arialbold",25),bg="#00FFFF")
    l.grid(row=0,columnspan=3)
    l1=Label(w,text="Student ID",font=("arialblack",13),bg="#00FFFF")
    l1.grid(row=2,column=1)
    e1=Entry(w,bd=3)
    e1.grid(row=2,column=2)
    # l2=Label(w,text="Student Name",font=("arialblack",13))
    # l2.grid(row=3,column=1)
    # e2=Entry(w,bd=3)
    # e2.grid(row=3,column=2)
    # l3=Label(w,text="Student Address",font=("arialblack",13))
    # l3.grid(row=4,column=1)
    # e3=Entry(w,bd=3)
    # e3.grid(row=4,column=2)
    l4=Label(w,text="Program",font=("arialblack",13),bg="#00FFFF")
    l4.grid(row=5,column=1)
    c=("select Your Course","BBA","BFM","Bsc IT","Bsc CS","B.com","LLB","BA","Other")
    month=ttk.Combobox(w,width=20,values=c)
    month.current(0)
    month.grid(row=5,column=2)
    l5=Label(w,text="Book ID",font=("arialblack",13),bg="#00FFFF")
    l5.grid(row=6,column=1)
    e5=Entry(w,bd=3)
    e5.grid(row=6,column=2)
    l6=Label(w,text="Issue date",font=("arialblack",13),bg="#00FFFF")
    l6.grid(row=7,column=1)
    e6=Entry(w,bd=3)
    e6.grid(row=7,column=2)
    l7=Label(w,text="Expiry date",font=("arialblack",13),bg="#00FFFF")
    l7.grid(row=8,column=1)
    e7=Entry(w,bd=3)
    e7.grid(row=8,column=2)
    b1=Button(w,text="Issue Book",activebackground="green",width=15,height=2)
    b1.grid(row=14,column=2)
    b2=Button(w,text="Cancel",activebackground="green",width=15,height=2,command=des)
    b2.grid(row=14,column=3)

    





    w.mainloop()



def view():




    
    from tkinter import messagebox
    def des():
        w.destroy()
    w=Tk()
    w.config(bg="#00FFFF")
    w.title("Book list")
    w.geometry("500x600")
    # f2=Frame()
    # f2.place(x=0,y=0,width=400,height=300)
    Label(w,text="bookid.",width=5,font=("arialbold",15),bg="#00FFFF").grid(row="1",column="1")
    Label(w,text="Name",width=15,font=("arialbold",15),bg="#00FFFF").grid(row="1",column="2")
    Label(w,text="Author",width=10,font=("arialbold",15),bg="#00FFFF").grid(row="1",column="3")
    Label(w,text="price",width=15,font=("arialbold",15),bg="#00FFFF").grid(row="1",column="4")
    Label(w,text="0001",width=5,font=("arial",10),bg="#00FFFF").grid(row="2",column="1")
    Label(w,text="Rich dad Poor dad",width=15,font=("arial",10),bg="#00FFFF").grid(row="2",column="2")
    Label(w,text="Robert Kiyosaki",width=11,font=("arial",10),bg="#00FFFF").grid(row="2",column="3")
    Label(w,text="$15",width=15,font=("arial",10),bg="#00FFFF").grid(row="2",column="4")
    Label(w,text="0002",width=5,font=("arial",10),bg="#00FFFF").grid(row="3",column="1")
    Label(w,text="Henry fielding",width=15,font=("arial",10),bg="#00FFFF").grid(row="3",column="2")
    Label(w,text="Tom Jones",width=11,font=("arial",10),bg="#00FFFF").grid(row="3",column="3")
    Label(w,text="$10",width=15,font=("arial",10),bg="#00FFFF").grid(row="3",column="4")
    Label(w,text="0003",width=5,font=("arial",10),bg="#00FFFF").grid(row="3",column="1")
    Label(w,text="Pickwick Paper",width=15,font=("arial",10),bg="#00FFFF").grid(row="3",column="2")
    Label(w,text="Charles Dickens",width=11,font=("arial",10),bg="#00FFFF").grid(row="3",column="3")
    Label(w,text="$50",width=15,font=("arial",10),bg="#00FFFF").grid(row="3",column="4")
    Label(w,text="0004",width=5,font=("arial",10),bg="#00FFFF").grid(row="4",column="1")
    Label(w,text="Oliver twist",width=15,font=("arial",10),bg="#00FFFF").grid(row="4",column="2")
    Label(w,text="Charles Dickens",width=11,font=("arial",10),bg="#00FFFF").grid(row="4",column="3")
    Label(w,text="$25",width=15,font=("arial",10),bg="#00FFFF").grid(row="4",column="4")
    Label(w,text="0005",width=5,font=("arial",10),bg="#00FFFF").grid(row="5",column="1")
    Label(w,text="Germinal",width=15,font=("arial",10),bg="#00FFFF").grid(row="5",column="2")
    Label(w,text="Emile Zola",width=11,font=("arial",10),bg="#00FFFF").grid(row="5",column="3")
    Label(w,text="$12",width=15,font=("arial",10),bg="#00FFFF").grid(row="5",column="4")
    Label(w,text="0006",width=5,font=("arial",10),bg="#00FFFF").grid(row="6",column="1")
    Label(w,text="Mayor of Casterbridge",width=15,font=("arial",10),bg="#00FFFF").grid(row="6",column="2")
    Label(w,text="Thomas hardy",width=11,font=("arial",10),bg="#00FFFF").grid(row="6",column="3")
    Label(w,text="$25",width=15,font=("arial",10),bg="#00FFFF").grid(row="6",column="4")
    Label(w,text="0007",width=5,font=("arial",10),bg="#00FFFF").grid(row="7",column="1")
    Label(w,text="The Jungle Book",width=15,font=("arial",10),bg="#00FFFF").grid(row="7",column="2")
    Label(w,text="Rudyard kipling",width=11,font=("arial",10),bg="#00FFFF").grid(row="7",column="3")
    Label(w,text="$20",width=15,font=("arial",10),bg="#00FFFF").grid(row="7",column="4")
    Label(w,text="0008",width=5,font=("arial",10),bg="#00FFFF").grid(row="8",column="1")
    Label(w,text="Ramona",width=15,font=("arial",10),bg="#00FFFF").grid(row="8",column="2")
    Label(w,text="Hunt jackson",width=11,font=("arial",10),bg="#00FFFF").grid(row="8",column="3")
    Label(w,text="$25",width=15,font=("arial",10),bg="#00FFFF").grid(row="8",column="4")
    Label(w,text="0009",width=5,font=("arial",10),bg="#00FFFF").grid(row="9",column="1")
    Label(w,text="Mukt mala",width=15,font=("arial",10),bg="#00FFFF").grid(row="9",column="2")
    Label(w,text="Lakshman Hable",width=11,font=("arial",10),bg="#00FFFF").grid(row="9",column="3")
    Label(w,text="$12",width=15,font=("arial",10),bg="#00FFFF").grid(row="9",column="4")
    Label(w,text="0010",width=5,font=("arial",10),bg="#00FFFF").grid(row="10",column="1")
    Label(w,text="Ramona",width=15,font=("arial",10),bg="#00FFFF").grid(row="10",column="2")
    Label(w,text="Srinivas Das",width=11,font=("arial",10),bg="#00FFFF").grid(row="10",column="3")
    Label(w,text="$12",width=15,font=("arial",10),bg="#00FFFF").grid(row="10",column="4")
    Label(w,text="0011",width=5,font=("arial",10),bg="#00FFFF").grid(row="11",column="1")
    Label(w,text="harry Potter",width=15,font=("arial",10),bg="#00FFFF").grid(row="11",column="2")
    Label(w,text="lora laiken",width=11,font=("arial",10),bg="#00FFFF").grid(row="11",column="3")
    Label(w,text="$15",width=15,font=("arial",10),bg="#00FFFF").grid(row="11",column="4")
    Label(w,text="0012",width=5,font=("arial",10),bg="#00FFFF").grid(row="12",column="1")
    Label(w,text="Indulekha",width=15,font=("arial",10)).grid(row="12",column="2")
    Label(w,text="Chandu Menon",width=11,font=("arial",10)).grid(row="12",column="3")
    Label(w,text="$26",width=15,font=("arial",10),bg="#00FFFF").grid(row="12",column="4")
    Label(w,text="0013",width=5,font=("arial",10),bg="#00FFFF").grid(row="13",column="1")
    Label(w,text="Ramayana",width=15,font=("arial",10),bg="#00FFFF").grid(row="13",column="2")
    Label(w,text="Guru Valmiki",width=11,font=("arial",10),bg="#00FFFF").grid(row="13",column="3")
    Label(w,text="$500",width=15,font=("arial",10),bg="#00FFFF").grid(row="13",column="4")
    Label(w,text="0014",width=5,font=("arial",10),bg="#00FFFF").grid(row="15",column="1")
    Label(w,text="Pride and Prejudice",width=15,font=("arial",10),bg="#00FFFF").grid(row="15",column="2")
    Label(w,text="Jane Austin",width=11,font=("arial",10),bg="#00FFFF").grid(row="15",column="3")
    Label(w,text="$5",width=15,font=("arial",10),bg="#00FFFF").grid(row="15",column="4")
    Label(w,text="George Ellit",width=11,font=("arial",10),bg="#00FFFF").grid(row="15",column="3")    
    Label(w,text="$7",width=15,font=("arial",10),bg="#00FFFF").grid(row="15",column="4")
    Label(w,text="0016",width=5,font=("arial",10),bg="#00FFFF").grid(row="16",column="1")
    Label(w,text="Robinson Cursor",width=15,font=("arial",10),bg="#00FFFF").grid(row="16",column="2")
    Label(w,text="Ramesh bhai",width=11,font=("arial",10),bg="#00FFFF").grid(row="16",column="3")
    Label(w,text="$5",width=15,font=("arial",10),bg="#00FFFF").grid(row="16",column="4")
    Label(w,text="0017",width=5,font=("arial",10),bg="#00FFFF").grid(row="17",column="1")
    Label(w,text="Emirates",width=15,font=("arial",10),bg="#00FFFF").grid(row="17",column="2")
    Label(w,text="Bravo ",width=11,font=("arial",10),bg="#00FFFF").grid(row="17",column="3")
    Label(w,text="$20",width=15,font=("arial",10),bg="#00FFFF").grid(row="17",column="4")
    Label(w,text="0018",width=5,font=("arial",10),bg="#00FFFF").grid(row="18",column="1")
    Label(w,text="mumbai indians",width=15,font=("arial",10),bg="#00FFFF").grid(row="18",column="2")
    Label(w,text="Rohit Sharma",width=11,font=("arial",10),bg="#00FFFF").grid(row="18",column="3")
    Label(w,text="$17",width=15,font=("arial",10),bg="#00FFFF").grid(row="18",column="4")
    Label(w,text="0019",width=5,font=("arial",10),bg="#00FFFF").grid(row="19",column="1")
    Label(w,text="The help",width=15,font=("arial",10),bg="#00FFFF").grid(row="19",column="2")
    Label(w,text="kathryn Stockett",width=11,font=("arial",10),bg="#00FFFF").grid(row="19",column="3")
    Label(w,text="$52",width=15,font=("arial",10),bg="#00FFFF").grid(row="19",column="19")
    Label(w,text="0020",width=5,font=("arial",10),bg="#00FFFF").grid(row="20",column="1")
    Label(w,text="The Goldfinch",width=15,font=("arial",10),bg="#00FFFF").grid(row="20",column="2")
    Label(w,text="Donna Trtt",width=11,font=("arial",10),bg="#00FFFF").grid(row="20",column="3")
    Label(w,text="$25",width=15,font=("arial",10),bg="#00FFFF").grid(row="20",column="4")
    Label(w,text="0021",width=5,font=("arial",10),bg="#00FFFF").grid(row="21",column="1")
    Label(w,text="Origin",width=15,font=("arial",10),bg="#00FFFF").grid(row="21",column="2")
    Label(w,text="dan brown",width=11,font=("arial",10),bg="#00FFFF").grid(row="21",column="3")
    Label(w,text="FREE",width=15,font=("arialbold",10),bg="#00FFFF").grid(row="21",column="4")
# def ok():
#     w.destroy()
    Button(w,text="back",activebackground="green",command=des).grid(row=23,columnspan=4)
    
    w.mainloop()
    

def op():
    w=Tk()
    w.geometry("500x500")
    w.config(bg="#00FFFF")

    def des():
        w.destroy()
        def display():

            messagebox.showinfo("success","Welcome to our Library")

    
    l1=Button(w,text="Welcome guys",font=("arialbold",25),command=display,relief=FLAT)
    l1.place(x=100,y=30)
    Photo=PhotoImage(file="o1.png")
    l2=Label(image=Photo)
    l2.place(x=250,y=150)
    b1=Button(w,text="View Book List",width=25,relief=RAISED,command=view,height=2)
    b1.place(x=20,y=120)
    b2=Button(w,text="Issue Book to Student",width=25,command=issuebook,height=2)
    b2.place(x=20,y=170)
    b3=Button(w,text="Add Book details",width=25,height=2,command=addbook)
    b3.place(x=20,y=230)
    b4=Button(w,text="delete books",width=25,height=2,command=deletebook)
    b4.place(x=20,y=280)
    b5=Button(w,text="Return book",width=25,height=2)
    b5.place(x=20,y=330)
    b6=Button(w,text="exit",activebackground="green",width=20,command=des)
    b6.place(x=200,y=400)




def validateLogin():
    if  e1.get()=='login' and  e2.get()=='admin':
        messagebox.showinfo("success","Welcome to our Library")
        w=Tk()
        w.geometry("500x500")
        w.config(bg="#00FFFF")
        
        # def display():
            # messagebox.showinfo("success","Welcome to our Library")

        l1=Button(w,text="Welcome guys",font=("arialbold",25),command=display,relief=FLAT)
        l1.place(x=100,y=30)
        # Photo=PhotoImage(file="o1.png")
        # l2=Label(image=Photo)
        # l2.place(x=250,y=150)
        b1=Button(w,text="View Book List",width=25,relief=RAISED,command=view,height=2)
        b1.place(x=20,y=120)
        b2=Button(w,text="Issue Book to Student",width=25,command=issuebook,height=2)
        b2.place(x=20,y=170)
        b3=Button(w,text="Add Book details",width=25,height=2,command=addbook)
        b3.place(x=20,y=230)
        b4=Button(w,text="delete books",width=25,height=2,command=deletebook)
        b4.place(x=20,y=280)
        b5=Button(w,text="Return book",width=25,height=2,command=returnbook())
        b5.place(x=20,y=330)
        Photo=PhotoImage(file="o1.png")
        l2=Label(image=Photo)
        l2.place(x=250,y=150)
        b6=Button(w,text="exit",activebackground="green",width=20)#command=des
        b6.place(x=200,y=400)
        
        w.mainloop()

        


        
    else :


        messagebox.showwarning("warning","Please Provide required crediantals")
        w.destroy()
l=Label(w,text="Welcome Bibliophile",font=('Arialblack',30))
l.place(x=100,y=60)
l1=Label(w,text="UserName",font=("Arialblack",20))
l1.place(x=30,y=200)
e1=Entry(w,bd=3,font=('Arialblack,20'))
e1.place(x=180,y=200)
l1=Label(w,text="Password",font=("Arialblack",20))
l1.place(x=30,y=280)
e2=Entry(bd=3,show='*',font=('Arialblack,20'))
e2.place(x=180,y=280)
b1=Button(w,text="Login",width=15,font=("Arialblack",15),activebackground="green",command=validateLogin)
b1.place(x=180,y=350)
w.mainloop()


w.mainloop()



