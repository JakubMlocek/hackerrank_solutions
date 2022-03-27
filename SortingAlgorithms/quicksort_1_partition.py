"""
Quicksort 1 - Partition

The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm with a running time of . In these next few challenges, we're covering a divide-and-conquer algorithm called Quicksort (also known as Partition Sort). This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as follows:
Step 1: Divide 
Choose some pivot element, , and partition your unsorted array, , into three smaller arrays: , , and , where each element in , each element in , and each element in .
Example 

In this challenge, the pivot will always be at , so the pivot is .
 is divided into , , and . 
Putting them all together, you get . There is a flexible checker that allows the elements of  and  to be in any order. For example,  is valid as well.
Given  and , partition  into , , and  using the Divide instructions above. Return a 1-dimensional array containing each element in  first, followed by each element in , followed by each element in .
Function Description
Complete the quickSort function in the editor below.
quickSort has the following parameter(s):
int arr[n]:  is the pivot element
Returns
int[n]: an array of integers as described above
Input Format
The first line contains , the size of . 
The second line contains  space-separated integers  (the unsorted array). The first integer, , is the pivot element, .
Constraints

 where 
All elements are distinct.
"""

def quicksort(A):
    p = 0
    r = len(A) - 1
    A[p], A[r] = A[r],A[p]
    x = A[r]
    i = p - 1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return A
