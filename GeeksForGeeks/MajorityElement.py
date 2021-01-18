# A = array
# N = num of elements
# A majority element is an element that appears more than N/2 times in the array
# Return "-1" if no majority exists

# Have 2 loops
# Iterates over the array & then iterates over each # to count its occurrences
def majorityElement(A,N):
    index = -1
    majCount = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if A[i] == A[j]:
                count += 1
        if count > majCount:
            majCount = count
            index = i
    if majCount > N//2:
        return A[index]
    else:
        return -1

# INCOMPLETE: program took longer than expected