from tkinter import *
from tkinter import ttk
import requests

def city_keys():
  city = city_name.get()
  data = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=d78f79a69d66be56aeb228cfe35bc552').json()
  pressure.config(text=data['main']['pressure'])
  temp.config(text=str(data['main']['temp']-273.15))
  climate.config(text=data['weather'][0]['description'])
  humidity.config(text=data['main']['humidity'])

def window_exit():
  wea.destroy()


wea = Tk()
wea.title(' ##### WEATHER #####')
wea.geometry('500x500')
wea.config(bg='black')

wl = Label(text="WEATHER",bg='blue',fg='white',font=('Times',30,'bold'))
wl.place(x=130,y=40,height=40,width=250)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com =ttk.Combobox(wea,text='WEATHER',values = list_name,font=('Times',10,'bold'),textvariable=city_name)
com.place(x=155,y=100,height=30,width=200)

Label(wea,text='TEMPRATURE',font=('Times',13)).place(x = 100,y =210,height=30,width=112)

Label(wea,text='PRESSURE',font=('Times',13)).place(x = 100,y =250,height=30,width=112)

Label(wea,text='WEATHER',font=('Times',13)).place(x = 100,y =290,height=30,width=112)

Label(wea,text=',HUMIDITY',font =('Times',13)).place(x=100,y=330,height=30,width=112)

temp = Label(wea,text='',font=('Times',13))
temp.place(x = 300,y =210)

pressure = Label(wea,text='',font=('Times',13))
pressure.place(x = 300,y =250)

climate = Label(wea,text='',font=('Times',13))
climate.place(x = 300,y =290)

humidity =Label(wea,text='',font=('Times',13))
humidity.place(x=300,y=330)

DONE_button = Button(text='DONE',font=('Times',20,'bold'),bg='yellow',command=city_keys).place(x = 200,y = 150,height=40,width=100)


EXIT_button = Button(text='EXIT',font=('Times',20,'bold'),bg='red',command=window_exit).place(x=200,y=420,height=40,width=100)

wea.mainloop()
