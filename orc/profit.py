import pandas as pd
import numpy as np

df1 = pd.read_csv('Book1.csv')
df2 = pd.read_csv('Book2.csv')
df3 = pd.read_csv('Book3.csv')
df4 = pd.read_csv('Book4.csv')
re1 = pd.read_csv('re1.csv')
re2 = pd.read_csv('re2.csv')
re3 = pd.read_csv('re3.csv')

salaries=np.array([[5,7.2,9.6,14,20]])
lv_summary=np.array([[20,100,160,80,40]])
#daily salaries
daily_sal=0
for i in range(len(salaries[0])):
   daily_sal+= salaries[0,i]*lv_summary[0,i]




t_r=re3.to_numpy()
travel_cost=4*sum(sum(t_r[0:6:15,5:10])) + 3.5*sum(sum(t_r[0:6,10:15])) + 5*sum(sum(t_r[6:14,0:5])) + 4*sum(sum(t_r[6:14,10:15])) + 3*sum(sum(t_r[14:21,0:5])) + 3*sum(sum(t_r[14:21,5:10])) + 4*sum(sum(t_r[21:24,0:5])) + 3.5*sum(sum(t_r[21:24,5:10])) + 3*sum(sum(t_r[21:24,10:15]))

re1_arr=re1.to_numpy()
arr2=df2.to_numpy()
arr3=df3.to_numpy()

d_r=0
for i in range(52):
    for j in range(len(salaries[0])):
        d_r+=re1_arr[i,1]*arr2[i,5+j]*arr3[i,j+1]
print("Daily Rate:")
print(d_r)
print("Daily Travel Cost:")
print(travel_cost)
print("Daily Salaries:")
print(daily_sal)
print("Profit Per Day")
print(d_r-travel_cost-daily_sal)
print("Total Proit")
print(120*(d_r-travel_cost-daily_sal))
