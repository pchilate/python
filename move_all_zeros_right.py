
def moveZeros(l:[int]) -> [int]:
    j = -1
    for i in range(len(l)):
        if l[i] == 0:
            j = i
            break
    
    
    if j == -1:
        return l
    
    for k in range(j+1,len(l)):
        if l[k] != 0:
            l[k] , l[j] = l[j] , l[k]
            j += 1
    
    return l

# time complexity: O(N)
# spcae complexity: O(1)





ans = [1,2,0,3,4,0,5]

print(moveZeros(ans))