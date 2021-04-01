# -*- coding: utf-8 -*-
"""
Created on Thu Apr 1 23:59:59 2021

@author: sophie
"""
#%%
#import libraries
import csv
from download import download
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as stat
import matplotlib.pyplot as plt
import datetime as dt

#%%
#Download csv
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "./bicycle_20_21.csv"
download(url, path_target, replace=True)
data = pd.read_csv("bicycle_20_21.csv")
print(data)

#%%
#Rename columns
data.columns = ["Date", "Heure", "Total cumulé", "Total de la journée", "Sans nom", "Remarque"]

#%%
#Delete the two first lines and the three columns 
bic = data.drop(index = [0, 1], columns = ["Total cumulé", "Sans nom", "Remarque"])
bic = bic.set_index(bic.index - 1)

print(bic)

#%%
#First test
a = np.linspace(1, len(bic["Date"]), len(bic["Date"]))
tj = bic["Total de la journée"]
plt.scatter(a, tj)

#%%
#Bikes between midnight and 9 a.m.
bic_0_9 = bic[(bic["Heure"] > "00:01:00") & (bic["Heure"] < "09:00:01")]

bic_0_9["Date"] = pd.to_datetime(bic["Date"] + " " + bic["Heure"], format = "%d/%m/%Y %H:%M:%f")

#%%
#Total bikes per day before 9 a.m.
bic_0_9_ = bic_0_9.groupby(bic_0_9["Date"].dt.date).last()
bic_0_9_d = bic_0_9_.drop(columns = ["Heure"])

#%%
#Plot total bikes per day 
plt.scatter(bic_0_9_d["Date"], bic_0_9_d["Total de la journée"])
plt.xlabel("Date")
plt.ylabel("Nombre de vélos")
plt.title("Nombre de vélos par jour entre minuit et 9h depuis 1 an")

#%%
#Linear regression per day
bic_0_9_d.reset_index(drop = True,inplace=True) #to be sure
fit = stat.linregress(bic_0_9_d.index, bic_0_9_d['Total de la journée'])
print(fit)
linreg = fit.intercept + fit.slope * bic_0_9_d.index
print(f"R-squared: {fit.rvalue**2*100:.5f}%")

#%%
#Plot line's regression
fig = plt.figure()
axes = fig.add_subplot(111)
plt.xticks(np.arange(min(bic_0_9_d.index), max(bic_0_9_d.index)+1, 26.14))
axes.scatter(bic_0_9_d.index, bic_0_9_d["Total de la journée"], label = "Nombre de vélos")
 
axes.plot(bic_0_9_d.index, linreg, "r", label = "Droite de régression")
plt.legend()
axes.xaxis.set_ticklabels(['2020-03', '2020-05', '2020-07', '2020-09', '2020-11', '2021-01', '2021-03'])
plt.xlabel("Date")
plt.ylabel("Nombre de vélos")
plt.title("Nombre de vélos par jour entre minuit et 9h depuis 1 an")
plt.savefig("Graph regression lineaire.pdf")

# %%
#Prediction of 2nd April
pred = fit.intercept + fit.slope * 182
print(f"Le nombre de vélos passant le 2 avril serait de : {pred:1.{0}f} entre minuit et 9h.")
