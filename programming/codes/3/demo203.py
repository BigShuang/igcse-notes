arr = [7, 8, 3, 4, 5, 9, 6]

first = 0
last = len(arr)

swap = True
while last >= 1 and swap:
    swap = False
    for j in range(last-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            swap = True

    last = last - 1

print(arr)