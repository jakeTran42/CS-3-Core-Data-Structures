#!python
import math

def sortList(lists):
    sort = []
    for i in range(len(lists)):
        minValue = lists.pop(lists.index(min(lists)))
        sort.append(minValue)
    # return sort[:int(len(sort) / 2)]
    return sort

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if item == array[index]:
        return index
    else:
        index += 1
        return linear_search_recursive(array, item, index)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests



def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # lowerBound = 0
    # upperBound = len(array) - 1
    # middleIndex = 0
    # while lowerBound <= upperBound:
    #     middleIndex = math.floor((upperBound + lowerBound) / 2)
    #     if item == array[middleIndex]:
    #         return middleIndex
    #     elif item > array[middleIndex]:
    #         lowerBound = middleIndex + 1
    #     else:
    #         upperBound = middleIndex - 1
    # return None

    arr = sortList(array)
    print(arr)

    lowerBound = 0
    upperBound = len(arr) - 1
    while True:
        if lowerBound > upperBound:
            return False
        middleIndex = math.floor((lowerBound + upperBound) / 2)
        if item == arr[middleIndex]:
            return middleIndex
        if item > arr[middleIndex]:
            lowerBound = middleIndex + 1
        else:
            upperBound = middleIndex - 1
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

print(binary_search_iterative([1,3,6,2,8,22,9,11,100,44,321,2131,67], 67))
print(binary_search_iterative(['jake', 'julie', 'jaimi'], 'julie'))
