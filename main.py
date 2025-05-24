from tkinter import * 
from tkinter.ttk import *
from tkinter import Button,Entry,Text,Label,Spinbox,Scale,Checkbutton,Grid
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letter + password_number + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    pass_inp.delete(0,END)
    pass_inp.insert(0,password)
    

    # print(f"Your password is: {password}") ## it will show pass in terminal

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_inp.get()
    email = email_inp.get()
    password = pass_inp.get()

#  REMOVING EMPTY SPACE FROM THE TEXT TO IMPOROVE EFFICIENCY AND DATA STORING.
    # web = len(website.replace(" ", ""))
    website = website.replace(" ", "")
    email = email.replace(" ", "")
    password = password.replace(" ", "")


    if len(email) == 0 or len(website) == 0 :
        messagebox.showinfo(title="Title",message="Please Don't leave the field empty")
    elif len(password) < 7 :
        messagebox.showinfo(title="PassWord",message="PassWord is Less than 8 char ")
    else:
        is_ok = messagebox.askokcancel(title=window,message=f"These are the detailed entered here \nEmail:{email}\nWebsite:{website}\nPassword: {password}\nAre U OKY to SAVE y/n ?")
        if is_ok :
            with open("TKINTER/Password Manager/data.csv",'a') as data_file:
                data_file.write(f"{website},{email},{password}\n")
                web_inp.delete(0,END)
                email_inp.delete(0,END)
                pass_inp.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PassWord Manager")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20) # It will arrange the windows padding

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="TKINTER/Password Manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# ALL Label
web_lbl = Label(window, text="Website: ",font=("Times New Roman",14))
email_lbl = Label(window,text="Email/ Username: ",font=("Times New Roman",14))
pass_lbl = Label(window, text="Password:",font=("Times New Roman",14))
extra = Label(window,text="*Empty Space Should Not Be Count / It will Skip")

web_lbl.grid(row=2)
email_lbl.grid(row=3)
pass_lbl.grid(row=4)
extra.grid(row=1,column=1)

# Entey Button __TEXT__  

web_inp = Entry(width = 36)
web_inp.grid(row=2,column=1,columnspan=2)

email_inp = Entry(width = 36)
email_inp.grid(row=3,column=1,columnspan=2)

pass_inp = Entry(width = 36)
pass_inp.grid(row=4,column=1,columnspan=2)

#BUTTON 
button = Button(text= "Generate Password ",command=generatepass)
button.grid(row = 4, column = 2,columnspan=1)
button = Button(text= "Add",width=31,command=save)
button.grid(row = 5, column = 1,columnspan=3)

window.mainloop()