
#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr = sorted(arr)
    
    min_diff = sys.maxsize
    result = []
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < min_diff:
            min_diff = arr[i] - arr[i - 1]
            result = [arr[i - 1], arr[i]]
        
        elif arr[i] - arr[i - 1] == min_diff:
            result.append(arr[i-1])
            result.append(arr[i-1])
            
    return result

    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(result)