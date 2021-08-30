#HOUSIE TICKET GENERATOR!!

import random

def deco():
    for i in range(0,75):
        print("-",end='')
   

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
    
        x.append(temp)
        #print(temp)

    #Until I get 5 numbers in each row...
    while rowcount!=[5,5,5]:
        for i in range(0,3):

            #If there are more than 5 numbers then remove the number
            if rowcount[i]>5:
                #print("Condition is running")
                a=random.randint(0,8)
                if i==0:
                    #print('Condition 1 ')
                    while (x[a][i]==0) or (x[a][i+1]==0 and x[a][i+2]==0):
                        #print('Condition 1 ',a)
                        a=random.randint(0,8)
                        
                elif i==1:
                    #print('Condition 2 ')
                    while (x[a][i]==0) or (x[a][i-1]==0 and x[a][i+1]==0):
                        #print('Condition 2 ',a)
                        a=random.randint(0,8)
                        
                elif i==2:
                    #print('Condition 3 ')
                    while (x[a][i]==0) or (x[a][i-1]==0 and x[a][i-2]==0):
                        #print('Condition 3 ',a)
                        a=random.randint(0,8)
                        
                        

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


    #Sorting the ticket
    for y in range(0,9):
        for y1 in range(0, 3):
            for y2 in range(y1, 3):
                if x[y][y1]>x[y][y2] and x[y][y1]!=0 and x[y][y2]!=0:
                    x[y][y1],x[y][y2]=x[y][y2],x[y][y1]
            
    
    #Printing Ticket
    for i in range(0,3):
        for j in range(0,9):
            if x[j][i]==0:
                print(' ', end='\t|')
            else:
                print(x[j][i], end='\t|')
        print()
    
    

n=int(input("Enter the number of tickets you want: "))
print()

for yellow in range(0,n):
    deco()
    print()
    print('\t\t\t\t',yellow+1)
    deco()
    print()
    ticket()
    deco()
    print()
    print()


'''
Check if all numbers are coming...
'''
