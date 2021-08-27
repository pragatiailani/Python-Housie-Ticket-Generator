#HOUSIE TICKET GENERATOR!!

import random

x=[]
i=0
while i<3:
    x.append([])
    count=0
    for j in range(0,9):
        option=random.randint(0,1)
        if option==0:
            x[i].append(0)
        else:
            a=random.randint(0,5)
            
            if i>0 and x[i-1][j]!=0:
                innercount=0
                #p=1
                while (a+(j*10))<=x[i-1][j]:
                    a=random.randint(0,9)
                    innercount+=1
                    if innercount==10:
                        #if x[i-1][j]-p in x[i
                        #x[i-1][j]-=1
                        a=0

            if i==2 and x[i-1][j]==0:
                innercount=0
                #p=1
                while (a+(j*10))<=x[i-2][j] and a!=0:
                    a=random.randint(0,9)
                    innercount+=1
                    if innercount==10:
                        #if x[i-1][j]-p in x[i
                        #x[i-1][j]-=1
                        a=0
                        
            x[i].append(a+(j*10))
            count+=1
        #print(x[i-1][j],end='\t')
    if count!=5:
        x.pop(i)
    else:
        #print(x[i])
        i+=1
        #print()
        #print()
        #print(count)
        #print()
    

#print('\n\n',x)

for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if x[i][j]==0:
            print(' ',end='\t|')
        else:
            print(x[i][j],end='\t|')
    #for j in range(0,len(x[i])):
        #print(end='\t|')
    print()
        
'''There are still some loop holes like if I get the highest number in first attempt only then it's messed...And still
I didn't code for a column containing 3 0's'''
