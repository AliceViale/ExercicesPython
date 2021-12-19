# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:51:56 2021

@author: utilisateur
"""
#Games
def loving_games(game="chess"):
    print("I love playing %s" % game)
    
loving_games("polo")
loving_games("football")
loving_games("Cluedo")
loving_games()

#Favorite movie
def favorite_movie(movie="The princess bride"):
    print("My favorite movie is %s" % movie)

favorite_movie("The Grinch")
favorite_movie("Bridget Jones")
favorite_movie("The wuthering heights")
favorite_movie()

#Favorite colors
def favorite_color(color,name):
    print("\nLa couleur préférée de %s est le %s ." % (name , color))
    
favorite_color("blanc","Louise")
favorite_color("bleu","Mahmoud")
favorite_color("vert","Aaron")

#Phones
def marque_modele(phone,model):
    print("\n %s %s" %(phone,model))

marque_modele("Iphone", "6")
marque_modele("Iphone", "7")
marque_modele("Huawei", "Plus")


#Keywords arguments
#Sport teams
def team(city,sport_team=None):
    print("\nThe city of %s hosts the %s team." %(city,sport_team))
    
team("Strasbourg", sport_team="Racing") 
team("Marseille", sport_team="Olympique de Marseille")
team("Lyon", sport_team="Olympique de Lyon")

#World languages
def world_lang(country,language=None):
    print("\nThe country of %s mostly speaks %s. " %(country, language))
    
world_lang("France", language="french")
world_lang("Spain", language="spanish")
world_lang("Portugal", language="portuguese")



    
   

    
    
    
