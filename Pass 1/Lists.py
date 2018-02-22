empty_list = []
list1 = [1, 2, 3, 4, 5]
list2 = ["foo","man","chu","Elvis"]
list3 = [100, "Foobar", 3.14]

#nested list/multidimensional array
list4 = ["Python", [8, 4, 6], ['a','b','c']]

#stuff with list 1 functions
print(list1)
list1.pop(1) #removes from list
print(list1)
print(list1[1])

#stuff with list2
print(list2)
list2.extend([6,7]) #adds to list as part of original array
print(list2)
list2.append([6,7]) #adds as a list
print(list2)
print(list2[2])

#stuff with list 4 and 5
print(list3)
print(list4[0][1])
print(list4[1][2])
print("Length of list3: ", len(list3))

#tuples, immutable lists. Used for constant set of values that you want to iterate
tuple1 = (1,2,3,4)
print(tuple1)

#There are even dictionaries with key/value pairing
movies = {'Pacific Rim': '5 stars', 'Black Panther': '5 stars', "Zombie Beavers":"0 stars"}
for key, value in movies.items():
    print(key,value)
