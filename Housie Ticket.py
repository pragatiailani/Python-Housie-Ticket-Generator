#HOUSIE TICKET GENERATOR!!

import random

def ticket():
    
    x=[]
    rowcount=[0,0,0]
    
    for i in range(0,9):
        temp=[]
        colcount=0
        for j in range(0,3):
            option=random.randint(0,1) # To decide whether it will be an empty value or not
            if option==0 and colcount<2 : # To give minimum 1 value in a column
                temp.append(0)
                colcount+=1
                
            else:
                a=random.randint(1,9)
                if (a+(i*10)) in temp: # If the value is already present in that column, change the value 
                    while (a+(i*10)) in temp:
                        a=random.randint(1,9)
                temp.append((a+(i*10)))
                rowcount[j]+=1
        

        #Sorting the columns
        for k in range(0,len(temp)):
            for z in range(k,len(temp)):
                if temp[z]<temp[k] and temp[z]!=0 and temp[k]!=0:
                    temp[z],temp[k]=temp[k],temp[z]
    
        x.append(temp)
        print(temp)

    #Until I get 5 numbers in each row...
    while rowcount!=[5,5,5]:
        for i in range(0,3):

            #If there are more than 5 numbers then remove the number
            if rowcount[i]>5:
                a=random.randint(0,8)
                #nono=1

                #while x[a][i]==0 and nono==1:
                    #nono=1
                while x[a][i]==0:
                    a=random.randint(0,8)                                
                    '''if x[a][i]==0:
                        if i==0:
                            if x[a][i+1]==0 and x[a][i+2]==0:
                                nono=1
                            else:
                                nono=0
                        elif i==1:
                            if x[a][i-1]==0 and x[a][i+1]==0:
                                nono=1
                            else:
                                nono=0
                        elif i==2:
                            if x[a][i-2]==0 and x[a][i-1]==0:
                                nono=1
                            else:
                                nono=0'''

                x[a][i]=0

                rowcount[i]-=1

            #If there are less than 5 numbers then add a number    
            elif rowcount[i]<5:
                
                a=random.randint(0,8)
                num=random.randint(1,9)

                if x[a][i]!=0:
                    while x[a][i]!=0:
                        a=random.randint(0,8)

                if (num+(a*10)) in x[a]:
                    while (num+(a*10)) in x[a]:
                        num=random.randint(1,9)

                x[a][i]= (num+(a*10))

                rowcount[i]+=1

    #print(x)
    
    #Printing Ticket
    for i in range(0,3):
        for j in range(0,9):
            if x[j][i]==0:
                print(' ', end='\t|')
            else:
                print(x[j][i], end='\t|')
        print()
    
    
'''    
for yellow in range(0,10):
    ticket()
    print()
    print()
'''
ticket()

'''So now I have 2 problems!!
1. When I'm removing a number from a row, I have to tell the program to check whether there are already 2 0s in the column or not
2. When it is adding a number I have to sort again!! ( I can do one thing i.e. sort after the ticket is ready!)
'''
