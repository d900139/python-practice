##################
##  assign4
#################

def summ(): 
   x=[y**2 for y in range(1,11)]
   q = x[::2]
   w = x[1::2]
   e = sum(q)
   r = sum(w)
   print (e-r)

summ()

