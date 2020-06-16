# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements

    # Your code here

    result = []
    left_ptr = right_ptr = 0

    while left_ptr < len(left) and right_ptr < len(right):

        if left[left_ptr] < right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1

    result.extend(left[left_ptr:])
    result.extend(right[right_ptr:])

    return result

    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(array):
    # Your code here
    if len(array) <= 1:
        return array
    
    midpoint = int(len(array) / 2)

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    
    array_to_return = merge(left, right)

    return array_to_return


    # return array

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

