#20ce146-Kavya Thaker

#Dictionary
#1 Write a Python script to check whether a given key already exists in a dictionary.
d = {7: 10, 5: 20, 3: 30, 1: 40, 9: 50}
def keypres(x):
  if x in d:
      print('Key exists')
  else:
      print('Key does not exist')
keypres(5)
keypres(2)
#2 Write a Python script to merge two Python dictionaries.
d1 = {'a': 150, 'b': 500}
d2 = {'x': 30, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)
#3 Write a Python program to sum all the items in a dictionary.
dict = {'a1':10,'a2':-89,'a3':988}
print(sum(dict.values()))
#4  Write a Python script to add a key to a dictionary.
p = {1:10, 3:20}
print(p)
p.update({5:30})
print(p)
#5 Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
#Tuple
#1 Write a Python program to create a tuple with different data types.
tpl = ("tuple", True, 0.7, 5)
print(tpl)
#2 Write a Python program to create a tuple with numbers and print one item.
tpl = 1, 3, 5, 7, 9
print(tpl)
tpl = 5,
print(tpl)
#3 Write a Python program to add an item in a tuple.
tpl = (0, 2, 4, 6, 8, 1)
print(tpl)
tuplex = tpl + (9,)
print(tpl)
#4 Write a Python program to convert a tuple to a string.
tpl = ('p', 'y', 't', 'h', 'o', 'n')
str =  ''.join(tpl)
print(str)
#5 Write a Python program to find the length of a tuple.
tpl = tuple("helloworld")
print(tpl)
print(len(tpl))
#Set
#1 Write a Python program to add member(s) in a set and clear a set
day = set()
print(day)
print("\nAdd elements:")
day.add("Saturday,Sunday")
print(day)
day.clear()
#2 Write a Python program to remove an item from a set if it is present in the set.
number = set([1,3,5,7,9])
print("Original set elements:")
print(number)
print("\nRemove 0 from the set:")
number.discard(4)
print(number)
print("\nRemove 5 from the said set:")
number.discard(3)
print(number)
#3 Write a Python program to create an intersection, Union, difference of sets.
P = {0,2,4,6,8};
Q = {1,2,3,4,5};
# union
print("Union :", P | Q)
# intersection
print("Intersection :", P & Q)
# difference
print("Difference :", P - Q)
#4 Write a Python program to find maximum and the minimum value in a set.
odd = {1,3,5,7,9}
print("Original set of elements:")
print(odd)
print("\nMaximum value:")
print(max(odd))
print("\nMinimum value:")
print(min(odd))
#5 Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
mostfreq = [1,1,2,3,4,4,4,5]
tup = tuple("helloworld")
print("\nList:",mostfreq)
print("\nTuple:",tup)
ctr = max(set(mostfreq), key = mostfreq.count)
temp = max(set(tup), key=tup.count)
print("\nElement with the highest frequency:",ctr)
print("\nElement with the highest frequency:",temp)