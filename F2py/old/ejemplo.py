
# scrip to count... and sum them as a list

a= range(1,1001,3) #defined as a list
b= range(1,1001,5)
c = set(a) | set(b) #redifined as a set and union
print c
print sum(c)
