import pandas as pd # import required packages
import numpy as np
from gekko import GEKKO
df1 = pd.read_csv('Book1.csv') # import and read required data CSV file
df2 = pd.read_csv('Book2.csv')
df3 = pd.read_csv('Book3.csv')
df4 = pd.read_csv('Book4.csv')
guess=pd.read_csv('guess.csv')
m = GEKKO()
x = m.Array(m.Var,[52,6],integer=True,lb=0,ub=30) # set decision variables
for i in range(0,52):
    for j in range(0,6):
        x[i,j].value=guess.iloc[i,j] #set an initial guess to start
m.Equation(sum(x[:,1])<=20) # constraints for avaiable resources in different levels
m.Equation(sum(x[:,2])<=100)
m.Equation(sum(x[:,3])<=160)
m.Equation(sum(x[:,4])<=80)
m.Equation(sum(x[:,5])<=40)
m.Equation(sum(x[:,0])<=52)
for i in range(0,52):
    a = m.if3(-x[i,0],df4.iloc[i,5],0) # Binary constraints for the binary variable
    m.Equation(sum(x[i,1:6]) == a)     
    m.Equation(x[i,0] <= 1)
    m.Equation(x[i,1] <= df4.iloc[i,1]) # constraints for cumulative demand matrix 
    m.Equation(sum(x[i,1:3]) <= df4.iloc[i,2])
    m.Equation(sum(x[i,1:4]) <= df4.iloc[i,3])
    m.Equation(sum(x[i,1:5]) <= df4.iloc[i,4])
m.Minimize(-sum(x[:,0]))
m.solve(disp=False)
print(x)


