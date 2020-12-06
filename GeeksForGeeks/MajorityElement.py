# A = array
# N = num of elements
# A majority element is an element that appears more than N/2 times in the array
# Return "-1" if no majority exists
def majorityElement(A,N):
    A.sort()
    prevElem = 0
    majCount = N/2
    count = 0
    for i in range(len(A)):
        prevElem = A[i - 1]
        if A[i] == prevElem:
            ++count
        else:
            count
        if count > N/2:
            return A[i]