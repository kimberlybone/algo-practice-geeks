# Task:
# Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.
# This method uses the summation formula
def MissingNumber(array,n):
    sumTotal = n*(n+1)/2
    total = 0
    for i in range(len(array)):
        total += array[i]
    missingNum = sumTotal - total
    print(missingNum)