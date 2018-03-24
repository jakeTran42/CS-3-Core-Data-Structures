lists = [1, 11, 2, 14, 3, 23, 4, 37, 15, 9, 16, 26, 33, 37, 79]
list2 = [(5, 'B'), ('3', 'A')]

# print(type(list2[0]), type(list2[1]))

# for item in range(len(list) - 1):
#     # print('item: ', item)
#     for i in range(item+1, (len(list))):
#         # print('i: ', i, '\n' )
#         if list[item] > list[i]:
#             list[item], list[i] = list[i], list[item]
#
# print(list)

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    for i in range(len(items)):
        for j in range(0, (len(items)-i-1)):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

print(bubble_sort(lists))
