from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("498x390")
root.minsize(width=498, height=50)
root.maxsize(width=498, height=390)
root.title("Timer")

f0 = Frame(root, bg="pink")
f0.pack(side="top", fill="x")
heading = Label(f0, text="TIMER", fg="white",
                bg="pink", font="calibri 29 bold")
heading.pack()

hrs = 0
minutes = 0
sec = 0
run = False


def inc_hrs():
    global hrs
    hrs += 1
    if hrs > 24:
        hrs = 0
    hrs_label['text'] = f"{hrs:02d}:"
    hours_label['text'] = f"{hrs:02d}:"


def dec_hrs():
    global hrs
    hrs -= 1
    if hrs < 0:
        hrs = 24
    hrs_label['text'] = f"{hrs:02d}:"
    hours_label['text'] = f"{hrs:02d}:"


def inc_min():
    global minutes
    minutes += 1
    if minutes > 60:
        minutes = 0
    min_label['text'] = f"{minutes:02d}:"
    minutes_label['text'] = f"{minutes:02d}:"


def dec_min():
    global minutes
    minutes -= 1
    if minutes < 0:
        minutes = 60
    min_label['text'] = f"{minutes:02d}:"
    minutes_label['text'] = f"{minutes:02d}:"


def inc_sec():
    global sec
    sec += 1
    if sec > 60:
        sec = 0
    sec_label['text'] = f"{sec:02d}"
    seconds_label['text'] = f"{sec:02d}"


def dec_sec():
    global sec
    sec -= 1
    if sec < 0:
        sec = 60
    sec_label['text'] = f"{sec:02d}"
    seconds_label['text'] = f"{sec:02d}"


def Start():
    global run
    f1.destroy()
    f2.destroy()
    f3.destroy()
    f4.destroy()
    run = True
    root.after(1000, loop())


# set timer
f1 = Frame(root, pady=30)
f1.pack(side="top")
hrs_label = Label(f1, text=f"{hrs:02d}:", fg="black", font="Aerial 47 bold")
hrs_label.pack(side="left")
min_label = Label(f1, text=f"{minutes:02d}:",
                  fg="black", font="Aerial 47 bold")
min_label.pack(side="left")
sec_label = Label(f1, text=f"{sec:02d}", fg="black", font="Aerial 47 bold")
sec_label.pack(side="left")

f2 = Frame(root, pady=3)
f2.pack(side="top")
f3 = Frame(root, pady=3)
f3.pack(side="top")
Button(f2, text="Inc_Hrs", width=7, bg="white", fg="pink", activebackground="pink",
       border=2, borderwidth=2, padx=2, pady=2, command=inc_hrs).pack(side="left", padx=26)
Button(f3, text="Dec_Hrs", width=7, bg="white", fg="pink", activebackground="pink",
       border=2, borderwidth=2, padx=2, pady=2, command=dec_hrs).pack(side="left", padx=26)
Button(f2, text="Inc_Min", width=7, bg="white", fg="pink", activebackground="pink",
       border=2, borderwidth=2, padx=2, pady=2, command=inc_min).pack(side="left", padx=26)
Button(f3, text="Dec_Min", width=7, bg="white", fg="pink", activebackground="pink",
       border=2, borderwidth=2, padx=2, pady=2, command=dec_min).pack(side="left", padx=26)
Button(f2, text="Inc_Sec", width=7, bg="white", fg="pink", activebackground="pink",
       border=2, borderwidth=2, padx=2, pady=2, command=inc_sec).pack(side="left", padx=26)
Button(f3, text="Dec_Sec", width=7, bg="white", fg="pink", activebackground="pink",
       border=2, borderwidth=2, padx=2, pady=2, command=dec_sec).pack(side="left", padx=26)

f4 = Frame(root, pady=26)
f4.pack(side="top")
Button(f4, text="Start", font="lucida 18", bg="white", fg="pink", width=5,
       height=1, pady=3, padx=3, border=3, borderwidth=3, command=Start).pack()


def loop():
    global sec, minutes, hrs, run
    while run == True:
        if sec == 0 and minutes == 0 and hrs == 0:
            run = False
        else:
            if minutes <= 0:
                if hrs > 0:
                    hrs -= 1
                    minutes = 60
            if sec <= 0:
                if minutes > 0:
                    minutes -= 1
                    sec = 60
            sec -= 1
            hours_label['text'] = f"{hrs:02d}:"
            minutes_label['text'] = f"{minutes:02d}:"
            seconds_label['text'] = f"{sec:02d}"
            if sec == 0 and minutes == 0 and hrs == 0:
                messagebox.showinfo("Message", "Time is up.")
            root.update()
            time.sleep(1)


def resume():
    global run
    run = True
    loop()


def pause():
    global run
    run = False


def cancel():
    pass


# timer starts
f5 = Frame(root, pady=47)
f5.pack(side="top")
hours_label = Label(f5, text=f"{hrs:02d}:",
                    fg="red", font="sans-serif 47 bold")
hours_label.pack(side="left")
minutes_label = Label(f5, text=f"{minutes:02d}:",
                      fg="red", font="sans-serif 47 bold")
minutes_label.pack(side="left")
seconds_label = Label(f5, text=f"{sec:02d}",
                      fg="red", font="sans-serif 47 bold")
seconds_label.pack(side="left")

f6 = Frame(root, pady=4)
f6.pack(side="top")
Button(f6, text="Pause", font="Helvetica 14 bold", command=pause, width=6, border=3, borderwidth=3,
       fg="pink", bg="white", activebackground="pink", padx=3, pady=4).pack(side="left", padx=15)
Button(f6, text="Resume", font="Helvetica 14 bold", command=resume, width=6, border=3, borderwidth=3,
       fg="pink", bg="white", activebackground="pink", padx=3, pady=4).pack(side="left", padx=15)
Button(f6, text="Cancel", font="Helvetica 14 bold", command=cancel, width=6, border=3, borderwidth=3,
       fg="pink", bg="white", activebackground="pink", padx=3, pady=4).pack(side="left", padx=15)

root.mainloop()
