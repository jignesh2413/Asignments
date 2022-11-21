#1.  What is List? How will you reverse a list?

# Lists are used to store multiple items in a single variable.
#  I will reverse the list by using list.reverse() function 

# 2. How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
    
    # I will remove last object from a list by slicing the list.
    # For list1 of [-1] will be 25

# 3. Differentiate between append () and extend () methods?

    # append() adds a single element to the end of the list while extend() can add multiple individual elements to the end of the list.

# 4. Write a Python function to get the largest number, smallest num and sum of all from a list.

# l1 = [4,5,5,6,8,45,65,98,50,65]
# print(" Largest number is: ", max(l1))
# print(" Smallest number is: ", min(l1))
# print(" Sum of all number is: ", sum(l1))

# 5. How will you compare two lists?

# l1 = [10, 20, 30, 40, 50] 
# l2 = [10, 20, 30, 50, 40, 70] 
# l3 = [50, 10, 30, 20, 40] 

# l1.sort() 
# l2.sort() 
# l3.sort() 

# if l1 == l3: 
#     print ("The lists l1 and l3 are the same") 
# else: 
#     print ("The lists l1 and l3 are not the same") 


# if l1 == l2: 
#     print ("The lists l1 and l2 are the same") 
# else: 
#     print ("The lists l1 and l2 are not the same") 


# 6. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
 
# def True_words(words):
#   wd = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       wd += 1
#   return wd

# print(True_words(['abc', 'xyz', 'aba', '1221']))


# 7. Write a Python program to remove duplicates from a list.

# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)

# 8. Write a Python program to check a list is empty or not.

# my_list = []
# my_list = [2,5]
# if my_list == []:
#     print("The list is empty")
# else:
#     print("The list is not empty")

# 9.Write a Python function that takes two lists and returns true if they have at least one common member.

# def common_data(list1, list2):
#      result = False
#      for x in list1:
#          for y in list2:
#              if x == y:
#                  result = True
#                  return result
# print(common_data([1,2,3,4,5], [5,6,7,8,9]))
# print(common_data([1,2,3,4,5], [6,7,8,9]))

# 10. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l[:5])
# 	print(l[-5:])

# printValues()

# 11. Write a Python function that takes a list and returns a new list with unique elements of the first list. 

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5]))

# 12. Write a Python program to convert a list of characters into a string.

# a_list = ["Python", "Convert", "List", "String"]  
  
# string = " ".join( a_list )
    
# print (string)  
# print (type(string))

# 13. Write a Python program to select an item randomly from a list

# import random
# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))

# 14. Write a Python program to find the second smallest number in a list.

# def find_len(list1):
#     length = len(list1)
#     list1.sort()
#     print("Second Smallest element is:", list1[1])
 
# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
# Largest = find_len(list1)

# 15. Write a Python program to get unique values from a list
# my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# print("Original List : ",my_list)
# my_set = set(my_list)
# my_new_list = list(my_set)
# print("List of unique numbers : ",my_new_list)

# 16. Write a Python program to check whether a list contains a sub list

# test_list = [5, 6, 3, 8, 2, 1, 7, 1]
 

# print("The original list : " + str(test_list))
 
# sublist = [8, 2, 1]
 
# status = False
# for idx in range(len(test_list) - len(sublist) + 1):
#         if test_list[idx : idx + len(sublist)] == sublist:
#             status = True
#             break
         
# print("Is sublist present in list ? : " + str(status))

# 17. Write a Python program to split a list into different variables

# color = [("Black", "vob"), ("Red", "scs"),
#          ("Yellow", "sfg")]
# var1, var2, var3 = color
# print(var1)
# print(var2)
# print(var3)


#18. What is tuple? Difference between list and tuple.

# Tuples are used to store multiple items in a single variable.A tuple is a collection which is ordered and unchangeable.
# Lists are mutable, where Tuples are immutable.

# 19. Write a Python program to create a tuple with different data types.

# tuple = ("Tops Technologies", True, 5.7, 8)
# print(tuple)

# 20. Write a Python program to create a tuple with numbers

# tuple = 5, 10, 15, 20, 25
# print(tuple)

# tuple = 5,
# print(tuple)

# 21. Write a Python program to convert a tuple to a string.

# def convertTuple(tup):
#     str = ''.join(tup)
#     return str
 
 
# tuple = ('J', 'I', 'G', 'N', 'E', 'S', 'H')
# str = convertTuple(tuple)
# print(str)

# 22. Write a Python program to check whether an element exists within a tuple

# tuple = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print("r" in tuple)
# print(5 in tuple)

# 23. Write a Python program to find the length of a tuple

# tuple = tuple("Tops Technologies")
# print(tuple)
# print(len(tuple))

# 24. Write a Python program to convert a list to a tuple

# list = [5, 10, 7, 4, 15, 3]
# print(list)
# tuple = tuple(list)
# print(tuple)

# 25. Write a Python program to reverse a tuple
# x = ("Jignesh")
# y = reversed(x)
# print(tuple(y))

# 26. Write a Python program to replace last value of tuples in a list.

# l = [(10, 20, 40)]
# print([t[:-1] + (100,) for t in l])

# 27. Write a Python program to find the repeated items of a tuple.

# tup=(1,3,4,32,1,1,1)  
# for i in tup:
#     if tup.count(i) > 1:
#         print('Repeated Item')

# 28. Write a Python program to remove an empty tuple(s) from a list of tuples.

# def Remove(tuples):
#     tuples = [t for t in tuples if t]
#     return tuples

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
#           ('krishna', 'akbar', '45'), ('',''),()]
# print(Remove(tuples))

# 29. Write a Python program to unzip a list of tuples into individual lists. 

# l = [(1,2), (3,4), (8,9)]
# print(list(zip(*l)))

# 30. Write a Python program to convert a list of tuples into a dictionary. 

# tuples = [('tops', 1), ('python', 2), ('language', 3)]

# result = dict(tuples)

# print(result)

# 31. How will you create a dictionary using tuples in python?

# Tuple = ((5, "language"), (6, "Python"), (7, "tops"))
# print("The input Tuple:", Tuple)

# mydict = dict((x, y) for x, y in Tuple)
# print("The result dictionary:", mydict)

# 32. Write a Python script to sort (ascending and descending) a dictionary by value.

# my_dict = {'c': 3,
#            'a': 1,
#            'd': 4,
#            'b': 2}
 
# sorted_dict = sorted([(x,y)
#  for (y,x) in my_dict.items()])
 
# print("Sorted dictionary is :")
# print(sorted_dict)

# 33. Write a Python script to concatenate following dictionaries to create a new one. 

# d1={'A':1,'B':2}
# d2={'C':3}
# d1.update(d2)
# print("Concatenated dictionary is:")
# print(d1)

# 34. Write a Python script to check if a given key already exists in a dictionary.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)

# 35. How Do You Traverse Through A Dictionary Object In Python?

# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
# }
 
# keys = statesAndCapitals.keys()
# print(keys)

# 36. How Do You Check The Presence Of A Key In A Dictionary?

# dict = {'a': 100, 'b':200, 'c':300}
 
# if dict.get('c') == None:
#   print("Not Present")
# else:
#   print("Present")

# 37. Write a Python script to print a dictionary where the keys are numbers between 1 and 15

# d=dict()
# for x in range(1,16):
#     d[x]=x+1
# print(d)

# 38. Write a Python program to check multiple keys exists in a dictionary 

# student = {
#   'name': 'Jay',
#   'class': 'V',
#   'roll_id': '2'
# }
# print(student.keys() >= {'class', 'name'})
# print(student.keys() >= {'name', 'Jay'})
# print(student.keys() >= {'roll_id', 'name'})

# 39. Write a Python script to merge two Python dictionaries

# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)

# 40. Write a Python program to map two lists into a dictionary

# keys = ['red', 'green', 'blue']
# values = ['tomato','grapes', 'sky']
# color_dictionary = dict(zip(keys,values))
# print(color_dictionary)

# 41. Write a Python program to combine two dictionary adding values for common keys.  
#     d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}  
#     Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'c':400}
# d3 = {}

# for i,j in d1.items():
#     for x,y in d2.items():
#         if i==x:
#             d3[i] = (j+y)

# print(d3)

# 42. Write a Python program to print all unique values in a dictionary.

# L = [{"V":"1"}, {"V": "2"}, {"VI": "1"}, {"VI": "5"}, {"VII":"5"}, {"V":"9"},{"VIII":"7"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# 43. Why Do You Use the Zip () Method in Python?

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.


# 44. Write a Python program to create and display all combinations of letters, 
#     selecting each letter from a different key in a dictionary.
#     Sample data: {'1': ['a','b'], '2': ['c','d']}  Expected Output:  ac ad bc bd 

# my_dict= {'1':['a', 'b'], '2':['c', 'd']}
# my_list= list(my_dict.values())
# for i in my_list[0]:
#     for j in my_list[1]:
#         print(i+j)

# 45. Write a Python program to find the highest 3 values in a dictionary

# my_dict = {'A': 67, 'B': 23, 'C': 45,
#         'D': 56, 'E': 12, 'F': 69}
 
# print("Initial Dictionary:")
# print(my_dict, "\n")
 
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
 
# x=list(my_dict.values())
# d=dict()
# x.sort(reverse=True)
# x=x[:3]
# for i in x:
#     for j in my_dict.keys():
#         if(my_dict[j]==i):
#             print(str(j)+" : "+str(my_dict[j]))


#46.  Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':  300}, o {'item': 'item1', 'amount': 750}]  
# Expected Output:  Counter ({'item1': 1150, 'item2': 300}) 

# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(result) 


# 47. Write a Python program to create a dictionary from a string.  
# Note: Track the count of the letters from the string.  
# Sample string: 'w3resource'  Expected output:  {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# from collections import defaultdict, Counter
# str1 = 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# 48. Write a Python function to calculate the factorial of a number (a nonnegative integer)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# n = int(input("enter a number: "))
# print(factorial(n))

# 49. Write a Python function to check whether a number is in a given range

# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)


# 50. Write a Python function to check whether a number is perfect or not. 
# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))

# 51. Write a Python function that checks whether a passed string is palindrome or not.

# def palindrome(string):
# 	left = 0
# 	right = len(string) - 1
	
# 	while right >= left:
# 		if not string[left] == string[right]:
# 			return False
# 		left += 1
# 		right -= 1
# 	return True
# print(palindrome('tenet')) 


# 52. How Many Basic Types Of Functions Are Available In Python?


# There are three types of functions in Python:

# Built-in functions, such as help() to ask for help, min() to get the minimum value, print() to print an object to the terminal,

# User-Defined Functions (UDFs), which are functions that users create to help them out;

# Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.


# 53. How can you pick a random item from a list or tuple?

    #  We can pick random items from a list or tuple by using random.choice()

# 54. How can you pick a random item from a range?

    #   We can pick random items from a range by using random.randrange()

# 55. How can you get a random number in python?

    #    We can get random number from by using random.randint()

# 56. How will you set the starting value in generating random numbers?

# BY using seed() method we can initialize  the random number 


# 57. How will you randomizes the items of a list in place?

# The shuffle() method randomizes the items of a list in place.

# 58. Write a Python program to read a random line from a file.

# import random
# def random_line(name):
#     lines = open(name).read().splitlines()
#     return random.choice(lines)
# print(random_line('test.txt'))

# 59. Write a Python program to convert degree to radian

# pi=22/7
# degree = float(input("Input degrees: "))
# radian = degree*(pi/180)
# print(radian)

# 60. Write a Python program to calculate the area of a trapezoid

# height = float(input("Height of trapezoid: "))
# base_1 = float(input('Base one value: '))
# base_2 = float(input('Base two value: '))
# area = ((base_1 + base_2) / 2) * height
# print("Area is:", area)


# 61. Write a Python program to calculate the area of a parallelogram.

# base = float(input('Length of base: '))
# height = float(input('Measurement of height: '))
# area = base * height
# print("Area is: ", area)


# 62. Write a Python program to calculate surface volume and area of a cylinder

# pi = 3.14
# radius = float(input("Enter radius: "))
# height = float(input("enter height: "))

# SA = 2*pi*radius*height
# print("Surface area is: ", SA)

# V = pi*radius*radius*height
# print("Volume is: ", V)

# 63. Write a Python program to returns sum of all divisors of a number

# def sum_div(number):
#     divisors = [1]
#     for i in range(2, number):
#         if (number % i)==0:
#             divisors.append(i)
#     return sum(divisors)
# print(sum_div(8))
# print(sum_div(12))

# 64. Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

# print("Enter the Multiple Decimal numbers")
# dec = input("").split(",")
# print("Maximum: ", max(dec))
# print("Minimum: ", min(dec))

  







