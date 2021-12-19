# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:45:40 2021

@author: utilisateur
"""
numbers = list(range(1,1000001))
for number in range(1,21):
    print(number)
#Larger sets
for number in range(1,1002):
    print(number)
#List Comprehensions
#Numerical Comprehensions
#Multiple of tens
#Make a list of the first ten multiples of ten (10, 20, 30... 90, 100). There are a number of ways to do this, but try to do it using a list comprehension. Print out your list.
for number in range(1,100,10):
    print(number)
#Strings as lists
#Listing a sentence
#Store a single sentence in a variable. Use a for loop to print each character from your sentence on a separate line.
sentence=("J'aime les nouilles")
for letter in sentence:
    print(letter)
#Sentence List
#Store a single sentence in a variable. Create a list from your sentence. Print your raw list (don't use a loop, just print the list).   
sentence=("J'aime plus les nouilles")
sentence_list=list(sentence)
print(sentence_list)
#Sentence Slices
phrase=("Elle vit apparaître le matin et se tût discrètement")
first_phrase=phrase[0]
last_phrase=phrase[-1]
any_phrase=phrase[3:6]
print(first_phrase)
print(last_phrase)
print(any_phrase)
#Finding Python
#Store a sentence in a variable, making sure you use the word Python at least twice in the sentence.
phrase=("Python n'est pas un serpent mais le language Python")
python_present="Python"in phrase
print(python_present)
#Use the find() function to show where the word Python first appears in the sentence.
python_index=phrase.find("Python")
print(python_index)
#Use the rfind() function to show the last place Python appears in the sentence.
last_python_index=phrase.rfind("Python")
print(last_python_index)
#Use the count() function to show how many times the word Python appears in your sentence.
number_python=phrase.count("Python")
print(number_python)
#Use the split() function to break your sentence into a list of words. Print the raw list, and use a loop to print each word on its own line.
words=phrase.split(' ')
print(words)
for word in words:
    print(word)
# Use the replace() function to change Python to Ruby in your sentence.   
phrase=phrase.replace("Python","Ruby")
print(phrase)
    
    




    