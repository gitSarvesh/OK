arr = [6,3,2,8,9,1,0]
print(arr)
for i in range(len(arr)):
    minInd = 99
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            minInd = j
            arr[j], arr[i] = arr[i], arr[j]
print(arr)