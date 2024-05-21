


def findUnion(l1,l2):
    i = 0
    j = 0
    union_list = []
    
    while(i<len(l1) and j < len(l2)):
        if l1[i] <= l2[j]:
            if union_list == [] or union_list[-1] != l1[i]:
                union_list.append(l1[i])
            i += 1    
        else:
            if union_list == [] or union_list[-1] != l2[j]:
                union_list.append(l2[j])
            j += 1
            
    while(i<len(l1)):
        if union_list[-1] != l1[i]:
            union_list.append(l1[i])
        i += 1
        
    while(j<len(l2)):
        if union_list[-1] != l2[j]:
            union_list.append(l2[j])
        j += 1
        
    return union_list




l1 = [1,2,3,4,5,6,6]
l2 = [2,3,4,5,5,7,8]

ans = findUnion(l1,l2)
for i in ans:
    print(i, end=" ")