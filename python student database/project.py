import tkinter 
from tkinter import ttk
import mysql.connector 
from tkinter import *
import tkinter.messagebox as messagebox
import subprocess
import re


window = tkinter.Tk()
window.geometry("1350x700+0+0")
window.title("student Management system")

conn=mysql.connector.connect(host="localhost",port="3306",username="root",password="",database="mypartproject_db")
cursor=conn.cursor()

command="CREATE TABLE IF NOT EXISTS students_guidb( `MatricNo` int(225), `Firstname` VARCHAR(225),`Lastname` VARCHAR(225),`Email` VARCHAR(225),`Mobilenumber` int(255),`Yearofentry` int(255),`Gender` CHAR(10),`DOB` VARCHAR(255),`DEPARTMENT` VARCHAR(255),`FACULTY` VARCHAR(255))"
cursor.execute(command)


import tkinter as tk
from tkinter import messagebox





#this is to display all the records in the database
def show_all():
    cursor.execute("SELECT * FROM students_guidb")
    records = cursor.fetchall()
    if len(records) != 0:
        student_table.delete(*student_table.get_children())
        for record in records:
            student_table.insert("", tkinter.END, values=record)
        conn.commit()
    
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        tooltip_label = tk.Label(self.tooltip, text=self.text, bg="white")
        tooltip_label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()   


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return re.match(pattern, email)

def click_me():
    matric_no = MatricNo.get()
    first_name = Firstname.get()
    last_name = Lastname.get()
    email = Email.get()
    department=Department.get()
    faculty=Faculty.get()
    if validate_email(email):
       
        
                mobile_number = Mobilenumber.get()
                year_of_entry = Yearofentry.get()
                gender = Gender.get()
                dob = DOB.get()
                 
                
                check_query = "SELECT * FROM students_guidb WHERE MatricNo = %s"
                values = (matric_no,)
                cursor.execute(check_query, values)
                existing_record = cursor.fetchall()

                if existing_record:
                        MatricNo.set("")
                        messagebox.showwarning("Invalid Matric Number", "Matric number already exists. Please enter a new matric number.")
                  
                
                     
        
                elif first_name and last_name and matric_no and email and mobile_number and dob and gender and year_of_entry and department and faculty:
                    insert_query = "INSERT INTO students_guidb(MatricNo, Firstname, Lastname, Email, Mobilenumber, Yearofentry, Gender, DOB,DEPARTMENT,FACULTY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
                    values = (matric_no, first_name, last_name, email, mobile_number, year_of_entry, gender, dob,department,faculty)
            
                    cursor.execute(insert_query, values)
                    conn.commit()
                    show_all()
            
            
                    messagebox.showinfo(title="Success", message="Student added successfully")
            
                    # Clear the input fields
                    MatricNo.set("")
                    Firstname.set("")
                    Lastname.set("")
                    Email.set("")
                    Mobilenumber.set("")
                    Yearofentry.set("")
                    Gender.set("")
                    DOB.set("")
                    Department.set("")
                    Faculty.set("")
                else:
                    messagebox.showwarning(title="ERROR!", message="Please enter all the fields")
    else:
                messagebox.showwarning("Invalid Email", "Please enter a valid email address")


def clear():
     #to clear all the values in the detail frame

    student_table.delete(*student_table.get_children())

def reset():
    MatricNo.set("")
    Firstname.set("")
    Lastname.set("")
    Email.set("")
    Mobilenumber.set("")
    Yearofentry.set("")
    Gender.set("")
    Department.set("")
    Faculty.set("")
    DOB.set("")
    

def update_data():
    # Retrieve the updated values from the entry fields
    
    matric_no = MatricNo.get()
    first_name = Firstname.get()
    last_name = Lastname.get()
    email = Email.get()
    mobile_number = Mobilenumber.get()
    year_of_entry = Yearofentry.get()
    gender = Gender.get()
    dob = DOB.get()
    department=Department.get()
    faculty=Faculty.get()

    


    # SQL UPDATE query
    update_query = "UPDATE students_guidb SET Firstname=%s, Lastname=%s, Email=%s, Mobilenumber=%s, Yearofentry=%s, Gender=%s,DEPARTMENT=%s,FACULTY=%s, DOB=%s WHERE MatricNo=%s"
    values = (first_name, last_name, email, mobile_number, year_of_entry, gender, dob, matric_no,department,faculty)
    messagebox.showinfo(title="success", message="student data updated succesfully")

    # MatricNo.set("")
    # Firstname.set("")
    # Lastname.set("")
    # Email.set("")
    # Mobilenumber.set("")
    # Yearofentry.set("")
    # Gender.set("")
    # DOB.set("")
    # Execute the query
    cursor.execute(update_query, values)
    conn.commit()
    
    show_all()




def search_records():
    search_value = search_by.get()

    if search_value:
        search_query = """
            SELECT * FROM students_guidb
            WHERE MatricNo = %s OR Firstname LIKE %s OR Lastname LIKE %s 
            OR Yearofentry = %s OR DEPARTMENT LIKE %s OR FACULTY LIKE %s
        """
        search_value_with_wildcards = f'%{search_value}%'
        cursor.execute(search_query, (
            search_value, search_value_with_wildcards, search_value_with_wildcards, 
            search_value, search_value_with_wildcards, search_value_with_wildcards
        ))
    
        records = cursor.fetchall()
        if len(records) != 0:
            student_table.delete(*student_table.get_children())
            for record in records:
                student_table.insert("", tkinter.END, values=record)
            conn.commit()
        else:
            messagebox.showerror("Error", "No records found for the entered value.")
    else:
        messagebox.showerror("Error", "Please enter a search value.")




    
#this is to display all of the clicked on information to the detail frame
def get_cursor(event):
     cursor_row=student_table.focus()
     content=student_table.item(cursor_row)
     row=content['values']
     MatricNo.set(row[0])
     Firstname.set(row[1])
     Lastname.set(row[2])
     Email.set(row[3])
     Mobilenumber.set(row[4])
     Yearofentry.set(row[5])
     Gender.set(row[6])
     DOB.set(row[7])


def delete_record():
    selected_item = student_table.selection()
    if not selected_item:
        return

    record_id = student_table.item(selected_item)["values"][0]  # Assuming MatricNo is the first column
    delete_query = "DELETE FROM students_guidb WHERE MatricNo = %s"
    cursor.execute(delete_query, (record_id,))
    messagebox.showinfo(title="success",message="student deleted successfully")
    
    conn.commit()
    clear()
    # messagebox.showwarning(title="ERROR!", message="student deleted successfully")

def logout():
    window.destroy()  # Close the student management window
    subprocess.run(["python", "login.py"])  # Import and run the login page code
    


background="white"
window.config(bg=background)
title_label=tkinter.Label(window,text="Student management system",bg="#57a1f8",font=("Microsoft Yahei UI Light",25),bd=7,relief=tkinter.GROOVE)
title_label.pack(side=tkinter.TOP,fill=tkinter.X)


detail_frame=tkinter.LabelFrame(window,text="Enter your details",font=("Microsoft Yahei UI Light",25),bg="#57a1f8",bd=7,relief=tkinter.GROOVE)
detail_frame.place(x=20, y=90,width=430,height=710)


data_frame=tkinter.Frame(window,bd=7,bg="#57a1f8",relief=tkinter.GROOVE)
data_frame.place(x=475,y=90,width=840,height=710)

# window.resizable(False,False)
#----------------------variables----------------------

MatricNo=tkinter.StringVar()
Firstname=tkinter.StringVar()
Lastname=tkinter.StringVar()
Email=tkinter.StringVar()
Mobilenumber=tkinter.StringVar()
Yearofentry=tkinter.StringVar()
Gender=tkinter.StringVar()
DOB=tkinter.StringVar()

search_by=tkinter.StringVar()
Faculty=tkinter.StringVar()
Department=tkinter.StringVar()




# ------------------------------entry field---------

# --------------matric-number--------------------

martic_no_lbl=tkinter.Label(detail_frame,text="Matric no:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
martic_no_lbl.grid(row=0,column=0,padx=20,pady=10)

martic_no_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=MatricNo)
martic_no_entry.grid(row=0,column=1,padx=20,pady=10)



# --------------first name--------------------
first_name_lbl=tkinter.Label(detail_frame,text="first name:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
first_name_lbl.grid(row=1,column=0,padx=20,pady=10)

first_name_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=Firstname)
first_name_entry.grid(row=1,column=1,padx=20,pady=10)



# --------------last name--------------------
last_name_lbl=tkinter.Label(detail_frame,text="last name:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
last_name_lbl.grid(row=2,column=0,padx=20,pady=10)

last_name_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=Lastname)
last_name_entry.grid(row=2,column=1,padx=20,pady=10)

# --------------email--------------------
Email_lbl=tkinter.Label(detail_frame,text="Email:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
Email_lbl.grid(row=3,column=0,padx=20,pady=10)



Email_entry = tk.Entry(detail_frame, bd=3, font=("Microsoft Yahei UI Light", 12), textvariable=Email, validate="key")

Email_entry.grid(row=3,column=1,padx=20,pady=10)




# --------------mobile-number--------------------
mobile_number_lbl=tkinter.Label(detail_frame,text="Mobile no:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
mobile_number_lbl.grid(row=4,column=0,padx=20,pady=10)

mobile_number_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=Mobilenumber)
mobile_number_entry.grid(row=4,column=1,padx=20,pady=10)

#------------------year of entry-----------------
year_of_Entry_lbl=tkinter.Label(detail_frame,text="Year of entry:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
year_of_Entry_lbl.grid(row=5,column=0,padx=20,pady=10)

year_of_Entry_combo=ttk.Combobox(detail_frame,width=27,textvariable=Yearofentry, values=["",2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023])
year_of_Entry_combo.grid( row=5 , column=1,padx=20,pady=10 )

#---------------------gender------------------------
gender_lbl=tkinter.Label(detail_frame,text="Gender:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
gender_lbl.grid(row=6,column=0,padx=20,pady=10)

gender_combo=ttk.Combobox(detail_frame,width=27,textvariable=Gender, values=[" ","Male","Female","Other"])
gender_combo.grid( row=6, column=1,padx=20,pady=10 )

#-----------------dob----------------------
date_of_birth_lbl=tkinter.Label(detail_frame,text="DOB:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
date_of_birth_lbl.grid(row=7,column=0,padx=20,pady=10)

date_of_birth_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=DOB)
date_of_birth_entry.grid(row=7,column=1,padx=20,pady=10)\


department_lbl=tkinter.Label(detail_frame,text="Department:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
department_lbl.grid(row=8,column=0,padx=20,pady=10)

department_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=Department)
department_entry.grid(row=8,column=1,padx=20,pady=10)


faculty_lbl=tkinter.Label(detail_frame,text="faculty:",font=("Microsoft Yahei UI Light",12),bg="#57a1f8")
faculty_lbl.grid(row=9,column=0,padx=20,pady=10)

faculty_entry=tkinter.Entry(detail_frame,bd=3,font=("Microsoft Yahei UI Light",12),textvariable=Faculty)
faculty_entry.grid(row=9,column=1,padx=20,pady=10)


#---------------------buttons-----------------
btn_frames=tkinter.Frame(detail_frame,bg="#57a1f8",bd=5,relief=tkinter.GROOVE)
btn_frames.place(x=90,y=500,width=240,height=105)


ADD_btn=tkinter.Button(btn_frames,bg="#57a1f8",text="ADD",bd=5,font=("Microsoft Yahei UI Light",12),width=10, command= click_me )
ADD_btn.grid(row=0,column=0,pady=2,padx=4)


Update_btn=tkinter.Button(btn_frames,bg="#57a1f8",text="UPDATE",bd=5,font=("Microsoft Yahei UI Light",12),width=10,command=update_data)
Update_btn.grid(row=0,column=1,pady=2,padx=4)

delete_btn=tkinter.Button(btn_frames,bg="#57a1f8",text="DELETE",bd=5,font=("Microsoft Yahei UI Light",12),width=10,command=delete_record)
delete_btn.grid(row=1,column=0,pady=4,padx=4)


clear_btn=tkinter.Button(btn_frames,bg="#57a1f8",text="RESET",bd=5,font=("Microsoft Yahei UI Light",12),width=10,command=reset)
clear_btn.grid(row=1,column=1,pady=4,padx=4)

#----------------------------search box---------

search_frame=tkinter.Frame(data_frame,bg="#333239",bd=5,relief=tkinter.GROOVE)
search_frame.pack(side=tkinter.TOP,fill=tkinter.X)



def on_enter(e):
    search_combo.delete(0, END)

def on_leave(e):
    name = search_combo.get()
    if name == "":
        search_combo.insert(0, "search matric no, firstname,lastname,year of entry")
search_combo=tkinter.Entry(search_frame, textvariable=search_by, width=35)
search_combo.grid(row=0,column=1,padx=10,pady=2)
search_combo.insert(0, "search MatricNo,Firstname,lastname,yearOfEntry")
search_combo.bind('<FocusIn>', on_enter)
search_combo.bind('<FocusOut>', on_leave)



search_btn=tkinter.Button(search_frame,text="Search",font=("Microsoft Yahei UI Light",13),bd=5,width=9,bg="#57a1f8", command=search_records)
search_btn.grid(row=0,column=2,padx=5,pady=2)


show_all_btn=tkinter.Button(search_frame,text="Show all",font=("Microsoft Yahei UI Light",13),bd=5,width=9,bg="#57a1f8",command=show_all)
show_all_btn.grid(row=0,column=3,padx=5,pady=2)

# show_all_tooltip = Tooltip(show_all_btn, "Click to show all records")

clear_btn=tkinter.Button(search_frame,text="clear",font=("Microsoft Yahei UI Light",13),bd=5,width=9,bg="#57a1f8",command=clear)
clear_btn.grid(row=0,column=4,padx=5,pady=2)

# Create the Logout button
logout_button = tkinter.Button(search_frame, text="Logout", bg="#57a1f8", font=("Microsoft Yahei UI Light", 12), bd=5, width=9, command=logout)
logout_button.grid(row=0, column=5, padx=5, pady=2)


#------------------data base frame------------------

database_frame=tkinter.Frame(data_frame,bg="#a29bbf",bd=8,relief=tkinter.GROOVE)
database_frame.pack(fill=tkinter.BOTH,expand=True)



#------------------------scroll bar-------------------------
y_scroll=tkinter.Scrollbar(database_frame,orient=tkinter.VERTICAL)
x_scroll=tkinter.Scrollbar(database_frame,orient=tkinter.HORIZONTAL)

student_table=ttk.Treeview(database_frame,columns=("MatricNo","Firstname","Lastname","Email","Mobilenumber","Yearofentry","Gender","DOB","department","faculty"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)


y_scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
x_scroll.pack(side=tkinter.BOTTOM,fill=tkinter.X)



student_table.heading("MatricNo", text="MatricNo" )
student_table.heading("Firstname", text="Firstname")
student_table.heading("Lastname", text="Lastname" )
student_table.heading("Email", text="Email")
student_table.heading("Mobilenumber", text="Mobilenumber")
student_table.heading("Yearofentry", text="Yearofentry")
student_table.heading("Gender", text="Gender")
student_table.heading("DOB", text="DOB")
student_table.heading("department", text="department")
student_table.heading("faculty", text="faculty")




student_table['show']= 'headings'

student_table.column("MatricNo",width=200, anchor="center")
student_table.column("Firstname",width=200,anchor="center")
student_table.column("Lastname",width=200,anchor="center")
student_table.column("Email",width=200,anchor="center")
student_table.column("Mobilenumber",width=200,anchor="center")
student_table.column("Yearofentry",width=100,anchor="center")
student_table.column("Gender",width=100,anchor="center")
student_table.column("DOB",width=200,anchor="center")
student_table.column("department",width=200,anchor="center")
student_table.column("faculty",width=200,anchor="center")


student_table.tag_configure('hover', background='lightblue')
  

hovered_row = None

def on_hover(event):
    global hovered_row
    # Remove the hover effect from the previous row
    if hovered_row:
        student_table.item(hovered_row, tags=())
    # Get the row under the cursor
    hovered_row = student_table.identify_row(event.y)
    if hovered_row:
        student_table.item(hovered_row, tags=('hover',))

student_table.bind('<Motion>', on_hover)




student_table.pack(fill=tkinter.BOTH,expand=True)

student_table.bind("<ButtonRelease-1>",get_cursor)

window.mainloop()