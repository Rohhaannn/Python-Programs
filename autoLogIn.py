from tkinter import *

def fun():
    def autologin():
        username.set("python.hub")
        password.set("123456")
        login_screen = tk()
        login_screen.title("Login")
        login_screen.geometry("300x250")

        Label(login_screen, text="Please enter login details").pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Username").pack()

        username = StringVar()
        password = StringVar()

        username_login_entry = Entry(login_screen, textvariable = username)
        username_login_entry.pack()

        l1 = Label(login_screen, text = "").pack()
        l2 = Label(login_screen, text = "Password").pack()

        password__login_entry = Entry(login_screen, textvariable = password)
        password__login_entry.pack()

        Label(login_screen, text="").pack()
        Button(login_screen, text = "Autofill id & pass", command = autologin).pack()

        Button(login_screen, text="Login", width = 10, height = 1).pack(pady = 10)
        login_screen.mainloop()

fun()
