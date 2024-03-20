arr = [3, 7, 2, 9, 5, 6]

maxV = arr[0]
for i in range(1, len(arr)):
    if arr[i] > maxV:
        maxV = arr[i] 

print(maxV)