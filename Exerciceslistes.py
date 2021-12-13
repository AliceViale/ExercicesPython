Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> programmes=["python", "c", "java"]
>>> print(programmes[0])
python
>>> print(programmes[1])
c
>>> print(programme[2])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(programme[2])
NameError: name 'programme' is not defined
>>> print(programmes[2])
java
>>> programmes=["python", "c", "java"]
>>> phrase=("Le langage"+" "+programmes+"est un bon langage de programmation.")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    phrase=("Le langage"+" "+programmes+"est un bon langage de programmation.")
TypeError: can only concatenate str (not "list") to str
>>> phrase=Un bon langage de programmation est programmes
SyntaxError: invalid syntax
>>> print("Un bon langage de programmation est le langage" programmes[0])
SyntaxError: invalid syntax
>>> print("Un bon langage de programmation est le langage"+programmes[0])
Un bon langage de programmation est le langagepython
>>> print("Un bon langage de programmation est le langage "+programmes[0])
Un bon langage de programmation est le langage python
>>> phrase=Un bon langage de programmation est le langage
SyntaxError: invalid syntax
>>> phrase="Un bon langage de programmation est le langage"
>>> print(phrase+" "+programmes[1])
Un bon langage de programmation est le langage c
>>> print(phrase+" "+programmes[2])
Un bon langage de programmation est le langage java
>>> animaux=[ours, licorne, dahu, chevreuil]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    animaux=[ours, licorne, dahu, chevreuil]
NameError: name 'ours' is not defined
>>> animaux=["ours", "licorne", "dahu", "chevreuil"]
>>> phrase="Un des éléments de ma liste est"
>>> print(phrase+animaux[0])
Un des éléments de ma liste estours
>>> phrase="Un des éléments de ma liste est "
>>> print(phrase+animaux[1])
Un des éléments de ma liste est licorne
>>> #Exercices LOOP
>>> #Repeat First List, but this time use a loop to print out each value in the list.
>>> programmes=["python", "c", "java"]
>>> for programme in programmes
SyntaxError: invalid syntax
>>> for programme in programmes:
	print(programme)

	
python
c
java
>>> #Repeat First Neat List, but this time use a loop to print out your statements. Make sure you are writing the same sentence for all values in your list. Loops are not effective when you are trying to generate different output for each value in your list.
>>> programmes=["python", "c", "java"]phrase="Un bon langage de programmation est le langage"
SyntaxError: invalid syntax
>>> programmes=["python", "c", "java"]
>>> phrase="Un bon langage de programmation est le langage"
>>> for programme in programmes:
	print(phrase+" "+programme)

	
Un bon langage de programmation est le langage python
Un bon langage de programmation es t le langage c
Un bon langage de programmation est le langage java
>>> #Repeat Your First List, but this time use a loop to print out your message for each item in your list. Again, if you came up with different messages for each value in your list, decide on one message to repeat for each value in your list.
>>> animaux=["ours", "licorne", "dahu", "chevreuil"]
>>> phrase="Un des éléments de ma liste est "
>>> for animal in animaux:
	print(phrase+animal)

	
Un des éléments de ma liste est ours
Un des éléments de ma liste est licorne
Un des éléments de ma liste est dahu
Un des éléments de ma liste est chevreuil

>>> #Working List Make a list that includes four careers, such as 'programmer' and 'truck driver'. Use the list.index() function to find the index of one career in your list. Use the in function to show that this career is in your list.Use the append() function to add a new career to your list. Use the insert() function to add a new career at the beginning of the list. Use a loop to show all the careers in your list.
>>> careers=["programmeuse", "infirmière", "avocate", "livreuse"]
>>> print(careers.index('avocate'))






          
