# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:33:48 2021

@author: utilisateur
"""

#Pet names
dictionary={"Santi":"labrador","Wiwi":"pingouin", "Rustine":"chartreux"}
for word, meaning in dictionary.items():
    print("\n %s est un %s." %(word,meaning))
    
#Polling friends
response={"Sandy":"est d'accord.","Aaron":"ne veut pas répondre.","Louise":"n'est pas d'accord"}  
for word, meaning in response.items():
    print("\n%s %s" %(word,meaning))
    
#Pet names 2
dictionary={"Santi":"labrador","Wiwi":"pingouin", "Rustine":"chartreux"}
for word, meaning in dictionary.items():
    print("\n %s est un %s." %(word,meaning)) 

dictionary["Santi"] = "lévrier" 
for word, meaning in dictionary.items():
    print("\n %s est un %s." %(word,meaning)) 
    
dictionary["Icare"]= "chien" 
for word, meaning in dictionary.items():
    print("\n %s est un %s." %(word,meaning)) 
    
del dictionary["Rustine"]
for word, meaning in dictionary.items():
    print("\n %s est un %s." %(word,meaning)) 

#Weight lifting
lifting={"pompes":"50","squats":"30","planche":"10"}   
for word, meaning in lifting.items():
    print("\n J'ai fait %s %s." %(meaning,word)) 
    
lifting["pompes"]="60" 
for word, meaning in lifting.items():
    print("\n J'ai fait %s %s." %(meaning,word)) 
    
lifting["lever de poids"]="15"
for word, meaning in lifting.items():
    print("\n J'ai fait %s %s." %(meaning,word)) 
    
del lifting["pompes"] 
for word, meaning in lifting.items():
    print("\n J'ai fait %s %s." %(meaning,word))   
    
#Mountain heights
mountains={"Machapuchare":"6993","Makalu":"8485","Nupse":"7861","Kamet":"7756","Chogolisa":"7665"}
for key in mountains: 
    print('Mountain: %s' % key) 
    
for value in mountains: 
    print('\nValue: %s' % value) 

for word, meaning in mountains.items():
    print("\n %s is %s tall.\n" %(word,meaning))
    
#Mountain heights 2
for word in sorted(mountains.keys()): 
    print(word)   
    
    

    
    
    

    
    
    

    
    

    
    
    

