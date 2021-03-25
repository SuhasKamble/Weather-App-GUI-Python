from tkinter import *
import requests
from PIL import  Image,ImageTk
from pprint import pprint
API_Key = "828d39304bdf392ac629aae192aed9e8"
root = Tk()
temeraure_var = StringVar()
searchText = StringVar()
searchText.set("Search")

def getWeather():
    searchText.set("Loading...")
    query = cityInput.get()
    temeraure_var.set("")
    tempLabel = Label(root, text=temeraure_var, font="Ralway 30 bold", bg='#fff', fg='#6C63FF')
    if query:
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_Key}"
        print(base_url)
        weatherData = requests.get(base_url).json()
        name = weatherData['name']
        wData = weatherData['main']['temp']
        temeraure_var.set(wData)

        nameLabel = Label(root,text=name,font="Ralway 18 bold",bg='white',fg='#6C63FF')
        nameLabel.place(x=50,y=250)
        tempLabel.config(text=wData)

        tempLabel.place(x=50,y=290)
    else:

        temeraure_var.set("")
        tempLabel.config(text=temeraure_var)
        msgLabel = Label(root, text="Please Enter City", font="Ralway 18 bold", bg='white', fg='#6C63FF')
        msgLabel.place(x=50, y=250)
        msgLabel.after(10000 , lambda: msgLabel.destroy())
    searchText.set("Search")    



root.title("Weather App")
root.geometry('700x400')

img =Image.open("img.png")
img = img.resize((250, 250))
photo = ImageTk.PhotoImage(img)
label = Label(root,image=photo)
label.image = photo
label.place(x=430,y=60)



title = Label(root,text="Weather App",font="Ralway 22 ",bg='#fff')
title.place(x=10,y=10)

subTitle = Label(root,text="Enter a city",font="Ralway 16",bg='#fff')
subTitle.place(x=50,y=100)

cityName = StringVar()
cityInput = Entry(root,textvariable=cityName,font="Ralway 14 ",bg="#f2f2f2",borderwidth=1,relief=FLAT)
cityInput.place(x=50,y=140)
button = Button(root,textvariable=searchText,font="Ralway 12 bold", padx=10,bg="#6C63FF",fg="#fff",command=getWeather)
button.place(x=50,y=200)
root.config(bg='#fff')
root.mainloop()
