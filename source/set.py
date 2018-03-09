

class Set(object):

    def __init__(self, elements=None):
        self.list = list()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.list.append(elements):
                self.size += 1


    def contains(self, element):
        for items in self.list:
            if element == items:
                return True
        return False


    def add(self, element):
        if self.contains(element):
            raise ValueError('Set already have', element)
        else:
            self.list.append(element)
            self.size += 1

    def remove(self, element):
        self.list.remove(element)
        self.size -= 1

    def union(self, other_set):
        new_set = Set(self.list)

        for item in other_set.list:
            if not new_set.contains(item):
                new_set.add(item)
        return new_set


    def intersection(self, other_set):
        new_set = Set()
        for item in other_set.list:
            if self.contains(item):
                new_set.add(item)
        return new_set


    def difference(self, other_set):
        new_set = Set()

        for item in self.list():
            if not self.contains(item):
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
