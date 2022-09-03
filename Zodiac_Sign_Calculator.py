from tkinter import *

root = Tk()
root.title("ZODIAC SIGN CALCULATOR BY JOHN MARTIN")
root.geometry("440x325")
root.configure(bg="white")

result = Label(root, bg="white")
result.grid(row=4, column=0, columnspan=2)

def get_zodiac(date, month):
    global result
    result.grid_forget()
    date = int(entry1.get())
    month = int(entry2.get())

    if (month == 3 and date >= 21) or (month == 4 and date < 20):
        result = Label(root, text="YOUR ZODIAC SIGN IS ARIES", borderwidth=12, bg="red")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 4 and date >= 20) or (month == 5 and date < 21):
        result = Label(root, text="YOUR ZODIAC SIGN IS TAURUS", borderwidth=12, bg="green")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 5 and date >= 21) or (month == 6 and date < 21):
        result = Label(root, text="YOUR ZODIAC SIGN IS GEMINI", borderwidth=12, bg="yellow")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 6 and date >= 21) or (month == 7 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS CANCER", borderwidth=12, bg="silver")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 7 and date >= 23) or (month == 8 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS LEO", borderwidth=12, bg="orange")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 8 and date >= 23) or (month == 9 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS VIRGO", borderwidth=12, bg="brown")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 9 and date >= 23) or (month == 10 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS LIBRA", borderwidth=12, bg="pink")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 10 and date >= 23) or (month == 11 and date < 22):
        result = Label(root, text="YOUR ZODIAC SIGN IS SCORPIO", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 11 and date >= 22) or (month == 12 and date < 22):
        result = Label(root, text="YOUR ZODIAC SIGN IS SAGITTARIUS", borderwidth=12, bg="purple")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 12 and date >= 22) or (month == 12 and date < 20):
        result = Label(root, text="YOUR ZODIAC SIGN IS CAPRICORN", borderwidth=12, bg="grey")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 1 and date >= 20) or (month == 2 and date < 19):
        result = Label(root, text="YOUR ZODIAC SIGN IS AQUARIUS", borderwidth=12, bg="blue")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    elif (month == 2 and date >= 19) or (month == 3 and date < 21):
        result = Label(root, text="YOUR ZODIAC SIGN IS PISCES", borderwidth=12, bg="lime")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)
    else:
        result = Label(root, text="YOUR INPUTS ARE FALSE", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)


label1 = Label(root, text="WELCOME TO THE ZODIAC SIGN CALCULATOR", borderwidth=20, bg="black", fg="white")
label1.config(font=("Britannic Bold", 15))
label1.grid(row=0, column=0, columnspan=2)
label2 = Label(root, text="BIRTH DATE:", borderwidth=25, bg="white")
label2.config(font=("Britannic Bold", 20))
label2.grid(row=1, column=0)
label3 = Label(root, text="BIRTH MONTH:", borderwidth=25, bg="white")
label3.config(font=("Britannic Bold", 20))
label3.grid(row=2, column=0)

entry1 = Entry(root, borderwidth=3, width=7)
entry1.grid(row=1, column=1)
entry2 = Entry(root, borderwidth=3, width=7)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)

date = entry1.get()
month = entry2.get()

get_button = Button(root, text="KNOW YOUR ZODIAC SIGN", anchor=CENTER, command=lambda:get_zodiac(date, month), height=2, width=20, bg="black", fg="white")
get_button.grid(row=3, column=0, columnspan=2)

root.mainloop()





