import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    c.sort()
    
    total_cost = 0
    flowers_bought = [0] * k  # Array to track how many flowers each friend has bought
    
    for i in range(len(c)):
        friend_index = i % k
        
        cost_multiplier = 1 + flowers_bought[friend_index]
        
        total_cost += c[i] * cost_multiplier
        
        flowers_bought[friend_index] += 1
    
    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()  # Read the first line with n (number of flowers) and k (number of friends)
    n = int(nk[0])  # number of flowers
    k = int(nk[1])  # number of friends
    c = list(map(int, input().rstrip().split()))  # Read the prices of the flowers
    
    # Get the minimum cost using the getMinimumCost function
    minimumCost = getMinimumCost(k, c)
    
    # Write the result to the output file
    fptr.write(str(minimumCost) + '\n')
    fptr.close()
