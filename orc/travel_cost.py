import pandas as pd
import numpy as np
from gekko import GEKKO

re1 = pd.read_csv('re1.csv')

m,n=np.shape((re1))
row_in=[]
col_in=["project","LV8","LV7","LV6","LV5","LV4","SCOTLAND","LONDON","NORTH ENGLAND","IRELAND"]

for i in range(m):
    if re1.iloc[i,1] == 1:
        row_in.append(re1.iloc[i,0])

tab1=np.zeros((len(row_in),len(col_in)))
a=0
for i in range(m):
    if re1.iloc[i,1] == 1:
        tab1[a,0] =re1.iloc[i,0]
        tab1[a,1:] = re1.iloc[i,2:11]
        a+=1
tab1_df = pd.DataFrame(data = tab1, index = np.arange(1,25), columns = col_in)

df1 = pd.read_csv('Book1.csv')
df2 = pd.read_csv('Book2.csv')
df3 = pd.read_csv('Book3.csv')
df4 = pd.read_csv('Book4.csv')
re1 = pd.read_csv('re1.csv')
re2 = pd.read_csv('re2.csv')
re3 = pd.read_csv('re3.csv')
m = GEKKO()



S_p=[]
L_p=[]
NE_p=[]
NI_p=[]
for i in range(24):
    if tab1[i,6]==int(1):
        S_p.append(tab1[i,0:11])
    elif tab1[i,7]==1:
        L_p.append(tab1[i,0:11])
    elif tab1[i,8]==1:
        NE_p.append(tab1[i,0:11])
    elif tab1[i,9]==1:
        NI_p.append(tab1[i,0:11])
S_p = np.array(S_p)
L_p = np.array(L_p)
NE_p = np.array(NE_p)
NI_p = np.array(NI_p)
tab2 = np.concatenate((S_p, L_p, NE_p, NI_p), axis=0)
tab2_df = pd.DataFrame(data = tab2, index = np.arange(1,25), columns = col_in)

import pandas as pd
import numpy as np
from gekko import GEKKO
x = m.Array(m.Var,(24,15),integer=True,lb=0,ub=30) # set decision variables
for i in range(0,24):   #set an initial guess
    for j in range(0,15):
        x[i,j].value=3
m.Equation(sum(x[:,0])<=3) # constraints for the consultants with the differnet level in the differnet base locztion 
m.Equation(sum(x[:,1])<=21)
m.Equation(sum(x[:,2])<=31)
m.Equation(sum(x[:,3])<=12)
m.Equation(sum(x[:,4])<=13)
m.Equation(sum(x[:,5])<=9)
m.Equation(sum(x[:,6])<=43)
m.Equation(sum(x[:,7])<=55)
m.Equation(sum(x[:,8])<=38)
m.Equation(sum(x[:,9])<=15)
m.Equation(sum(x[:,10])<=8)
m.Equation(sum(x[:,11])<=36)
m.Equation(sum(x[:,12])<=74)
m.Equation(sum(x[:,13])<=30)
m.Equation(sum(x[:,14])<=12)
for i in range(0,24): # constraints for optimal consultants allocation from Stage 1 results
    m.Equation( (x[i,0]+x[i,5]+x[i,10]) == tab2_df.iloc[i,1])  
    m.Equation( (x[i,1]+x[i,6]+x[i,11]) == tab2_df.iloc[i,2])    
    m.Equation( (x[i,2]+x[i,7]+x[i,12]) == tab2_df.iloc[i,3])
    m.Equation( (x[i,3]+x[i,8]+x[i,13]) == tab2_df.iloc[i,4])
    m.Equation( (x[i,4]+x[i,9]+x[i,14]) == tab2_df.iloc[i,5])
m.options.SOLVER = 1 # sole the system
m.Minimize(4*sum(sum(x[0:7:15,5:10])) + 3.5*sum(sum(x[0:7,10:15])) + 5*sum(sum(x[7:15,0:5])) + 4*sum(sum(x[7:15,10:15])) + 3*sum(sum(x[15:22,0:5])) + 3*sum(sum(x[15:22,5:10])) + 4*sum(sum(x[22:24,0:5])) + 3.5*sum(sum(x[22:24,5:10])) + 3*sum(sum(x[22:24,10:15])))
m.solve(disp=False)
print(x)
