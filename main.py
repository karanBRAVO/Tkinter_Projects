from tkinter import *


def main2():
    root = Tk()
    root.geometry("300x200")
    root.minsize(width=300, height=200)
    root.title("Login Window")

    defaultbg = root.cget('bg')

    f1 = Frame(root, bg="grey", pady=4)
    f1.pack(side=TOP, fill="x")
    f2 = Frame(root, bg=defaultbg, pady=14)
    f2.pack(side=TOP)
    f3 = Frame(root, bg=defaultbg, pady=14)
    f3.pack(side=TOP)
    f4 = Frame(root, bg=defaultbg, pady=3)
    f4.pack(side=TOP)

    heading = Label(f1, text="Login", font="Helvetica 15 bold", bg="grey", fg="white")
    heading.pack()

    user_name = Label(f2, text="Username", fg="black", padx=10)
    user_name.pack(side=LEFT)
    user_pass = Label(f3, text="Password", fg="black", padx=12)
    user_pass.pack(side=LEFT)


    def check():
        lst = []
        print("Checking...")
        with open("values.txt", 'r') as f:
            for line in f:
                for word in line.split():
                    lst.append(word)
            f.close()
        if user_name_entry.get() == lst[0] and user_pass_entry.get() == lst[1]:
            print("matched")
        elif user_name_entry.get() != lst[0] or user_pass_entry.get() != lst[1]:
            print("Not matched")


    user_name_value = StringVar()
    user_pass_value = StringVar()

    user_name_entry = Entry(f2, textvariable=user_name_value)
    user_name_entry.pack()
    user_pass_entry = Entry(f3, textvariable=user_pass_value)
    user_pass_entry.pack()

    Button(root, text="Login", bg="light grey", fg="black", height=1, width=8, font="serif 10", pady=5, command=check).pack()

    root.mainloop()


def main1():
    root = Tk()
    root.geometry("300x300")
    root.minsize(width=300, height=300)
    root.maxsize(width=300, height=300)

    root.title("Sign Up Window")

    defaultbg = root.cget('bg')

    f1 = Frame(root, bg="grey")
    f1.pack(side=TOP, fill="x")
    f2 = Frame(root, bg=defaultbg)
    f2.pack(side=TOP)
    f3 = Frame(root, bg=defaultbg)
    f3.pack(side=TOP)
    f4 = Frame(root, bg=defaultbg)
    f4.pack(side=TOP)
    f5 = Frame(root, bg=defaultbg)
    f5.pack(side=TOP)

    heading = Label(f1, text="Sign In", font="fantasy 15 bold", fg="white", bg="grey", padx=20, pady=10)
    heading.pack()
    Button(text="Already signed in LOGIN.", pady=5, cursor="target", command=main2).pack()

    user_id = Label(f2, text="Username", fg="black", bg=defaultbg, padx=4, pady=10)
    user_id.pack(side=LEFT)
    user_password = Label(f3, text="Password", fg="black", bg=defaultbg, padx=6, pady=10)
    user_password.pack(side=LEFT)


    def storeValues():
        global run

        with open("values.txt", 'w') as f:
            f.write(f"{user_id_value.get()}\n")
            f.write(f"{user_password_value.get()}")
            f.close()
            Label(pady=5, text="SIGNED IN SUCCESSFULLY", fg="green").pack()


    user_id_value = StringVar()
    user_password_value = StringVar()
    user_remember_value = IntVar()

    user_id_entry = Entry(f2, textvariable=user_id_value, width=19)
    user_id_entry.pack(side=LEFT)
    user_password_entry = Entry(f3, textvariable=user_password_value, width=19)
    user_password_entry.pack(side=LEFT)
    user_rememberMe = Checkbutton(f4, text="Remember me", variable=user_remember_value)
    user_rememberMe.pack()

    Button(f5, text="Sign In", fg="black", bg="light grey", padx=16, borderwidth=3, border=3, command=storeValues).pack(pady=15)

    root.mainloop()


main1()
