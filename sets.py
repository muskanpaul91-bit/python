"""sets
1.unordered (no indexing)
2.semi-mutable(can add and remove, but cannot change )
3.unique elements (no duplicates)
4.heterogeneous (can contain different data types)"""
s=set()#empty set
s={10,1,2,3,4}

"""METHODS in sets
1.add()
s.add(5) #for adding single value

2.update()
s.update([6,7,8]) #for adding multiple values

3.discard()
s.discard(10) #if we use discard and element not present in sets it will not give error and print the set as it is

4.pop()
s.pop() # remove smallest element from the set

5.clear()
s.clear() #remove all the elements from the set and return empty set

6.remove()
s.remove(1)#if value is not present we will get error
"""
"""s1={1,2,3,4}
s2={2,3,4,6}

1.intersection
s1.intersection(s2)

2.union
s1.union(s2)

3.difference # return elements present in set1 but not in set2
s1.difference(s2)

4.symmetric difference
s1.symmetric_diffrence(s2)

"""

a={12,34,56,66,45,32,34,13}
a=frozenset(a)  #frozenset is a function, we can not add or remove new elements in the set

