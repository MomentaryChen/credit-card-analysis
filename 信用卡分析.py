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
    for j in range(4,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_m[list_name[j]][i])
    total_m_money.append(total)
    
for i in range(0,csv_f_count):          
    total=0
    for j in range(4,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_f[list_name[j]][i])
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
        total += int(csv_m[list_name[j]][i])
    total_m_money_count.append(total)

for i in range(0,csv_f_count):          
    total=0
    for j in range(3,col_count-2,2):
        #print(csv_m[list_name[j+2]][i])
        total += int(csv_f[list_name[j]][i])
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
plt.rcParams['font.sans-serif']=['SimHei'] #解決亂碼
'''
plt.bar(range(len(total_f_avg)),total_f_avg , fc='r') 
plt.title('女生')
plt.show()

plt.bar(range(len(total_m_avg)),total_m_avg , fc='g') 
plt.title('男生')
plt.show()
'''
plt.title("Total")
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
        total_m_cost.append(total/len(name)*2)
   
    #print(total_m_cost)
    
    print()
    #女生Item花費
    for i in range(csv_f_count):
        total=0
        for j in range(0,len(name),2):
            total += csv_f[name[j+1]][i]/csv_f[name[j]][i]
        total_f_cost.append(total/len(name)*2)
    #print(total_f_cost)
    #print(csv_f[name[1]][0],csv_f[name[0]][0])
    
    '''plt.title(getTitle[pattern])
    plt.bar(range(len(total_f_cost )),total_f_cost , fc='r') 
    plt.bar(range(len(total_m_cost)),total_m_cost , fc='g') 
    plt.show()'''
    return total_m_cost,total_f_cost

key_word = ["食","衣","旅館","交通","文教","百貨","其他"]

total_m_food_cost,total_f_food_cost=findAvgItem(key_word[0])    #少
total_m_cloth_cost,total_f_cloth_cost=findAvgItem(key_word[1])    #多
total_m_accommodation_cost,total_f_accommodation_cost=findAvgItem(key_word[2])  #多
total_m_transportationFee_cost,total_f_transportationTee_cost=findAvgItem(key_word[3])  #少
total_m_edu_cost,total_f_edu_cost=findAvgItem(key_word[4])  #多
total_m_departmentStore_cost,total_f_departmentStore_cost=findAvgItem(key_word[5])  #多
total_m_other_cost,total_f_other_cost=findAvgItem(key_word[6])  #多


def getAvg(l):
    return sum(l)/len(l)

total_m_credit_card_cost = [getAvg(total_m_food_cost),  #個別花費的平均
                            getAvg(total_m_cloth_cost),
                            getAvg(total_m_accommodation_cost),
                            getAvg(total_m_transportationFee_cost),
                            getAvg(total_m_edu_cost),
                            getAvg(total_m_departmentStore_cost),
                            getAvg(total_m_other_cost)]     
total_f_credit_card_cost =  [getAvg(total_f_food_cost),  #個別花費的平均
                            getAvg(total_f_cloth_cost),
                            getAvg(total_f_accommodation_cost),
                            getAvg(total_f_transportationTee_cost),
                            getAvg(total_f_edu_cost),
                            getAvg(total_f_departmentStore_cost),
                            getAvg(total_f_other_cost)]      


print(total_f_credit_card_cost)
total_m_card_cost_percent=[]
total_f_card_cost_percent=[]
for m in total_m_credit_card_cost:
    total_m_card_cost_percent.append(m/sum(total_m_credit_card_cost))

for f in total_f_credit_card_cost:
    total_m_card_cost_percent.append(f/sum(total_m_credit_card_cost))
graph_name=[]

for i in key_word:    
    graph_name.append(getTitle[i])

plt.figure(figsize=(4,7)) #调节图形大小
labels = graph_name
sizes = total_m_credit_card_cost
colors = ['red','yellowgreen','lightskyblue','yellow','blue','lightblue','green'] #每块颜色定义
explode = (0,0,0,0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形

plt.axis('equal')
plt.show()