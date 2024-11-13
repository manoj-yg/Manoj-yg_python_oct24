import numpy as np
def f(x,y):
    return 10*x+y
my_array=np.fromfunction(f,(5,4),dtype=int)

print('Before:\n {my_array}')
my_array[:,[0,-1]]=0 #for aall rows set 0 to 1st and last columns
my_array[[0,-1],:]=0 #for 1st row and last row ,set all elements
#-1 is index of last element

#after
print('After:\n {my_array}')