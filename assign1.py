############################
##  Perfect Number
############################


def is_perfect(inputnum):
    li = [x for x in range(1,inputnum) if inputnum % x == 0]
    return sum(li) == inputnum

