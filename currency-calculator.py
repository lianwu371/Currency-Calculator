import tkinter as tk
from tkinter import *
import requests
import pandas as pd
import sys


root = Tk()
root.title("Currency Calculator")

data = requests.get('https://api.exchangeratesapi.io/latest').json()
currencies = data['rates']

#need to define a function that updates the currencies

countrycode1 = StringVar()
countrycode2 = StringVar()
finalamount = tk.IntVar()
countrycode1.set("")
countrycode2.set("")
finalamount.set("")

#Main buttons

#Labels
greetings_label = Label(root, text = "Welcome to Real Time Currency Convertor",  fg = 'blue', relief = tk.RAISED, borderwidth = 2)
from_currency_label = Label(root, textvariable=countrycode1,relief = tk.SUNKEN)
to_currency_label = Label(root, textvariable=countrycode2,relief = tk.SUNKEN)
date_label = Label(root, text = data['date'], borderwidth = 5)
to_currency_label_amount = Label(root, textvariable=finalamount,relief = tk.RIDGE)

#label placement
greetings_label.grid(row=0,column=0,columnspan=4)
from_currency_label.grid(row=1,column=0)
to_currency_label.grid(row=1,column=3)
date_label.grid(row=1,column=1,columnspan=2)
to_currency_label_amount.grid(row=2,column=3)
#Entries amount you want to convert

amount = Entry(root, bd=2 , relief=tk.RIDGE, justify=tk.CENTER, borderwidth=6,width=10)
#place buttons

amount.grid(row=2,column=0)

#Define button function

def currency_click(countrycode):
	#update the label field
	global countrycode1, countrycode2
	if len(countrycode1.get()) == 0:
		countrycode1.set(countrycode)
	else:
		countrycode2.set(countrycode)


def button_clear():
	amount.delete(0, END)
	countrycode1.set("")
	countrycode2.set("")
	finalamount.set("")

def convert():
	value = float(amount.get())

	if countrycode1.get() != "EUR":
		value = value / currencies[countrycode1.get()]
	value = round(value*currencies[countrycode2.get()],4)
	finalamount.set(value)

#Define all the buttons and their locations

#Currency Labels
button_CAD = Button(root, text="CAD",padx=20,pady=10,command=lambda:currency_click("CAD"))
button_HKD = Button(root, text="HKD",padx=20,pady=10,command=lambda:currency_click("HKD"))
button_ISK = Button(root, text="ISK",padx=20,pady=10,command=lambda:currency_click("ISK"))
button_PHP = Button(root, text="PHP",padx=20,pady=10,command=lambda:currency_click("PHP"))
button_DKK = Button(root, text="DKK",padx=20,pady=10,command=lambda:currency_click("DKK"))
button_HUF = Button(root, text="HUF",padx=20,pady=10,command=lambda:currency_click("HUF"))
button_CZK = Button(root, text="CZK",padx=20,pady=10,command=lambda:currency_click("CZK"))
button_AUD = Button(root, text="AUD",padx=20,pady=10,command=lambda:currency_click("AUD"))
button_RON = Button(root, text="RON",padx=20,pady=10,command=lambda:currency_click("RON"))
button_SEK = Button(root, text="SEK",padx=20,pady=10,command=lambda:currency_click("SEK"))
button_IDR = Button(root, text="IDR",padx=20,pady=10,command=lambda:currency_click("IDR"))
button_INR = Button(root, text="INR",padx=20,pady=10,command=lambda:currency_click("INR"))
button_BRL = Button(root, text="BRL",padx=20,pady=10,command=lambda:currency_click("BRL"))
button_RUB = Button(root, text="RUB",padx=20,pady=10,command=lambda:currency_click("RUB"))
button_HRK = Button(root, text="HRK",padx=20,pady=10,command=lambda:currency_click("HRK"))
button_JPY = Button(root, text="JPY",padx=20,pady=10,command=lambda:currency_click("JPY"))
button_THB = Button(root, text="THB",padx=20,pady=10,command=lambda:currency_click("THB"))
button_CHF = Button(root, text="CHF",padx=20,pady=10,command=lambda:currency_click("CHF"))
button_SGD = Button(root, text="SGD",padx=20,pady=10,command=lambda:currency_click("SGD"))
button_PLN = Button(root, text="PLN",padx=20,pady=10,command=lambda:currency_click("PLN"))
button_BGN = Button(root, text="BGN",padx=20,pady=10,command=lambda:currency_click("BGN"))
button_TRY = Button(root, text="TRY",padx=20,pady=10,command=lambda:currency_click("TRY"))
button_CNY = Button(root, text="CNY",padx=20,pady=10,command=lambda:currency_click("CNY"))
button_NOK = Button(root, text="NOK",padx=20,pady=10,command=lambda:currency_click("NOK"))
button_ZAR = Button(root, text="ZAR",padx=20,pady=10,command=lambda:currency_click("ZAR"))
button_USD = Button(root, text="USD",padx=20,pady=10,command=lambda:currency_click("USD"))
button_MXN = Button(root, text="MXN",padx=20,pady=10,command=lambda:currency_click("MXN"))
button_ILS = Button(root, text="ILS",padx=20,pady=10,command=lambda:currency_click("ILS"))
button_GBP = Button(root, text="GBP",padx=20,pady=10,command=lambda:currency_click("GBP"))
button_KRW = Button(root, text="KRW",padx=20,pady=10,command=lambda:currency_click("KRW"))
button_MYR = Button(root, text="MYR",padx=20,pady=10,command=lambda:currency_click("MYR"))

button_convert = Button(root, text="Convert",padx=20,pady=10,command=convert)
button_clear = Button(root, text="Clear",padx=20,pady=10,command=button_clear)
#button placement

button_CAD.grid(row=3,column=0)
button_HKD.grid(row=3,column=1)
button_ISK.grid(row=3,column=2)
button_PHP.grid(row=3,column=3)
button_DKK.grid(row=4,column=0) 
button_HUF.grid(row=4,column=1)
button_CZK.grid(row=4,column=2)
button_AUD.grid(row=4,column=3)
button_RON.grid(row=5,column=0)
button_SEK.grid(row=5,column=1)
button_IDR.grid(row=5,column=2)
button_INR.grid(row=5,column=3)
button_BRL.grid(row=6,column=0)
button_RUB.grid(row=6,column=1)
button_HRK.grid(row=6,column=2)
button_JPY.grid(row=6,column=3)
button_THB.grid(row=7,column=0)
button_CHF.grid(row=7,column=1)
button_SGD.grid(row=7,column=2)
button_PLN.grid(row=7,column=3)
button_BGN.grid(row=8,column=0)
button_TRY.grid(row=8,column=1)
button_CNY.grid(row=8,column=2)
button_NOK.grid(row=8,column=3)
button_ZAR.grid(row=9,column=0)
button_USD.grid(row=9,column=1)
button_MXN.grid(row=9,column=2)
button_ILS.grid(row=9,column=3)
button_GBP.grid(row=10,column=0)
button_KRW.grid(row=10,column=1)
button_MYR.grid(row=10,column=2)

button_convert.grid(row=11,column=0, columnspan=2)
button_clear.grid(row=11,column=2,columnspan=2)

root.mainloop()