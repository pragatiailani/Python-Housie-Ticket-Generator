#HOUSIE TICKET GENERATOR!!

import random

x=[]
i=0
count=0
a=0
while i<3:
    x.append([])
    count=0 #Counting the numbers of a row
    for j in range(0,9):
        
        option=random.randint(0,1) #The option is whether number should be printed or it should empty 

        if option==0:
            x[i].append(0)
        else:
            a=random.randint(0,4)

            #This is to check whether the numbers in column are being printed ascending or not            
            if i>0 and x[i-1][j]!=0:
                while (a+(j*10))<=x[i-1][j]:
                    #if i==2 and j==8:
                    if j==8:
                        #Because in last column there is possibility of 11 numbers (80-90)
                        a=random.randint(0,10)
                    else:
                        a=random.randint(0,7)
                    

            #This condition doesn't have any problem
            if i==2 and x[i-1][j]==0:
                while (a+(j*10))<=x[i-2][j] and a!=0:
                    a=random.randint(0,9)

                        
            x[i].append(a+(j*10))
            count+=1
            
    print(i,count)#Sometimes it is getting stuck on (1,5) So there is some problem with the third row.Just one case of (2,6)
    
    #If there are more than 5 numbers in a row remove the row
    if count!=5:
        x.pop(i)
    else:
        i+=1
    

#Printing The Housie Ticket
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if x[i][j]==0:
            print(' ',end='\t|')
        else:
            print(x[i][j],end='\t|')
    print()
        
'''There are still some loop holes like if I get the highest number in first attempt only then it's messed...And still
I didn't code for a column containing 3 0's And sometimes program is just processing and not printing'''
