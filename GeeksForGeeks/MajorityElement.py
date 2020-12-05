# A = array
# N = num of elements
# A majority element is an element that appears more than N/2 times in the array
# Return "-1" if no majority exists
def majorityElement(A,N):
    for i in range(len(A)):
        if A[i] > N/2:
            return A[i]
        else:
            return -1