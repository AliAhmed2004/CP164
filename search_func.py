def binary_search(arr, val):
    """Binary search algorithm.

    Args:
        arr (list): List of integers.
        val (int): Value to search for.

    Returns:
        int: Index of the value in the list, or -1 if not found.
    """
    # Your code here
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while low <= high:
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    return -1

def linear_search(arr, val):
    """Linear search algorithm.

    Args:
        arr (list): List of integers.
        val (int): Value to search for.

    Returns:
        int: Index of the value in the list, or -1 if not found.
    """
    # Your code here
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1