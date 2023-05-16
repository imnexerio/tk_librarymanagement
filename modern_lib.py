from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import customtkinter
import tkinter

app=customtkinter.CTk()
app.geometry('900x700')
app.title('Library Management')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")

studentTable = 'students'
issueTable = 'trans'
bookTable='bookTable'
mypass = "root"
mydatabase="library"
allBid = [] 
fund=''
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS bookTable (book_id varchar(20) primary key, title varchar(30), author varchar(30), subject varchar(30), publication varchar(30), edition varchar(30), total_no_of_copies int(30), no_of_copies_available int(30), book_location varchar(30), status varchar(30))'
    )
cur.execute(
    'CREATE TABLE IF NOT EXISTS trans (student_id varchar(20) primary key, name varchar(30), title varchar(20), issue_date date, return_date date)'
    )
cur.execute(
    'CREATE TABLE IF NOT EXISTS students (student_id varchar(20) primary key, name varchar(30), DOB date)'
    )
 
def onetime_data_add():
    insertBooks = "insert into bookTable (book_id,title,author,subject,publication,edition,total_no_of_copies,no_of_copies_available,book_location,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vallue=(('b1','cmaths','unknown','Maths','cengage','3',5,3,'r1c4','available'))
    try:
        cur.execute(insertBooks,vallue)
        con.commit()
        messagebox.showinfo('Success',"All set for First time use")
    except:
        pass
onetime_data_add()

def loginn():

    def button_function():
        l2.destroy()
        entry1.destroy()
        entry2.destroy()
        l3.destroy()
        button1.destroy()
        frame.destroy()
        
        def maiin():
            
                
            def addBook():   

                bbtn0.destroy()
                bbtn1.destroy()
                bbtn2.destroy()
                bbtn3.destroy()
                bbtn4.destroy()
                bbtn5.destroy()
                qquitBtn.destroy()
                fframe1.destroy()
                llabel1.destroy()

                def baack():
                    quitBtn.destroy()
                    SubmitBtn.destroy()
                    bookInfo10.destroy()
                    bookInfo9.destroy()
                    bookInfo8.destroy()
                    bookInfo7.destroy()
                    bookInfo6.destroy()
                    bookInfo5.destroy()
                    bookInfo4.destroy()
                    bookInfo3.destroy()
                    bookInfo2.destroy()
                    bookInfo1.destroy()
                    headingFrame1a.destroy()
                    headingLabela.destroy()
                    maiin()

                def bookRegister():

                    book_id = bookInfo1.get()
                    title = bookInfo2.get()
                    author = bookInfo3.get()
                    subject=bookInfo4.get()
                    publication=bookInfo5.get()
                    edition=bookInfo6.get()
                    total_no_of_copies=bookInfo7.get()
                    no_of_copies_available=bookInfo8.get()
                    book_location=bookInfo9.get()
                    status = bookInfo10.get()
                    status = status.lower()
                    print(book_id,title,author,subject,publication,edition,total_no_of_copies,no_of_copies_available,status)
                    
                    insertBooks = "insert into bookTable (book_id,title,author,subject,publication,edition,total_no_of_copies,no_of_copies_available,book_location,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    vallue=(book_id,title,author,subject,publication,edition,total_no_of_copies,no_of_copies_available,book_location,status)
                    try:
                        cur.execute(insertBooks,vallue)
                        con.commit()
                        messagebox.showinfo('Success',"Book added successfully")
                    except:
                        messagebox.showinfo("Error","Can't add data into Database")

                #img1=ImageTk.PhotoImage(Image.open(r"C:\Users\santo\OneDrive\Documents\Program\Office\library\custom_tkinter_login-master\pattern.png"))
                #l1=customtkinter.CTkLabel(master=w,image=img1)
                #l1.pack()
                    
                headingFrame1a = customtkinter.CTkFrame(master=app,width=650,height=550,corner_radius=15)
                headingFrame1a.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

                headingLabela = customtkinter.CTkLabel(master=headingFrame1a, text="Add Books", font=('Century Gothic',20))
                headingLabela.place(x=300,y=45)

                    
                # Book ID
                    
                bookInfo1 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Book ID')
                bookInfo1.place(x=100,y=160)
                    
                # Title            
                bookInfo2 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Book Title')
                bookInfo2.place(x=100,y=210)
                    
                # Book Author
                bookInfo3 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Book Author')
                bookInfo3.place(x=100,y=260)

                #Book Subject
                bookInfo4 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Subject')
                bookInfo4.place(x=100,y=310)

                #Book Publication
                bookInfo5 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Publication')
                bookInfo5.place(x=100,y=360)

                #Book Edition
                bookInfo6 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Edition')
                bookInfo6.place(x=380,y=360)

                #Book total no of copies
                bookInfo7 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Total no of copies')
                bookInfo7.place(x=380,y=160)

                #Book total copies available
                bookInfo8 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Available Copies')
                bookInfo8.place(x=380,y=210)

                #Book location
                bookInfo9 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Book Location')
                bookInfo9.place(x=380,y=260)

                # Book Status
                bookInfo10 = customtkinter.CTkEntry(master=headingFrame1a,width=180,placeholder_text='Status')
                bookInfo10.place(x=380,y=310)

                #Submit customtkinter.CTkButton
                SubmitBtn = customtkinter.CTkButton(master=headingFrame1a,text="SUBMIT",width=180,command=bookRegister,corner_radius=6)
                SubmitBtn.place(x=100,y=410)

                quitBtn = customtkinter.CTkButton(master=headingFrame1a,text="Back",width=180 ,command=baack,corner_radius=6)
                quitBtn.place(x=380,y=410)

                #app.mainloop()
                
                
            def delete_tk(): 
                bbtn0.destroy()
                bbtn1.destroy()
                bbtn2.destroy()
                bbtn3.destroy()
                bbtn4.destroy()
                bbtn5.destroy()
                qquitBtn.destroy()
                fframe1.destroy()
                llabel1.destroy()

                def baack():
                    bookInfo1d.destroy()
                    SubmitBtnd.destroy()
                    quitBtnd.destroy()
                    headingLabeld.destroy()
                    headingFrame1d.destroy()
                    maiin()

                def deleteBook():
                
                    book_id = bookInfo1d.get()
                    
                    deleteSql = "delete from "+bookTable+" where book_id = "+"'"+book_id+"'"
                    #deleteIssue = "delete from "+issueTable+" where book_id = "+book_id
                    try:
                        cur.execute(deleteSql)
                        con.commit()
                        #cur.execute(deleteIssue)
                        #con.commit()
                        messagebox.showinfo('Success',"Book Record Deleted Successfully")
                    except:
                        messagebox.showinfo("Please check Book ID"+book_id)
                    

                    bookInfo1d.delete(0, END)
                
                headingFrame1d = customtkinter.CTkFrame(master=app,width=450,height=350,corner_radius=15)
                headingFrame1d.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
                    
                headingLabeld = customtkinter.CTkLabel(master=headingFrame1d, text="Delete Book",font=('Century Gothic',20))
                headingLabeld.place(x=170,y=45)
            
                # Book ID to Delete            
                bookInfo1d = customtkinter.CTkEntry(master=headingFrame1d,width=180,placeholder_text='Book ID to Delete')
                bookInfo1d.place(x=150,y=150)
                
                #Submit customtkinter.CTkButton
                SubmitBtnd = customtkinter.CTkButton(master=headingFrame1d,text="SUBMIT",width=150,command=deleteBook,corner_radius=6)
                SubmitBtnd.place(x=70,y=280)
                
                quitBtnd = customtkinter.CTkButton(master=headingFrame1d,text="Back",width=150,command=baack,corner_radius=6)
                quitBtnd.place(x=250,y=280)


                
            def View():
                bbtn0.destroy()
                bbtn1.destroy()
                bbtn2.destroy()
                bbtn3.destroy()
                bbtn4.destroy()
                bbtn5.destroy()
                qquitBtn.destroy()
                fframe1.destroy()
                llabel1.destroy()

                def baack():
                    quitBtnv.destroy()
                    headingLabelv.destroy()
                    headingFrame1v.destroy()
                    maiin()
                        
                    
                headingFrame1v = customtkinter.CTkFrame(master=app,width=800,height=550,corner_radius=15)
                headingFrame1v.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
                    
                headingLabelv = customtkinter.CTkLabel(headingFrame1v, text="View Books",font=('Century Gothic',20))
                headingLabelv.place(x=350,y=45)
                
                yy = 140
                
                customtkinter.CTkLabel(headingFrame1v, text="%-10s%-20s%-10s%-20s%-20s%-15s%-25s%-20s%-20s%-10s"%('BID','Title','Author','Subject','Publication','Edition','Total no of copies','Available copies','Book Location ','Status')).place(x=10,y=100)
                customtkinter.CTkLabel(headingFrame1v, text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(x=5,y=120)
                getBooks = "select * from "+bookTable+" where status = 'available'"
                try:
                    cur.execute(getBooks)
                    con.commit()
                    for i in cur:
                        print(i)
                        customtkinter.CTkLabel(headingFrame1v,text="%-10s%-15s%-10s%-20s%-28s%-18s%-40s%-30s%-20s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])).place(x=10,y=yy)
                        yy += 20
                except:
                    messagebox.showinfo("Failed to fetch files from database")
                
                quitBtnv = customtkinter.CTkButton(master=headingFrame1v,text="Back",command=baack,corner_radius=6)
                quitBtnv.place(x=350,y=510)


                
                
            def issueBook():
                bbtn0.destroy()
                bbtn1.destroy()
                bbtn2.destroy()
                bbtn3.destroy()
                bbtn4.destroy()
                bbtn5.destroy()
                qquitBtn.destroy()
                fframe1.destroy()
                llabel1.destroy()

                def baack():
                    inf4i.destroy()
                    inf3i.destroy()
                    inf2i.destroy()
                    inf1i.destroy()
                    issueBtni.destroy()
                    quitBtni.destroy()
                    headingFrame1i.destroy()
                    headingLabeli.destroy()
                    maiin()



                def issue():

                    book_id = inf1i.get()
                    student_id = inf2i.get()
                    issue_date=inf3i.get()
                    return_date=inf4i.get()
                    
                    
                    extractBid = "select book_id from "+bookTable
                    try:
                        cur.execute(extractBid)
                        con.commit()
                        for i in cur:
                            allBid.append(i[0])
                        
                        if book_id in allBid:
                            checkAvail = "select status from "+bookTable+" where book_id = "+"'"+book_id+"'"
                            cur.execute(checkAvail)
                            con.commit()
                            for i in cur:
                                check = i[0]
                                
                            if check == 'available':
                                status = True
                            else:
                                status = False

                        else:
                            messagebox.showinfo("Error","Book ID not present")
                    except:
                        messagebox.showinfo("Error","Can't fetch Book IDs")

                        
                    
                    issueSql = "insert into "+issueTable+" (student_id,book_id,issue_date,return_date) VALUS (%s,%s,%s,%s)"
                    vaalu=(student_id,book_id,issue_date,return_date)
                    show = "select * from "+issueTable
                    
                    updateStatus = "update "+bookTable+" set status = 'issued' where book_id = "+"'"+book_id+"'"

                    try:
                        if book_id in allBid and status == True:
                            cur.execute(issueSql,vaalu)
                            con.commit()
                            cur.execute(updateStatus)
                            con.commit()
                            messagebox.showinfo('Success',"Book Issued Successfully")
                            baack()
                        else:
                            allBid.clear()
                            messagebox.showinfo('Message',"Book Already Issued")
                            return
                    except:
                        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
                    
                    allBid.clear()


                headingFrame1i = customtkinter.CTkFrame(master=app,width=550,height=450,corner_radius=15)
                headingFrame1i.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
                    
                headingLabeli = customtkinter.CTkLabel(headingFrame1i, text="Issue Book",font=('Century Gothic',20))
                headingLabeli.place(x=220,y=45)
                    
                # Book ID
                inf1i = customtkinter.CTkEntry(master=headingFrame1i,width=180,placeholder_text='Book ID')
                inf1i.place(x=200,y=130)
                
                # student_id            
                inf2i = customtkinter.CTkEntry(master=headingFrame1i,width=180,placeholder_text='Student ID')
                inf2i.place(x=200,y=190)

                # issuing from
                inf3i = customtkinter.CTkEntry(master=headingFrame1i,width=180,placeholder_text='Issuing from (YYYY-MM-DD)')
                inf3i.place(x=200,y=250)

                # Issuing upto 
                inf4i = customtkinter.CTkEntry(master=headingFrame1i,width=180,placeholder_text='Issuing upto (YYYY-MM-DD)')
                inf4i.place(x=200,y=310)
                
                #Issue customtkinter.CTkButton
                issueBtni = customtkinter.CTkButton(master=headingFrame1i,text="Issue",width=180,command=issue,corner_radius=6)
                issueBtni.place(x=70,y=390)
                
                quitBtni = customtkinter.CTkButton(master=headingFrame1i,text="Back",width=180, command=baack,corner_radius=6)
                quitBtni.place(x=330,y=390)
                


                
            def returnBook():
                bbtn0.destroy()
                bbtn1.destroy()
                bbtn2.destroy()
                bbtn3.destroy()
                bbtn4.destroy()
                bbtn5.destroy()
                qquitBtn.destroy()
                fframe1.destroy()
                llabel1.destroy()

                def baack():
                    bookInfo1r.destroy()
                    bookInfo2r.destroy()
                    SubmitBtnr.destroy()
                    quitBtnr.destroy()
                    headingLabelr.destroy()
                    labelFramer.destroy()
                    maiin()


                def returnn():
                
                    book_id = bookInfo1r.get()

                    extractBid = "select book_id from "+issueTable
                    try:
                        cur.execute(extractBid)
                        con.commit()
                        for i in cur:
                            allBid.append(i[0])
                        
                        if book_id in allBid:
                            checkAvail = "select status from "+bookTable+" where book_id = "+"'"+book_id+"'"
                            cur.execute(checkAvail)
                            con.commit()
                            for i in cur:
                                check = i[0]
                                
                            if check == 'issued':
                                status = True
                            else:
                                status = False

                        else:
                            messagebox.showinfo("Error","Book ID not present")
                    except:
                        messagebox.showinfo("Error","Can't fetch Book IDs")
                    
                    
                    issueSql = "delete from "+issueTable+" where book_id = "+"'"+book_id+"'"
                    #issueSql1 = "delete from "+issueTable+" where book_id = '"+book_id+"'"

                    updateStatus = "update "+bookTable+" set status = 'available' where book_id = "+"'"+book_id+"'"
                    #updateStatus1 = "update "+bookTable+" set status = 'available' where book_id = '"+book_id+"'"

                    try:
                        if book_id in allBid and status == True:
                            cur.execute(issueSql)
                            #cur.execute(issueSql1)
                            con.commit()
                            cur.execute(updateStatus)
                            con.commit()
                            messagebox.showinfo('Success',"Book Returned Successfully")
                        else:
                            allBid.clear()
                            messagebox.showinfo('Message',"Please check the book ID")
                            return
                    except:
                        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
                    
                    
                    allBid.clear()
                
                labelFramer = customtkinter.CTkFrame(master=app,width=500,height=350,corner_radius=15)
                labelFramer.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)   

                headingLabelr = customtkinter.CTkLabel(master=labelFramer, text="Return Book", font=('Century Gothic',20))
                headingLabelr.place(x=190,y=45)
                    
                # Book ID to Delete            
                bookInfo1r = customtkinter.CTkEntry(master=labelFramer,width=180,placeholder_text='Book ID')
                bookInfo1r.place(x=175,y=120)

                # student ID to Delete
                bookInfo2r = customtkinter.CTkEntry(master=labelFramer,width=180,placeholder_text='Student id')
                bookInfo2r.place(x=175,y=190)
                
                #Submit customtkinter.CTkButton
                SubmitBtnr = customtkinter.CTkButton(master=labelFramer,text="Return",width=180,command=returnn,corner_radius=6)
                SubmitBtnr.place(x=100,y=280)
                
                quitBtnr = customtkinter.CTkButton(master=labelFramer,text="Back",width=180, command=baack,corner_radius=6)
                quitBtnr.place(x=300,y=280)
                

                
            def addStudent():
                bbtn0.destroy()
                bbtn1.destroy()
                bbtn2.destroy()
                bbtn3.destroy()
                bbtn4.destroy()
                bbtn5.destroy()
                qquitBtn.destroy()
                fframe1.destroy()
                llabel1.destroy()

                def baack():
                    studentInfo1rr.destroy()
                    studentInfo2rr.destroy()
                    bookInfo3rr.destroy()
                    SubmitBtnrr.destroy()
                    quitBtnrr.destroy()
                    headingLabelrr.destroy()
                    labelFramerr.destroy()
                    maiin()


                def studentRegister():
                
                    student_id = studentInfo1rr.get()
                    name = studentInfo2rr.get()
                    DOB = bookInfo3rr.get()
                    
                    insertstudents = "insert into "+studentTable+" (student_id,name,DOB) Values (%s,%s,%s)" 
                    vaalu=(student_id,name,DOB)
                    try:
                        cur.execute(insertstudents,vaalu)
                        con.commit()
                        messagebox.showinfo('Success',"Student added successfully")
                    except:
                        messagebox.showinfo("Error","Can't add data into Database")

                labelFramerr = customtkinter.CTkFrame(master=app,width=500,height=400,corner_radius=15)
                labelFramerr.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
                
                headingLabelrr = customtkinter.CTkLabel(master=labelFramerr, text="Add Students", font=('Century Gothic',20))
                headingLabelrr.place(x=200,y=45)
            
                # student ID    
                studentInfo1rr = customtkinter.CTkEntry(master=labelFramerr,width=180,placeholder_text="Student ID")
                studentInfo1rr.place(x=180,y=120)
                    
                # name   
                studentInfo2rr = customtkinter.CTkEntry(master=labelFramerr,width=180,placeholder_text="Name")
                studentInfo2rr.place(x=180,y=180)
                    
                # DOB   
                bookInfo3rr = customtkinter.CTkEntry(master=labelFramerr,width=180,placeholder_text='DOB (YYYY-MM-DD)')
                bookInfo3rr.place(x=180,y=240)

                #Submit customtkinter.CTkButton
                SubmitBtnrr = customtkinter.CTkButton(master=labelFramerr,text="SUBMIT",width=180,command=studentRegister,corner_radius=6)
                SubmitBtnrr.place(x=50,y=320)
                
                quitBtnrr = customtkinter.CTkButton(master=labelFramerr,text="Back",width=180,command=baack,corner_radius=6)
                quitBtnrr.place(x=280,y=320)
                


            fframe1 = customtkinter.CTkFrame(master=app,width=650,height=550,corner_radius=15)
            fframe1.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

            llabel1=customtkinter.CTkLabel(master=fframe1, text="Welcome to \n Library Management",font=('Century Gothic',20))
            llabel1.place(x=220, y=45)

            
            bbtn0 = customtkinter.CTkButton(master=fframe1,width=220,text="Add Book Details",height=37, command=addBook,corner_radius=6)
            bbtn0.place(x=220,y=150)


            bbtn1 = customtkinter.CTkButton(master=fframe1,width=220,text="Add New Student",height=37, command=addStudent,corner_radius=6)
            bbtn1.place(x=220,y=205)
                
            bbtn2 = customtkinter.CTkButton(master=fframe1,text="Delete Book",width=220,height=37,command=delete_tk,corner_radius=6)
            bbtn2.place(x=220,y=260)
                
            bbtn3 = customtkinter.CTkButton(master=fframe1,text="View Available Books",width=220,height=37, command=View,corner_radius=6)
            bbtn3.place(x=220,y=315)
                
            bbtn4 = customtkinter.CTkButton(master=fframe1,text="Issue Book to Student",width=220,height=37, command = issueBook,corner_radius=6)
            bbtn4.place(x=220,y=370)
                
            bbtn5 = customtkinter.CTkButton(master=fframe1,text="Return Book",width=220,height=37, command = returnBook,corner_radius=6)
            bbtn5.place(x=220,y=425)

            qquitBtn = customtkinter.CTkButton(master=fframe1,text="Quit",width=220,height=37, command = app.destroy,corner_radius=6)
            qquitBtn.place(x=220,y=480)

            '''mydatabase=entry1.get()
            mypass=entry2.get
            con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
            cur = con.cursor()'''

            if entry1.get()!='libray':
                messagebox.showinfo('Login error')
                app.destroy()
            elif entry2.get()!='root':
                messagebox.showinfo('Login error')
                app.destroy()
                

        maiin()         

    img1=ImageTk.PhotoImage(Image.open("library.png"))
    l1=customtkinter.CTkLabel(master=app,image=img1)
    l1.pack()

    #creating custom frame
    frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
    l2.place(x=50, y=45)

    entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
    l3.place(x=155,y=195)

    #Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
    button1.place(x=50, y=240)

    app.mainloop()
loginn()