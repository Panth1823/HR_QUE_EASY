# Recursion is a powerful technique used in programming to solve problems that can be broken down into smaller, simpler problems.\
# It involves a function calling itself repeatedly until a base case is reached.

def fibbonacci(position):
    if position==0:
        return 0
    elif position==1:
        return 1
    else:
        return fibbonacci(position-1)+fibbonacci(position-2)

position=int(input())
print(fibbonacci(position))