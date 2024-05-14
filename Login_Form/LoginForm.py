from tkinter import *
from tkinter import messagebox


class LoginForm:
    window = Tk()
    window.title("Sign Up Form")
    window.geometry("600x600")
    window.config(bg="#333333")

    login_frame = Frame(window, bg="#333333")
    login_frame.pack()

    sign_up_frame = Frame(window, bg="#333333")
    sign_up_frame.pack()

    name_entry = ""
    email_entry = ""
    contact_entry = ""
    password_entry = ""

    email_checker = ""
    password_checker = ""

    def __init__(self):
        pass

    def signup(self):

        # Implement the widgets
        intro_label = Label(self.sign_up_frame, text="  Welcome", bg="#333333", fg="#EE1289",
                            font=("algerian", 30, "bold"), height=3)
        name_label = Label(self.sign_up_frame, text="Name", bg="#333333", fg="white",
                           font=("times new roman", 15))
        self.name_entry = Entry(self.sign_up_frame, font=("times new roman", 15))
        email_label = Label(self.sign_up_frame, text="Email-ID", bg="#333333", fg="white",
                            font=("times new roman", 15), height=2)
        self.email_entry = Entry(self.sign_up_frame, font=("times new roman", 15))
        contact_label = Label(self.sign_up_frame, text="Contact", bg="#333333", fg="white",
                              font=("times new roman", 15))
        self.contact_entry = Entry(self.sign_up_frame, font=("times new roman", 15))
        password_label = Label(self.sign_up_frame, text="Password ", bg="#333333", fg="white",
                               font=("times new roman", 15), height=2)
        self.password_entry = Entry(self.sign_up_frame, font=("times new roman", 15), show="*")
        button = Button(self.sign_up_frame, text="click", bg="#333333", fg="white",
                        font=("times new roman", 14), height=1, width=8, command=self.sign_up_popup)

        # Mount the widgets
        intro_label.grid(row=0, column=0, columnspan=2)
        name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1)
        contact_label.grid(row=3, column=0)
        self.contact_entry.grid(row=3, column=1)
        password_label.grid(row=4, column=0)
        self.password_entry.grid(row=4, column=1)
        button.grid(row=5, column=0, columnspan=2)

        self.window.mainloop()

    def sign_up_popup(self):

        # Implement the warnings popup in case some field is missing
        if self.name_entry.get() == "":
            messagebox.showwarning(title="Form says", message="Fill the name field")
        elif self.email_entry.get() == "":
            messagebox.showwarning(title="Form says", message="Fill the email field")
        elif self.contact_entry.get() == "":
            messagebox.showwarning(title="Form says", message="Fill the contact field")
        elif self.password_entry.get() == "":
            messagebox.showwarning(title="Form says", message="Fill the password field")

        # Implement the errors popup
        elif self.email_entry.get().count("@gmail.com") < 1:
            messagebox.showerror(title="Form says", message="Enter proper password\n\nSample - ****@gmail.com")
        elif len(self.contact_entry.get()) < 10 or not self.contact_entry.get().isnumeric():
            messagebox.showerror(title="Form says", message="Provide proper contact number")
        elif len(self.password_entry.get()) <= 6:
            messagebox.showerror(title="Form says", message="Password is too short\n\nPassword length must be "
                                                            "greater than 6")

        # Implement the popup for successful sign-up

        else:
            self.email_checker = self.email_entry.get().lower()
            self.password_checker = self.password_entry.get()
            messagebox.showinfo(title="This Form says", message="Sign up status: Success\n\nRedirect to login portal")
            self.sign_up_frame.destroy()
            self.login_page()

    def login_page(self):

        login_frame = Frame(self.window, bg="#333333")
        login_frame.pack()

        intro_label = Label(self.login_frame, text="  Welcome again", bg="#333333", fg="#EE1289",
                            font=("algerian", 30, "bold"), height=3)
        email_label = Label(self.login_frame, text="Email-ID", bg="#333333", fg="white",
                            font=("times new roman", 15), height=2)
        self.email_entry = Entry(self.login_frame, font=("times new roman", 15))
        password_label = Label(self.login_frame, text="Password", bg="#333333", fg="white",
                               font=("times new roman", 15), height=2)
        self.password_entry = Entry(self.login_frame, font=("times new roman", 15), show="*")
        button = Button(self.login_frame, text="Verify", bg="#333333", fg="white",
                        font=("times new roman", 14), height=1, width=8, command=self.login_popup)

        intro_label.grid(row=0, column=0, columnspan=2)
        email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1)
        button.grid(row=3, column=1, columnspan=2)

        self.window.mainloop()

    def login_popup(self):
        if self.email_checker != self.email_entry.get():
            messagebox.showerror(title="Form says", message="Email-ID not match")
        elif self.password_checker != self.password_entry.get():
            messagebox.showerror(title="Form says", message="Password not match")

        else:
            messagebox.showinfo(title="Form says", message="Login successful")
            self.login_frame.destroy()
            self.window.destroy()


obj = LoginForm()
obj.signup()
