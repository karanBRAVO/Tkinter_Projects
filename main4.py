from tkinter import *

root = Tk()
root.geometry("455x389")
root.title("Stop watch")

f0 = Frame(root, bg="light blue")
f0.pack(fill="x", side="top")
heading = Label(f0, text="STOP WATCH", fg="white",
                bg='light blue', font="consolas 34 bold")
heading.pack()

run = False
hrs = 0
minutes = 0
sec = 0


def Start():
    global run
    run = True


def Pause():
    global run
    run = False


def Reset():
    global hrs, minutes, sec, run
    run = False
    hrs = 0
    minutes = 0
    sec = 0
    sec_label["text"] = f"{sec:02d}"
    min_label["text"] = f"{minutes:02d} :"
    hr_label["text"] = f"{hrs:02d} :"


def Lap():
    global hrs, minutes, sec
    frame_lap = Frame(root)
    frame_lap.pack(side="top")
    Label(frame_lap, text=f"{hrs:02d}:{minutes:02d}:{sec:02d}",
          fg="red", font="serif 10").pack()


def loop():
    global run, hrs, minutes, sec
    if run == True:
        sec += 1
        if sec == 60:
            sec = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hrs += 1
        sec_label["text"] = f"{sec:02d}"
        min_label["text"] = f"{minutes:02d} :"
        hr_label["text"] = f"{hrs:02d} :"
    root.after(1000, loop)


root.after(1000, loop)

f2 = Frame(root, pady=47)
f2.pack(side="top")
hr_label = Label(
    f2, text=f"{hrs:02d} :", font="serif 46 bold", padx=5, pady=6, justify='center')
hr_label.pack(side="left")
min_label = Label(f2, text=f"{minutes:02d} :",
                  font="serif 46 bold", padx=5, pady=6, justify='center')
min_label.pack(side="left")
sec_label = Label(
    f2, text=f"{sec:02d}", font="serif 46 bold", padx=5, pady=6, justify='center')
sec_label.pack(side="left")

f3 = Frame(root, pady=5, padx=4)
f3.pack(side="top")
Button(f3, text="Start", fg="light blue", padx=3, pady=4, bg="white", font="lucida 14",
       border=3, borderwidth=3, command=Start, width=6).pack(side="left", padx=10)
Button(f3, text="Pause", fg="light blue", padx=3, pady=4, bg="white", font="lucida 14",
       border=3, borderwidth=3, command=Pause, width=6).pack(side="left", padx=10)
Button(f3, text="Reset", fg="light blue", padx=3, pady=4, bg="white", font="lucida 14",
       border=3, borderwidth=3, command=Reset, width=6).pack(side="left", padx=10)
Button(f3, text="Lap", fg="light blue", padx=3, pady=4, bg="white", font="lucida 14",
       border=3, borderwidth=3, command=Lap, width=6).pack(side="left", padx=10)

root.mainloop()
