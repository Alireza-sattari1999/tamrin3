num = input("Enter a number: ")
order = len(num)  
sum = 0
for i in num:
    
    sum += pow(int(i),order)
 
if sum == int(num):
    
    print(num,"is an Armstrong Number.")    
else:
    
    print(num,"is not an Armstrong Number.")