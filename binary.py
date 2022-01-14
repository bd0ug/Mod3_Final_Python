# This project implements binary search and proves binary is faster than naive

# Naive search: Scan entire list and ask if its equal to a target
# If yes, return the index,
# If not, return -1

def naiveSearch(myList, target):
    for index, number in enumerate(myList):
        if number == target:
            return index
    return -1
    
def binarySearch(myList, target, left=None, right=None):
    # For the first iteration
    if left is None:
        left = 0
    if right is None:
        right = len(myList) - 1

    # Finds midpoint of list entered
    midpoint = (left + right) // 2

    # If the number before the midpoint has an index less or equal to the number after the midpoint, the number is not in the list
    if left > right:
        return -1 

    # If the midpoint is the target, return the index
    if myList[midpoint] == target:
        return midpoint
    elif target < myList[midpoint]:
        # if middle number is greater than target, eliminate all items to right of midpoint, new last item is the number before the midpoint
        return binarySearch(myList, target, left, midpoint - 1)
    else:
        # if middle number is less than target, eliminate items to left of midpoint and make the new first index the number after the midpoint
        return binarySearch(myList, target, midpoint + 1, right)


