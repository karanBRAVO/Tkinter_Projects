from tkinter import *

root = Tk()
root.title("Window Resizer GUI")

width = 300
height = 300
root.geometry(f"{width}x{height}")
root.minsize(width=width, height=height)
root.maxsize(width=width, height=height)

def change():
    width = width_value.get()
    height = height_value.get()
    if width < 300:
        width = 300
    if height < 300:
        height = 300
    root.geometry(f"{width}x{height}")
    root.minsize(width=width, height=height)
    root.maxsize(width=width, height=height)

f0 = Frame(root, bg="grey")
f0.pack(side="top", fill='x')
Label(f0, text="Tkinter GUI", font="consolas 16 bold", fg="white", bg="grey").pack()

width_value = IntVar()
height_value = IntVar()

f1 = Frame(root, pady=height//30)
f1.pack(side="top")
Label(f1, text="Width:", fg="black", font="fantasy 10 bold").pack(side="left")
width_entry = Entry(f1, width=width//20, textvariable=width_value)
width_entry.pack(side="left")

f2 = Frame(root, pady=height//30)
f2.pack(side="top")
Label(f2, text="Height:", fg="black", font="fantasy 10 bold").pack(side="left")
height_entry = Entry(f2, width=width//20, textvariable=height_value)
height_entry.pack(side="left")

Button(root, text="Apply", bg="light grey", fg="black", font="serif 10", padx=5, pady=4, command=change).pack()

root.mainloop()