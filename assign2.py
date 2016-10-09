##############
##  assign2
##############

######################
##   *for test*
##
##   inputnum='2,5,6,9,3,7'
######################




def biggest3(inputnum):
    li = map(int, inputnum.split(','))
    li.sort(reverse = True)
    return li[0:3]



#######################
##  *run test*
##
##  print li[0:3]
##  biggest3(inputnum)
#######################



