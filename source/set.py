

class Set(object):

    def __init__(self, elements=None):
        '''
            Initializing a list for set method with size property.
            Then check to see if elements are given.
        '''
        self.list = list()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.list.append(elements):
                self.size += 1


    def contains(self, element):
        '''
            Check if Set contains given element
        '''
        for items in self.list:
            if element == items:
                return True
        return False

    def length(self):
        return len(self.list)


    def add(self, element):
        '''
            Add the element to the Set
        '''
        if self.contains(element):
            raise ValueError('Set already have', element)
        else:
            self.list.append(element)
            self.size += 1

    def remove(self, element):
        '''
            Remove the element from the set
        '''
        self.list.remove(element)
        self.size -= 1

    def union(self, other_set):
        '''
            Get a new set where all unique element are added from both set
        '''
        new_set = Set(self.list)

        for item in other_set.list:
            if not new_set.contains(item):
                new_set.add(item)
        return new_set

    def intersection(self, other_set):
        '''
            Get a new set where element are in both other set and this set
        '''
        new_set = Set()
        for item in other_set.list:
            if self.contains(item):
                new_set.add(item)
        return new_set


    def difference(self, other_set):
        '''
            Get a new set of all element does not exist in each other set.
        '''
        new_set = Set()

        #This can be optimize by making new set from one set and then checking
        #it against the other, no need to do two for loop.
        for item in self.list():
            new_set.add(item)
            
        for item in other_set.list:
            if not new_set.contains(item):
                new_set.add(item)
        return new_set

    def is_subset(self, other_set):
        for item in other_set.list:
            if not self.contains(item):
                return False
        return True
