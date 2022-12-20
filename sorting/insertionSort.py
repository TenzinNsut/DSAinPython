"""
Insetion sort is used: when list is partially sorted.
Boundary Cases of the Insertion Sort: takes maximum time if elements are sorted in reverse order.
Insertion Sort an in-place sorting algorithm
Time Complexity: (n^2)
"""

def insetionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i] #(current element: 1th index)
        previous = i-1

        while previous>=0 and current < arr[previous]:
            arr[previous+1] = arr[previous]
            previous = previous-1

        arr[previous+1] = current
    


# driver code
arr = [12,13,2,7,1,5,3]
insetionSort(arr)
for p in range(len(arr)):
    print("%d" % arr[p], end=" ")



    