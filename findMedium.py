def median(vec1, vec2):

    vec1 = sorted(vec1)
    vec2 = sorted(vec2)
    
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


vec1 = [3,24,5,16,1]
vec2 = [12,2,8,9,5]

vec = vec1[:]
vec.extend(vec2)
print sorted(vec)

print median(vec1, vec2)

