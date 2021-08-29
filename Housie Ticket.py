#HOUSIE TICKET GENERATOR!!

import random
x=[]
for i in range(0,9):
    temp=[]
    #x.append([])
    colcount=0
    for j in range(0,3):
        option=random.randint(0,1)
        if option==0 and colcount<2:
            temp.append(0)
            colcount+=1
        else:
            a=random.randint(1,9)
            if a in temp:
                while a in temp:
                    a=random.randint(1,9)
            temp.append((a+(i*10)))
        if j>0:
            if temp[j-1]>temp[j] and temp[j-1]!=0 and temp[j]!=0:
                temp[j-1],temp[j]=temp[j],temp[j-1]
    #temp.sort()
    x.append(temp)

print(x)
        
    
