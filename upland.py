import requests
from tkinter import *

#Code
url = 'https://v6.exchangerate-api.com/v6/ee15a2956a8828023a294906/latest/USD'

response = requests.get(url)
data = response.json()

def get():
    upland_usd = root_dolls.get()
    upland_usd = float(upland_usd)

    upland_tax = 0.95

    usd_to_brl = data['conversion_rates']['BRL']

    usd_to_brl *= 0.95

    real = upland_usd * upland_tax * usd_to_brl

    result.delete(1.0,END)

    result.insert(INSERT,f"You're gonna get about {real:.2f} Reais")

#UI

def main():
    root = Tk()
    root.geometry("300x200")
    root.title("Calculadora")
    root.configure(background="#00A0D0")

    root_header = Label(text="How many dollars you have in Upland: ",font=("arial,",10),fg="black", bg="#00A0D0")
    root_header.place(x=30,y=15)
    root_dolls = Entry(root)
    root_dolls.place(x=90, y=40,height=30)

    result = Text(root,height=2,width=34,font=("arial",10),bd=0,bg="#00A0D0")
    result.place(x=30,y=120)


    button = Button(text='Clique aqui',command=get,bg="lightgrey")
    button.place(x=120, y=75,height=30,width=75)

    root.mainloop()

main()
