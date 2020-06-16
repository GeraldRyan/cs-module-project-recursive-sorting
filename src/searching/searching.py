# TO-DO: Implement a recursive implementation of binary search

def binary_search(array, target, start=0, end=None):
    if end == None:
        end = len(array)-1
    #base case
    if end >=start:
        mid = (end + start) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            return binary_search(array, target, start, mid -1)

        else: 
            return binary_search(array, target, mid+1, end)
    else:
        return -1

array = [1,22,453,45,246,789,65,34]
print(binary_search(array,1))
print(binary_search(array,789))
print(binary_search(array,65))
print(binary_search(array,34))
print(binary_search(array,555))




# binary_search([1,2,3,4], 3, )

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

