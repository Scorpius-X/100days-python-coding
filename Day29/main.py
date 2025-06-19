from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    password_list = [choice(letters) for char in range(randint(8,10))]
    password_list += [choice(numbers) for char in range(randint(2,4))]
    password_list += [choice(symbols) for char in range(randint(2,4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

def find_password():
    website = website_input.get()
    try:
        with open("100days-python-coding/Day29/data.json", "r") as datafile:
            new_file = json.load(datafile)
            if website in new_file:
                email = new_file[website]["email"]
                password = new_file[website]["password"]
                messagebox.showinfo(title= website, message= f"Email: {email}\nPassword: {password}")
            
            else:
                messagebox.showinfo(title="Website not found", message= "No details for the website exist")
    except FileNotFoundError:
        messagebox.showinfo(title= "FILE NOT FOUND", message= "NO DATA FILE FOUND")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
         website:{
              "email": email,
              "password": password,
         }
                }

    
    if not website or not password:
        messagebox.showinfo(title= 'Oops', message= "Please don't leave any fields empty!")
        
    else:
        try:
            with open("100days-python-coding/Day29/data.json", "r") as datafile:
                #reading old data
                new_file = json.load(datafile)
                #updating old data
                new_file.update(new_data)
                
        except FileNotFoundError:
            print("file needs to be created first")
            with open("100days-python-coding/Day29/data.json", "w") as datafile:
                json.dump(new_data, datafile, indent= 4)

        else: 
            with open("100days-python-coding/Day29/data.json", "w") as datafile:
                #saving updated data
                json.dump(new_file, datafile, indent= 4)

        finally:
            website_input.delete(0,"end")
            password_input.delete(0,"end")
        
            
        


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx= 50, pady= 50)

#canvas

canvas = Canvas(width= 200, height= 200)
password_img = PhotoImage(file= "100days-python-coding/Day29/logo.png")
canvas.create_image(100,100, image = password_img)
canvas.grid(column= 1, row= 0)


#labels
website_label = Label(text= "Website:")
website_label.grid(column= 0, row= 1)

email_label = Label(text= "Email/Username:")
email_label.grid(column= 0, row= 2)

password_label = Label(text= "Password:")
password_label.grid(column=0 , row= 3)

#entries
website_input = Entry(width= 32)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width= 50)
email_input.grid(row= 2, column= 1, columnspan = 2)
email_input.insert(0, "eric.bolade@gmail.com")

password_input = Entry(width= 32)
password_input.grid(row= 3, column= 1)


#buttons
generate_button = Button(text= "Generate password", command= generate_password)
generate_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", width= 43, command= save_password)
add_button.grid(column= 1, row= 4, columnspan= 2)

search_button = Button(text="Search", width= 14, command= find_password)
search_button.grid(row= 1, column= 2)



windows.mainloop()