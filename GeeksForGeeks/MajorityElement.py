# A = array
# N = num of elements
# A majority element is an element that appears more than N/2 times in the array
# Return "-1" if no majority exists

# Have 2 loops
def majorityElement(A,N):
    majCount = 0
    index = -1
    for i in range(N):
        count = 0
        for j in range(N):
            if(A[i] == A[j]):
                count += 1
        if(count > majCount):
            majCount = count
            index = i
    if(count > N//2):
        print(A[index])
    else:
        print("No majority element")