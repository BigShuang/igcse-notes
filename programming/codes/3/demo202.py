arr = [7, 8, 3, 4, 5, 9, 6]
n = len(arr)
for i in range(n):
    swap = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            swap = True

    if not swap:
        break
    
print(arr)