'''
Algorithm::
Input: A sequence of n numbers a1,a2....an
Output: A permutation (reordering) a'1,a'2.... such that a'1<a'2...

Insertion Sort(A):
for j=2 to A.length:
    key=A[j]
    //insert A[j] to sorted sequence A[1....j-1]
    i=j-1
    while i>0 and A[i]>key:
        A[i+1]=A[i]
        i-=1
    A[i+1]=key
'''

def insertion_sort(arr):
    for j in range (1,len(arr)):
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=key
    return arr


print(insertion_sort([1,4,2,7,3]))