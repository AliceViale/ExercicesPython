Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> message=("Hello world")
>>> print(message)
Hello world
>>> message=("Goodbye world")
>>> print(message)
Goodbye world
>>> citation="Jésus dit, 'Lève-toi et marche'"
>>> print(citation)
Jésus dit, 'Lève-toi et marche'
>>> prenom=Alice
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    prenom=Alice
NameError: name 'Alice' is not defined
>>> prenom=alice
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    prenom=alice
NameError: name 'alice' is not defined
>>> prenom=jeanne
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    prenom=jeanne
NameError: name 'jeanne' is not defined
>>> 
>>> 
>>> 
>>> prenom=Alice
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    prenom=Alice
NameError: name 'Alice' is not defined
>>> prenom="Alice)
SyntaxError: EOL while scanning string literal
>>> prenom="Alice"
>>> print(prenom.lower())
alice
>>> print(prenom.title())
Alice
>>> print(prenom.upper())
ALICE
>>> nom="Peyrol-Viale"
>>> print(prenom+""+nom)
AlicePeyrol-Viale
>>> print(prenom+''+nom)
AlicePeyrol-Viale
>>> print(prenom+" "+nom)
Alice Peyrol-Viale
>>> prenomAda="Ada"
>>> nomAda="Lovelace"
>>> phrase=prenomAda+" "+nomAda+" "+"est la première programmeuse de l'histoire."
>>> print(phrase)
Ada Lovelace est la première programmeuse de l'histoire.
>>> prenom="\t Alice \t"
>>> print(prenom)
	 Alice 	
>>> print(prenom.lstrip())
Alice 	
>>> print(prenom.rstrip())
	 Alice
>>> print(prenom.strip())
Alice
>>> print(2+8)
10
>>> print(10-5)
5
>>> print(3*4)
12
>>> print(5**7)
78125
>>> ordrestandard=2+5-6
>>> print(ordrestrandard)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(ordrestrandard)
NameError: name 'ordrestrandard' is not defined
>>> print(ordrestandard)
1
>>> ordreautre=(2*3)+2
>>> print(ordreautre)
8
>>> print(0.3+0.3)
0.6
>>> print(0.1+0.2)
0.30000000000000004
>>> print(0.1+0.3)
0.4
>>> print(3/4)
0.75
>>> #Commentaire qui fonctionne
>>> languages=["python", "c", "java"]
>>> language=languages[0]
>>> print(language)
python
>>> language=languages[1]
>>> print(language)
c
>>> language=languages[2]
>>> print(language)
java
>>> phrase=(" "+"Est un bon langage de programmation")
>>> print(language[0]+phrase)
j Est un bon langage de programmation
>>> print(language.title[1]+phrase)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(language.title[1]+phrase)
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(language.title()[1]+phrase)
a Est un bon langage de programmation
>>> print(language[1]+phrase)
a Est un bon langage de programmation
>>> print(language[2]+phrase)
v Est un bon langage de programmation
>>> 