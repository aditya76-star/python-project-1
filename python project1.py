from tkinter import *
from tkinter import messagebox
import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "oracle",
    database = "project"
)
cursor = con.cursor()
def submit():
    collagename = variablecollagename.get()
    corsename = variablecoursename.get()
    contactnumber = variablecontactnumber.get()
    Gmail = variablegmailcollage.get()
    website = variablewebsite.get()
    password = variablepassword.get()
    if collagename and corsename and contactnumber and Gmail and website and password:
        try:
            query = "insert into detail values(%s, %s, %s, %s, %s, %s)"
            values = (collagename, corsename, contactnumber, Gmail, website, password)
            cursor.execute(query,values)
            con.commit()
            messagebox.showinfo("Success", "Registration successful!")
            variablecollagename.set('')
            variablecoursename.set('')
            variablecontactnumber.set('')
            variablegmailcollage.set('')
            variablewebsite.set('')
            variablepassword.set('')
        except mysql.connector.Error as err:
            messagebox.showinfo("Database Error", f"Error : {err}")
    else:
        messagebox.showinfo("Input Error", "All fields are requied")
k = Tk()
k.geometry('500x400')
k.title('FORM')

labeloftitle = Label(k, text='COLLEGE FORM', font='comicsansms 20 bold', background='green', borderwidth=7, relief=SOLID)
labeloftitle.grid(row=0, column=0, padx=20, pady=20)

collagename = Label(k, text='College Name:')
corsename = Label(k, text='Course Name:')
contactnumber = Label(k, text='Contact Number:')
Gmail = Label(k, text='Gmail:')
website = Label(k, text='Website:')
password = Label(k, text='Password:')

collagename.grid(row=1, column=0, padx=10, pady=5)
corsename.grid(row=2, column=0, padx=10, pady=5)
contactnumber.grid(row=3, column=0, padx=10, pady=5)
Gmail.grid(row=4, column=0, padx=10, pady=5)
website.grid(row=5, column=0, padx=10, pady=5)
password.grid(row=6, column=0, padx=10, pady=5)

variablecollagename = StringVar()
variablecoursename = StringVar()
variablecontactnumber = StringVar()
variablegmailcollage = StringVar()
variablewebsite = StringVar()
variablepassword = StringVar()
cheakboxvalue = IntVar()

enter_1 = Entry(k, textvariable=variablecollagename)
enter_2 = Entry(k, textvariable=variablecoursename)
enter_3 = Entry(k, textvariable=variablecontactnumber)
enter_4 = Entry(k, textvariable=variablegmailcollage)
enter_5 = Entry(k, textvariable=variablewebsite)
enter_6 = Entry(k, textvariable=variablepassword,show='*')

enter_1.grid(row=1, column=1, padx=10, pady=5)
enter_2.grid(row=2, column=1, padx=10, pady=5)
enter_3.grid(row=3, column=1, padx=10, pady=5)
enter_4.grid(row=4, column=1, padx=10, pady=5)
enter_5.grid(row=5, column=1, padx=10, pady=5)
enter_6.grid(row=6, column=1, padx=10, pady=5)

# Checkbox
checkbutton = Checkbutton(k, text='Want to submit', variable=cheakboxvalue)
checkbutton.grid(row=7, column=0, columnspan=2, pady=10)

# Submit button
button_form = Button(k, text='SUBMIT FORM', bg='orange', fg='black', command=submit)
button_form.grid(row=8, column=0, columnspan=2, pady=20)

k.mainloop()