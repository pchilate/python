

def findMissingNumber(l,n):
    s1 = n * (n+1)//2
    s2 = sum(l)
    
    return s1-s2


n = 5
l = [1,2,3,4]

print(findMissingNumber(l,n))