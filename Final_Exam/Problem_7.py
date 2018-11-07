class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals.keys():
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals.keys():
            return self.vals[e]
        else:
            return 0
    
    def __add__(self, other):
        """ assumes e is hashable
            if bag 1 + bag 2 represent new bag """
        new_bag = Bag()
        
        for item in self.vals.keys():
            if item in new_bag.vals.keys():
                new_bag.vals[item] += self.vals[item]
            else:
                new_bag.vals[item] = self.vals[item]
        for element in other.vals.keys():
            if element in new_bag.vals.keys():
                new_bag.vals[element] += other.vals[element]
            else:
                new_bag.vals[element] = other.vals[element]
        
        return new_bag

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable, then remove"""
        if e in self.vals.keys():
            del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if subsequently in self and False otherwise."""
        if e in self.vals.keys():
            return True
        else:
            return False

d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))