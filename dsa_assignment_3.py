#1q Implement Binary Search
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
arr = list(map(int,input('enter the array: ').split()))
x = int(input('enter the number:'))
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


#2q Implement Merge Sort

def merge(array,l,m,r):
    n_1 = m - l + 1
    n_2 = r - m
    L =  [0] * (n_1)
    R =  [0] * (n_2)
    for i in range(0, n_1):
        L[i] = array[l + i]
    for j in range(0, n_2):
        R[j] = array[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n_1 and j < n_2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < n_1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n_2:
        j += 1
        k += 1
def merge_sort(array,l,r):
    if l < r:
        m = l+(r-l)//2
        merge_sort(array,l,m)
        merge_sort(array,m+1,r)
        merge(array,l,m,r)
array_x = list(map(int,input('enter the list of array: ').split()))
n = len(array_x)
print('given array is')
for i in range(n):
    print("%d" % array_x[i],end =" ")
merge_sort(array_x,0,n-1)
print("\n\nsorted array is")
for i in range(n):
    print("%d" % array_x[i],end =" ")


#3q Implement Quick Sort

def partition(array,lower,higher):
    pivot = array[higher]
    i = lower - 1
    for j in range(lower,higher):
        if array[j] <= pivot:
            i = i + 1
            (array[i],array[j]) = (array[j],array[i])
    (array[i + 1], array[higher]) = (array[higher],array[i + 1]) 
    return i + 1
def quick_sort(array,lower,higher):
    if lower < higher:
        pi = partition(array,lower,higher)
        quick_sort(array,lower,pi - 1)
        quick_sort(array,pi + 1,higher)
data = list(map(int,input('enter the list of array: ').split()))
print('unsorted data!')
size = len(data)
quick_sort(data,0,size - 1)
print('sorted array in ascending order!')
print(data)


#4q Implement Insertion Sort

def insertion_sort(array):
    if(n := len(array)) <= 1:
        return
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
array = list(map(int,input('enter the list of array: ').split()))
insertion_sort(array)
print(array)


#5q Write a program to sort list of strings (similar to that of dictionary)

def dictionary_sort(strings):
    return sorted(strings)
my_list = list(map(str,input('enter the list of strings: ').split()))
sorted_list = dictionary_sort(my_list)
print(sorted_list)