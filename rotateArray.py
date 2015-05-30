def rotateArray(A, k):

    temp = A[k:]

    temp.extend(A[:k])

    return temp


A = []
n = 10
for i in range(n):
    A.append(i+1)

print rotateArray(A, 4)
