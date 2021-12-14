# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file"""
#Slicing a list
#Alphabet slices
alphabet=["a", "b","c","d","e","f","g","h","i","j"]
#Use a slice to print out the first three letters of the alphabet.
troislettres= alphabet[:3]
print(troislettres)
#Use a slice to print out any three letters from the middle of your list.
milieuphrase=alphabet[4:7]
print(milieuphrase)
#Use a slice to print out the letters from any point in the middle of your list, to the end.
lettresfin=alphabet[5:]
print(alphabet)
#Protected list
#Make a list with three people's names in it.
names=["Alice","Claire","Laurence"]
#Use a slice to make a copy of the entire list.
copynames=names[:]
print(names)
#Add at least two new names to the new copy of the list.
names.append("Gilles")
names.append("Arlette")
print(names)
#Make a loop that prints out all of the names in the original list, along with a message that this is the original list.
print("The original list is:", names)








