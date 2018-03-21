list = [11, 2, 32, 4, 15, 15, 79, 26, 37, 18 , 79, 10]

# for item in range(len(list) - 1):
#     # print('item: ', item)
#     for i in range(item+1, (len(list))):
#         # print('i: ', i, '\n' )
#         if list[item] > list[i]:
#             list[item], list[i] = list[i], list[item]
#
# print(list)

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    """
    for item in range(len(items) - 1):
        minItem = 0
        for i in range(item, item+1):
            if items[0] > items[i]:
                minItem = i
        temp = items[item]
        items[item] = items[temp]
        items[minItem] = temp
    return items

print(selection_sort(list))
