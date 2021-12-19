Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> careers=["programmeuse", "aviatrice", "avocate", "footballeuse"]
>>> print(careers.index("aviatrice"))
1
>>> print("aviatrice" in careers)
True
>>> careers.append("serveuse")
>>> print(careers)
['programmeuse', 'aviatrice', 'avocate', 'footballeuse', 'serveuse']
>>> careers.insert(1,"docteure",/)
SyntaxError: invalid syntax
>>> careers.insert(1, "docteure")
>>> print(careers)
['programmeuse', 'docteure', 'aviatrice', 'avocate', 'footballeuse', 'serveuse']
>>> for career in careers:
	print(career)

	
programmeuse
docteure
aviatrice
avocate
footballeuse
serveuse
>>> #Starting from empty
>>> #Create the list you ended up with in Working List, but this time start your file with an empty list and fill it up using append() statements.
>>> careers=[]
>>> careers.append("programmeuse")
>>> careers.append("docteure")
>>> careers.append("aviatrice")
>>> careers.append("avocate")
>>> careers.append("footballeuse")
>>> careers.append("serveuse")
>>> print(careers)
['programmeuse', 'docteure', 'aviatrice', 'avocate', 'footballeuse', 'serveuse']
>>> #Print a statement that tells us what the first career you thought of was.
>>> print(careers[0])
programmeuse
>>> print(careers[-1])
serveuse
>>> #Ordered Working List
>>> #Start with the list you created in Working List.
>>> careers=["programmeuse", "aviatrice", "avocate", "footballeuse"]
>>> #Print the list in its original order.
>>> for career in careers:
	print(career)

	
programmeuse
aviatrice
avocate
footballeuse
>>> #Print the list in alphabetical order.
>>> for career in sorted(careers):
	print(career.title())

	
Aviatrice
Avocate
Footballeuse
Programmeuse
>>> #Print the list in its original order.
>>> for career in careers:
	print(career.title())

	
Programmeuse
Aviatrice
Avocate
Footballeuse
>>> #Print the list in reverse alphabetical order.
>>> for career in sorted(careers, reverse=True):
	print(career.title())

	
Programmeuse
Footballeuse
Avocate
Aviatrice
>>> Print the list in its original order.
SyntaxError: invalid syntax
>>> #Print the list in its original order.
>>> for career in careers:
	print(career.title())

	
Programmeuse
Aviatrice
Avocate
Footballeuse
>>> #Print the list in the reverse order from what it started.
>>> careers.reverse()
>>> print(careers)
['footballeuse', 'avocate', 'aviatrice', 'programmeuse']
>>> #Print the list in its original order
>>> careers.reverse()
>>> print(careers)
['programmeuse', 'aviatrice', 'avocate', 'footballeuse']
>>> #Permanently sort the list in alphabetical order, and then print it out.
>>> careers.sort()
>>> print(careers)
['aviatrice', 'avocate', 'footballeuse', 'programmeuse']
>>> careers.sort(reverse=True)
>>> print(careers)
['programmeuse', 'footballeuse', 'avocate', 'aviatrice']
>>> #Ordered numbers
>>> #Make a list of 5 numbers, in a random order.
>>> numbers=[1,3,4,6,9]
>>> #Print the numbers in the original order.
>>> for number in numbers:
	print(number)

	
1
3
4
6
9
>>> #Print the numbers in increasing order.
>>> print(sorted(numbers))
[1, 3, 4, 6, 9]
>>> #Print the numbers in the original order.
>>> print(numbers)
[1, 3, 4, 6, 9]
>>> #Print the numbers in decreasing order.
>>> for number in sorted(numbers, reverse=True):
	print(numbers)

	
[1, 3, 4, 6, 9]
[1, 3, 4, 6, 9]
[1, 3, 4, 6, 9]
[1, 3, 4, 6, 9]
[1, 3, 4, 6, 9]
>>> print(number)
1
>>> for number in sorted(numbers, reverse=True):
	print(number)

	
9
6
4
3
1
>>> #Print the numbers in their original order.
>>> print(numbers)
[1, 3, 4, 6, 9]
>>> #Print the numbers in the reverse order from how they started.
>>> careers.reverse()
>>> print(careers)
['aviatrice', 'avocate', 'footballeuse', 'programmeuse']
>>> #Print the numbers in the original order.
>>> careers.reverse()
>>> print(careers)
['programmeuse', 'footballeuse', 'avocate', 'aviatrice']
>>> #Permanently sort the numbers in increasing order, and then print them out.
>>> numbers.sort()
>>> print(numbers)
[1, 3, 4, 6, 9]
>>> #Permanently sort the numbers in descreasing order, and then print them out.
>>> numbers.sort(reverse=True)
>>> print(numbers)
[9, 6, 4, 3, 1]
>>> #List Lenghts
>>> Copy two or three of the lists you made from the previous exercises, or make up two or three new lists.
SyntaxError: invalid syntax
>>> #Copy two or three of the lists you made from the previous exercises, or make up two or three new lists.
>>> careers=["programmeuse", "aviatrice", "avocate", "footballeuse"]
>>> animaux=["ours", "belette", "renard"]
>>> #Print out a series of statements that tell us how long each list is.
>>> lesanimaux=len(animaux)
>>> print(lesanimaux)
3
>>> #Famous people
>>> famous=["Jesus", "Cantona", "Marie", "Anastasia"]
>>> #Pop the last item from the list, and pop any item except the last item.
>>> lastfamous=famous.pop()
>>> middlefamous=famous.pop(2)
>>> print(famous)
['Jesus', 'Cantona']
>>> famous.remove("Jesus")
>>> famous.remove(0)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    famous.remove(0)
ValueError: list.remove(x): x not in list
>>> print(famous)
['Cantona']
>>> del famous[0]
>>> print("There are no famous people left in your list.")
There are no famous people left in your list.
>>> print(famous)
[]
>>> 