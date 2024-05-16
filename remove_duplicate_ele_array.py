


def removeDuplicate(l,n):
    i = 0
    for j in range(1,n+1):
        if l[j] != l[i]:
            i += 1
            l[i] = l[j]
    return i+1 
    

n = 5
l = [1,1,2,2,2,3,3]


ans = removeDuplicate(l,n)

for i in range(ans):
    print(l[i])