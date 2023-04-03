import mysql.connector
from tkinter import *
from tkinter import messagebox

class Signin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign In")
        self.root.geometry("200x200")
        self.root.configure(bg="#2C2F33")

        self.label_nickname = Label(self.root, text="Nickname", fg="#FFFFFF", bg="#2C2F33")
        self.label_nickname.pack()
        self.entry_nickname = Entry(self.root)
        self.entry_nickname.pack()

        self.label_password = Label(self.root, text="Password", fg="#FFFFFF", bg="#2C2F33")
        self.label_password.pack()
        self.entry_password = Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_signin = Button(self.root, text="Sign In", command=self.signin, bg="#7b90db", fg="#FFFFFF")
        self.button_signin.pack(pady=10)

    def signin(self):
        nickname = self.entry_nickname.get()
        password = self.entry_password.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root", # votre username BBD
            password="8520", # votre mdp BBD
            database="myDiscord"
        )

        mycursor = mydb.cursor()

        sql = "SELECT * FROM users WHERE nickname = %s AND password = %s"
        val = (nickname, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result is not None:
            messagebox.showinfo("Success", "You have been signed in!")
            self.root.destroy()

        else:
            messagebox.showerror("Error", "Invalid nickname or password")