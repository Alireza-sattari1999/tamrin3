def find_GCD(p, q): 
    if p > q: 
        val = q 
    else: 
        val = p 
    for i in range(1, val+1): 
        if((p % i == 0) and (q % i == 0)): 
            gcd = i     
    return gcd 
p = 30
q = 12
print ("The gcd of 30 and 12 is : ",end="") 
print (find_GCD(30,12))