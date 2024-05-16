

def leftRotate(l,n):
    temp = [0] * n
    for i in range(1,n):
        temp[i-1] = l[i]
    
    temp[n-1] = l[0]
    
    for i in range(n):
        print(temp[i] , end=" ")
        
# time complexity: O(n) ---  bcz we are running the loop n times
# space complexity: O(n) --- bcz we are using another list to store rotated array



def newLeftRotate(l,n):
    first_ele = l[0]
    for i in range(n):
        if i == n-1:
            l[i] = first_ele
        else:
            l[i] = l[i+1]

    for i in range(n):
        print(l[i], end=" ")

# time complexity : O(n) bcz we are running the loop n times
# space complexity: O(1) here we are not using any extra space

n = 5
l = [1,2,3,4,5]
# leftRotate(l,n)
newLeftRotate(l,n)
