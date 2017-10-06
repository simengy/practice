def median(vec1, vec2):

    m1 = len(vec1) / 2
    m2 = len(vec1) / 2

    while m1 + m2 > 1:

        if vec1[m1] < vec2[m2]:
            vec1 = vec1[m1:]
            vec2 = vec2[:m2]
        elif vec1[m1] >= vec2[m2]:
            vec1 = vec1[:m1]
            vec2 = vec2[m2:]

        m1 = len(vec1) / 2
        m2 = len(vec2) / 2

    return vec1, vec2


class Solution:

    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)

        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pa = min(k / 2, lenA)
        pb = k - pa

        if A[pa - 1] < B[pb - 1]:
            return self.getKth(A[pa:], B, k - pa)
        else:
            return self.getKth(A, B[pb:], k - pb)

    def findMedian(self, A, B):
        lenA = len(A)
        lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB) / 2 + 1)
        else:
            return 0.5 * self.getKth(A, B, (lenA + lenB) / 2) + \
                0.5 * self.getKth(A, B, (lenA + lenB) / 2 + 1)

vec1 = [3, 24, 5, 1]
vec2 = [12, 2, 8, 9, 7]

vec1 = sorted(vec1)
vec2 = sorted(vec2)

vec = vec1[:]
vec.extend(vec2)
print sorted(vec)
print median(vec1, vec2)

sol = Solution()
print sol.findMedian(vec1, vec2)
