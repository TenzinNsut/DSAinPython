
def mergeSort(arr):
    # FOR DIVIDING
    # Base Case:
    # keep dividing the list, if it contains only 1 element it will stop.
    if len(arr) > 1:
        mid = len(arr)//2
        arr_left = arr[:mid]
        arr_right = arr[mid:] # mid is included

        # recusivley divide until base case is met.
        mergeSort(arr_left)
        mergeSort(arr_right)

    # FOR MERGING:
    # Need there iterators [i(left_array), j(right_array), k(original array)]
        i=0
        j=0
        k=0

        while i<len(arr_left) and j<len(arr_right):
            if arr_left[i]<arr_right[j]:
                arr[k] = arr_left[i]
                i= i+1
                k= k+1
            else:
                arr[k] = arr_right[j]
                j = j+1
                k = k+1

        # CHECK IF ANY ELEMENT WAS LEFT:
        while i < len(arr_left):
            arr[k] = arr_left[i]
            i = i+1
            k = k+1
    
        while j < len(arr_right):
            arr[k] = arr_right[j]
            j = j+1
            k = k+1


# driver code
arr = [24,6,23,7,3,8,2,9]
mergeSort(arr)
for _ in range(len(arr)):
    print("%d" % arr[_], end=" ")

    
        
    
