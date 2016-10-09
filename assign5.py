###############
##  fibonacci
###############

def fib():
     f1 = 0
     f2 = 1
     while True:
          f1,f2 = f2, f1+f2
          yield f2


