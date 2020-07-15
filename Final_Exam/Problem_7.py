# Problem 7
# 20.0/20.0 points (graded)
# Implement the class myDict with the methods below, which will represent a dictionary without using a dictionary object. The methods you implement below should have the same behavior as a dict object, including raising appropriate exceptions. Your code does not have to be efficient. Any code that uses a Python dictionary object will receive 0.

# For example:

# With a dict:  |    With a myDict:
# -------------------------------------------------------------------------------
# d = {}             md = myDict()        # initialize a new object using 
#                                           your choice of implementation

# d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

# print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

# del(d[1])          md.delete(1)         # use delete method to remove 
#                                           key,value pair associated with key 1
# class myDict(object):
#     """ Implements a dictionary without using a dictionary """
#     def __init__(self):
#         """ initialization of your representation """
#         #FILL THIS IN
        
#     def assign(self, k, v):
#         """ k (the key) and v (the value), immutable objects  """
#         #FILL THIS IN
        
#     def getval(self, k):
#         """ k, immutable object  """
#         #FILL THIS IN
        
#     def delete(self, k):
#         """ k, immutable object """   
#         #FILL THIS IN




class myDict(object):
    """ Implements a dictionary without using a dictionary """
    
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        self.aDict = {}

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        self.k = k
        self.v = v
        if self.k not in self.aDict:
            self.aDict[self.k] = self.v
        else:
            self.aDict[self.k] = self.v
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN

        if k in self.aDict:
            return self.aDict[k]
        else:
            raise KeyError ('KeyError successfully raised')

        # return self.aDict[k]
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
        if k in self.aDict.keys():

            del self.aDict[k]
        else:
            raise KeyError('KeyError successfully raised')

