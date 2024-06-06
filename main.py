from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# find password
def find_password():
    website_name = website_entry.get()

    try:
        with open("data.json", mode="r") as data_file:
            information = json.load(data_file)
    except FileNotFoundError:
        print("create a file first")
    else:
        with open("data.json", mode="r") as data_file:
            information = json.load(data_file)
            if website_name in information:
                website_info = information[website_name]
                messagebox.showinfo(title=f"{website_name}", message=f"{website_info}")

            else:
                messagebox.showinfo(title="Error", message="No details for the website exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "username": username,
            "password": password,
        }
    }
    messagebox.showinfo(title=f"{website_name}", message=f"username/email: {username}\n"
                                                         f"password: {password}")
    # messagebox.askyesno(title="verify", message=f"Are these verified and valid information\n{website_name}\n"
    #                                           f"{username}\n{password}")
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure to fill all the fields")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # update data

        else:
            data.update(new_data)
            # to write the data open the file in write mode
            with open("data.json", mode="w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("arial", 8, "bold"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=30)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "yash@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.focus()
password_entry.grid(row=3, column=1, columnspan=2)

generate_password_button = Button()
generate_password_button.config(text="Generate password", font=("arial", 8, "bold"))
generate_password_button.grid(row=3, column=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=3)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()
