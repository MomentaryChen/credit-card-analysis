# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:11:02 2018

@author: Momentary
"""

import pandas as pd 

csv_m = pd.read_csv("BANK_TWN_ALL_AG_M.CSV")    #男生
csv_f = pd.read_csv("BANK_TWN_ALL_AG_F.CSV")    #女生

#得到有幾筆資料
def getCount(c):
    count=0;
    for i in range(len(c)):
        if(c["地區"][i]=='台灣'): count+=1
    return count

csv_m_count = getCount(csv_m)
csv_f_count = getCount(csv_f)

def getAvg(data1,data2):
    return data2/data1

list_name=[]

#把所有col名子存入list
for name in csv_m:      
    list_name.append(name)

col_count = len(list_name)
total_m_money=[]
total_f_money=[]
#算出那年總花費
for i in range(0,csv_m_count):          
    total=0
    for j in range(2,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_m[list_name[j+2]][i])
    total_m_money.append(total)
    
for i in range(0,csv_f_count):          
    total=0
    for j in range(2,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_f[list_name[j+2]][i])
    total_f_money.append(total)
    
#print(total_m_money)
#print(total_f_money)

#算出那年刷卡數
total_m_money_count=[]
total_f_money_count=[]

for i in range(0,csv_m_count):          
    total=0
    for j in range(3,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_m[list_name[j+2]][i])
    total_m_money_count.append(total)

for i in range(0,csv_f_count):          
    total=0
    for j in range(3,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_f[list_name[j+2]][i])
    total_f_money_count.append(total)

total_m_avg=[]
total_f_avg=[]
    
for i in range(csv_f_count):
    total_f_avg.append(total_f_money[i]/total_f_money_count[i])
    
for i in range(csv_m_count):
    total_m_avg.append(total_m_money[i]/total_m_money_count[i])
    
print(total_f_avg)
print(total_m_avg)

import matplotlib.pyplot as plt 
plt.bar(range(len(total_f_avg)),total_f_avg , fc='r') 
plt.title('女生')
plt.show()

plt.bar(range(len(total_m_avg)),total_m_avg , fc='g') 
plt.title('男生')
plt.show()

plt.bar(range(len(total_f_avg)),total_f_avg , fc='r') 
plt.bar(range(len(total_m_avg)),total_m_avg , fc='g') 
plt.show()
    
    