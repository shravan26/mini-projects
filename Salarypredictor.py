
#Machine-learning model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
exp = dataset.iloc[:,0].values
exp = exp.reshape(len(exp),1)
sal_eng = dataset.iloc[:,1].values
sal_eng = sal_eng.reshape(len(sal_eng),1)
sal_med = dataset.iloc[:,2].values
sal_med = sal_med.reshape(len(sal_med),1)
sal_fin = dataset.iloc[:,3].values
sal_fin = sal_fin.reshape(len(sal_fin),1)
sal_bs = dataset.iloc[:,4].values
sal_bs = sal_bs.reshape(len(sal_bs),1)
sal_law = dataset.iloc[:,5].values
sal_law = sal_law.reshape(len(sal_law),1)
sal_tea = dataset.iloc[:,6].values
sal_tea = sal_tea.reshape(len(sal_tea),1)

from sklearn.model_selection import train_test_split
exp_train , exp_test , sal_eng_train , sal_eng_test , sal_med_train , sal_med_test , sal_fin_train , sal_fin_test , sal_bs_train , sal_bs_test , sal_law_train , sal_law_test , sal_tea_train , sal_tea_test  =  train_test_split(exp , sal_eng , sal_med , sal_fin , sal_bs , sal_law , sal_tea , test_size = 1/3 , random_state = 0)

from sklearn.linear_model import LinearRegression
regressor_eng = LinearRegression()
regressor_med = LinearRegression()
regressor_fin = LinearRegression()
regressor_bs = LinearRegression()
regressor_law = LinearRegression()
regressor_tea = LinearRegression()
regressor_eng.fit(exp_train , sal_eng_train)
sal_pred_eng = regressor_eng.predict(exp_test)
regressor_med.fit(exp_train , sal_med_train)
sal_pred_med = regressor_med.predict(exp_test)
regressor_fin.fit(exp_train , sal_fin_train)
sal_pred_fin = regressor_fin.predict(exp_test)
regressor_bs.fit(exp_train , sal_bs_train)
sal_pred_bs = regressor_bs.predict(exp_test)
regressor_law.fit(exp_train , sal_law_train)
sal_pred_law = regressor_law.predict(exp_test)
regressor_tea.fit(exp_train , sal_tea_train)
sal_pred_tea = regressor_tea.predict(exp_test)

def optionselect():
    choice = selection.get()
    if choice == fields[0]:
        getSalPred_eng()
    elif choice == fields[1]:
        getSalPred_med()
    elif choice == fields[2]:
        getSalPred_fin()
    elif choice == fields[3]:
        getSalPred_bs()
    elif choice == fields[4]:
        getSalPred_law()
    elif choice == fields[5]:
        getSalPred_tea()
    else:
        tk.messagebox.showinfo("Error","Invalid Selection! Try Again")
def getSalPred_eng():
    name = name_entry.get()
    if name == "":
        tk.messagebox.showinfo("Error","Name Should not be left empty!")
        root.destroy()
    else:
        yoe = float(yearsofexperience.get())
        salary.delete('1.0' , END)
        salary.insert(END , str("%.2f" %regressor_eng.predict(yoe)).strip('[]'))

def getSalPred_med():
    name = name_entry.get()
    if name == "":
        tk.messagebox.showinfo("Error","Name Should not be left empty!")
        root.destroy()
    else:
        yoe = float(yearsofexperience.get())
        salary.delete('1.0' , END)
        salary.insert(END , str("%.2f" %regressor_med.predict(yoe)).strip('[]'))

def getSalPred_fin():
    name = name_entry.get()
    if name == "":
        tk.messagebox.showinfo("Error","Name Should not be left empty!")
        root.destroy()
    else:
        yoe = float(yearsofexperience.get())
        salary.delete('1.0' , END)
        salary.insert(END , str("%.2f" %regressor_fin.predict(yoe)).strip('[]'))

def getSalPred_bs():
    name = name_entry.get()
    if name == "":
        tk.messagebox.showinfo("Error","Name Should not be left empty!")
        root.destroy()
    else:
        yoe = float(yearsofexperience.get())
        salary.delete('1.0' , END)
        salary.insert(END , str("%.2f" %regressor_bs.predict(yoe)).strip('[]'))

def getSalPred_law():
    name = name_entry.get()
    if name == "":
        tk.messagebox.showinfo("Error","Name Should not be left empty!")
        root.destroy()
    else:
        yoe = float(yearsofexperience.get())
        salary.delete('1.0' , END)
        salary.insert(END , str("%.2f" %regressor_law.predict(yoe)).strip('[]'))

def getSalPred_tea():
    name = name_entry.get()
    if name == "":
        tk.messagebox.showinfo("Error","Name Should not be left empty!")
        root.destroy()
    else:
        yoe = float(yearsofexperience.get())
        salary.delete('1.0' , END)
        salary.insert(END , str("%.2f" %regressor_tea.predict(yoe)).strip('[]'))

#CREATE GUI
import tkinter
from tkinter import messagebox
from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('Salary Predictor')
titlelabel = Label(root, text = "Salary Predictor" , width = 20 , font = ("bold",20))
titlelabel.place(x = 90 , y = 53)
namelabel = Label(root, text = "Name:" , width = 20 , font = ("bold",10))
namelabel.place(x = 90 , y = 130)
name = StringVar()
name_entry = Entry(root , textvariable = name)
name_entry.place(x = 240 , y = 130)
yearsofexperiencelabel = Label(root, text = "Experience:" , width = 20 , font = ("bold",10))
yearsofexperiencelabel.place(x = 75 , y = 200)
yoe = StringVar()
yearsofexperience = Entry(root , textvariable = yoe)
yearsofexperience.place(x = 240 , y = 200)
fieldlabel = Label(root, text = "Field:" , width = 20 , font = ("bold",10))
fieldlabel.place(x = 90 , y = 270)
selection = StringVar()
fields = ['Engineering','Medicine','Finance','Business Strategy','Law','Teaching']
field  = OptionMenu(root,selection,*fields)
field.config(width = 20)
selection.set('Select your field')
field.place(x = 240 , y = 270)
salarylabel = Label(root, text = "Salary:", width = 20 ,font = ("bold" , 10))
salarylabel.place(x = 85 , y = 340)
salary = Text(root)
salary.config(width = 20 , height = 1)
salary.place(x = 240 , y = 340)
Button(root , text='Submit' , width=20 , bg='brown' , fg='white' , command = optionselect).place(x=180 , y=410)
root.mainloop()
