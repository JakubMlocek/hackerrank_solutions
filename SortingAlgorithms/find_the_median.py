"""
The median of a list of numbers is essentially its middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, find the median?
Example 

The sorted array . The middle element and the median is .
Function Description
Complete the findMedian function in the editor below.
findMedian has the following parameter(s):
int arr[n]: an unsorted array of integers
Returns
int: the median of the array
Input Format
The first line contains the integer , the size of . 
The second line contains  space-separated integers 
Constraints
"""

#Solution is to use quick select algorithm which gives us O(n) complexity for finding number on which should be on interested index of array after sorting
#O(n)

def partition(A, p, r):
    sr = (p + r)//2
    A[r], A[sr] = A[sr], A[r]
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSelect(A, p, r, k):
    if p == k:
        return A[k]
    q = partition(A, p, r)
    if q == k:
        return A[k]
    elif k < q:
        return quickSelect(A, p, q - 1, k)
    else:
        return quickSelect(A, q + 1, r, k)

def findMedian(arr):
    n = len(arr)
    result =  quickSelect(arr, 0, n - 1, (n//2))
    return result