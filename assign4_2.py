#################
##assign4_2
#################

#############
##  for test
##  x=1
##  y=10
#############

def summ(x,y):
    li=[y**2 for y in range(x,y+1)]
    odd = sum(li[x-1::2])
    even = sum(li[x::2])
    return (odd-even)
