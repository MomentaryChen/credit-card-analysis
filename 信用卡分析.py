# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:11:02 2018

@author: Momentary
"""

import pandas as pd 

csv_m = pd.read_csv("BANK_TWN_ALL_AG_M.CSV")    #男生
csv_f = pd.read_csv("BANK_TWN_ALL_AG_F.CSV")    #女生
#csv_m.head(5)
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
    
#print(total_f_avg)
#print(total_m_avg)

import matplotlib.pyplot as plt 
'''
plt.bar(range(len(total_f_avg)),total_f_avg , fc='r') 
plt.title('女生')
plt.show()

plt.bar(range(len(total_m_avg)),total_m_avg , fc='g') 
plt.title('男生')
plt.show()
'''
plt.bar(range(len(total_f_avg)),total_f_avg , fc='r') 
plt.bar(range(len(total_m_avg)),total_m_avg , fc='g') 
plt.show()
    

import re

getTitle = {"食":"Food","衣":"Cloth","旅館":"Accommodation","交通":"Transportation fee","文教":"Edu","百貨":"Department store","其他":"other"}
    
        
def findAvgItem(pattern):
    pattern=r''+pattern
    total_m_cost=[]
    total_f_cost=[]
    #result = re.search(pattern, string)
    #找出Item名稱
    name = []
    for str in list_name:
        if re.search(pattern, str):
            name.append(str)
    #print(name)
    #男生Item花費
    for i in range(csv_m_count):
        total=0
        for j in range(0,len(name),2):
            total += csv_m[name[j+1]][i]/csv_m[name[j]][i]
        total_m_cost.append(total/len(name))
   
    #print(total_m_cost)
    
    print()
    #女生Item花費
    for i in range(csv_f_count):
        total=0
        for j in range(0,len(name),2):
            total += csv_f[name[j+1]][i]/csv_f[name[j]][i]
        total_f_cost.append(total/len(name))
    #print(total_f_cost)
    #print(csv_f[name[1]][0],csv_f[name[0]][0])
    plt.title(getTitle[pattern])
    
    m_num = len(total_f_cost)
    m_num_month = []
    for i in range(m_num):
        m_num_month.append((i+1)%12)
    plt.bar(range(len(total_f_cost )),total_f_cost , fc='r') 
    plt.bar(range(len(total_m_cost)),total_m_cost , fc='g') 
    plt.show()
    return

#findAvgItem("食")    #少
#findAvgItem("衣")    #多
#findAvgItem("旅館")  #多
#findAvgItem("交通")  #少
#findAvgItem("文教")  #多
#findAvgItem("百貨")  #多
#findAvgItem("其他")  #多