def insetionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key
    


#driver code 
arr = [2,5,1,4,6,8]
print (insetionSort(arr))
for show in range(len(arr)):
    print("%d" % arr[show], end=" ")