#HOUSIE TICKET GENERATOR!!

import random

x=[]
i=0
count=0
a=0

while i<3:
    x.append([])
    for j in range(0,9):
        if i==0:
            a=random.randint(0,5)
            
        if i>0:
            
            a=random.randint((x[i-1][j]),9)
            if j!=0:
                a=random.randint((x[i-1][j])/(j*10),9)
        '''
        if j==8:
            a=random.randint(0,10)'''
        x[i].append(a+(j*10))
    i+=1        
    

#Printing The Housie Ticket
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if x[i][j]==0:
            print(' ',end='\t|')
        else:
            print(x[i][j],end='\t|')
    print()
