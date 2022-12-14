'''
 Siddesh Mishra
 Merge Sort and quick sort
 Roll no:06
 '''
import time

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        print(a) # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        if arr[j] <= pivot: # If current element is smaller than orequal to pivot
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)

def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
    print(alist)

n = int(input("Number of elements in the array:-"))
a = list(map(int, input("elements of array:-").strip().split()))[:n]
ch=int(input('\n1.Merge sort\n2.Quick sort\n'))
t0=time.time()
merge_sort(a, 0, len(a))if ch==1 else quickSort(a, 0, n - 1)
print('Sorted list: ', end='')
print(a)
t1=time.time()-t0
print('Time=',t1)


