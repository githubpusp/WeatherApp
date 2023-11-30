from tkinter import *
from tkinter import ttk
import requests


def get_data():
    state = state_name.get()
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + state + "&appid=45f107a04bd0ab1d91c4d735cff7bab1").json()
    wc_lebel1.config(text=data["weather"][0]["main"])
    wd_lebel1.config(text=data["weather"][0]["description"])
    temp_lebel1.config(text=str(int(data["main"]["temp"] - 273.15)))
    pressure_lebel1.config(text=data["main"]["pressure"])


win = Tk()  # display the root window and manage the other parameters of tinker application

win.title('Weather App')
win.config(bg="sky blue")
win.geometry("500x520")

name_lebel = Label(win, text="Weather App", font=("Times New Roman", 40, "bold"))
name_lebel.place(x=25, y=25, height=60, width=450)

list = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
        "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
        "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
        "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
        "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
        "Puducherry"]

state_name = StringVar()
com = ttk.Combobox(win, values=list, font=("Times New Roman", 25), textvariable=state_name)
com.place(x=30, y=115, height=50, width=450)

wc_lebel = Label(win, text="Weather Climate", font=("Times New Roman", 20))
wc_lebel.place(x=25, y=275, height=40, width=210)
wc_lebel1 = Label(win, text="", font=("Times New Roman", 20))
wc_lebel1.place(x=245, y=275, height=40, width=210)

wd_lebel = Label(win, text="Weather Description", font=("Times New Roman", 19))
wd_lebel.place(x=25, y=333, height=40, width=210)
wd_lebel1 = Label(win, text="", font=("Times New Roman", 19))
wd_lebel1.place(x=245, y=333, height=40, width=210)

temp_lebel = Label(win, text="Temperature(°C)", font=("Times New Roman", 19))
temp_lebel.place(x=25, y=393, height=35, width=210)
temp_lebel1 = Label(win, text="", font=("Times New Roman", 19))
temp_lebel1.place(x=245, y=393, height=35, width=210)

pressure_lebel = Label(win, text="Weather description", font=("Times New Roman", 19))
pressure_lebel.place(x=25, y=448, height=40, width=210)
pressure_lebel1 = Label(win, text="", font=("Times New Roman", 19))
pressure_lebel1.place(x=245, y=448, height=40, width=210)

done = Button(win, text="DONE", font=("Times New Roman", 25), command=get_data)
done.place(x=200, y=195, height=50, width=100)

win.mainloop()  # run all tinker loop
