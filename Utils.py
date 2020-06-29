import math
def euclidean_distance(vect1, vect2):
    ans = 0.0
    for i in range(len(vect1)):
        ans+=math.pow(vect1[i]-vect2[i],2)
    return math.sqrt(ans)

def manhattan_distance(vect1, vect2):
    ans = 0.0
    for i in range(len(vect1)):
        ans+=abs(vect1[i]-vect2[i])
    return ans