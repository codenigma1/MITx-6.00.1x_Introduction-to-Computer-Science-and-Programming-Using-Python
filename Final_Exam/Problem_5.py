# def uniqueValues(aDict):
#     '''
#     aDict: a dictionary
#     returns: a sorted list of keys that map to unique aDict values, empty list if none
#     '''
#     # Your code here
#     # old_aDict = aDict.values()
#     # for keys, values in aDict.items():
#     #     uniqList.append(values)
#     # print (uniqList)

#     # # Remove duplicates from uniqList
#     # uniqList = list(set(uniqList))
#     # print (uniqList)

# from collections import Counter
# def uniqueValues(aDict):
#     count = Counter(aDict.values())
#     print(count)
#     # print(list_count)
#     return sorted(k for k, v in count.items() if count[v] == 1)

from collections import Counter
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    unique_values = [k for k,v in aDict.items() if list(aDict.values()).count(v)==1]
    return unique_values

aDict = {1: 1, 2: 1, 3: 1}
print(uniqueValues(aDict))