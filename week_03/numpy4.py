from ntpath import join
import numpy as np

my_array=np.zeros((8,8),dtype=int)
my_array[1::2,::2]=1

print(my_array)
