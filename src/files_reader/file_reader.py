import pandas as pd
import numpy as np

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(r'C:\Users\Karol\Desktop\ZPB\Code\ZPB_FET\res\FETs.xlsx')
data_numpy=dataframe1.to_numpy()
#print(dataframe1)
#print(data_numpy)

Ids_od_Vgs=data_numpy[1:72,1:3]
print(Ids_od_Vgs)

Ids_od_Vds=data_numpy[1:52,4:11]
print(Ids_od_Vds)



# chwilowo tu wsadzę algorytmy

I_off=Ids_od_Vgs[30,1] # Dla Vds=100mV, Vgs=0V 
I_on=Ids_od_Vgs[70,1] # Dla Vds=100mV, Vgs=4V 
print(I_off)
print(I_on)

i=0
x_prev=0
pochodna=[0]*71
for x in Ids_od_Vgs[:,1]:
    pochodna[i]=x-x_prev
    x_prev=x
    i=i+1

print(pochodna)

i2=0
x_prev2=0
pochodna2=[0]*72
for x2 in pochodna:
    pochodna2[i2]=x2-x_prev2
    x_prev2=x2
    i2=i2+1

print(pochodna2)