import random

print(" tool array:")

n=int(input())

array=[]
a=0

while a<n:
    m=random.randint(1,50)

    if m not in array:

        array.append(m)
        a+=1
    if a==n:
        break
        
            
    print(array)

     

     