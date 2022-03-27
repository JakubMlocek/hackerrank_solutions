"""
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.
Example 

Sorted, . Several pairs have the minimum difference of : . Return the array .
Note 
As shown in the example, pairs may overlap.
Given a list of unsorted integers, , find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.
Function Description
Complete the closestNumbers function in the editor below.
closestNumbers has the following parameter(s):
int arr[n]: an array of integers
Returns 
- int[]: an array of integers as described
"""

#Sollution is to sort whole array. Than we look if a pair gives us a new min difference. If it does we clear our result array and put new pair in.
#If a pair has same min difference we append it to our result array.
def closestNumbers(arr):
    arr.sort()
    
    min_diff = arr[1] - arr[0]
    result = []
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < min_diff:
            min_diff = arr[i] - arr[i - 1]
            result = [arr[i - 1], arr[i]]
        
        elif arr[i] - arr[i - 1] == min_diff:
            result.append(arr[i-1])
            result.append(arr[i])
            
    return result
