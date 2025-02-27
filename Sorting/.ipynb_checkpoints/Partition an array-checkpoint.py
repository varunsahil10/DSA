def partition(arr, pivot):
    n = len(arr)
    arr[pivot], arr[n-1] = arr[n-1], arr[pivot]
    temp = []
    for i in range(n):
        if arr[i] <= arr[n-1]:
            temp.append(arr[i])
    for j in range(n):
        if arr[j] > arr[n-1]:
            temp.append(arr[j])
    for k in range(n):
        arr[k] = temp[k]

arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
pivot = 6
partition(arr, pivot)
print(arr)