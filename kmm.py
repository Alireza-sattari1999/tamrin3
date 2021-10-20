from math import gcd
list1 = [5,3]  
lcm = list1[0]
for i in list1[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print("least common multiple =  ", lcm)