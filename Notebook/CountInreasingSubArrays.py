#Count increasing subarrays
'''You are given an integer array arr of length n and an integer k.
Find the number of contiguous subarrays of length k in which every element is strictly greater than the previous element '''
arr = [1, 2, 3, 2, 4, 5]
k = 3
n = len(arr)
count = 0
answer = 0
for i in range(n - 1): #Because you're accessing arr[i + 1]. We must avoid accessing an index outside the list
    if arr[i] < arr[i + 1]:
        count+=1
        if count >= k - 1:
            answer += 1
        else :
            count = 0
print(answer)
    
