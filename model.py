#importation du module JSON
import json
#importatin du module math
import math
# Création de la classe Agent
class Agent:
    # Utilisation du constructeur init pour créer une méthode
    #Self est le paramètre qui représente l'instance
    #Agent_attributes est le paramètre qui représente le dictionnaire créé à partir du fichier JSON
    #Quand on passe un dictionnaire en paramètre on utilise ** devant
    def __init__(self, position, **agent_attributes):
        self.position=position
        for attr_name, attr_value in agent_attributes.items():
            #setattr est une méthode qui prend en considération l'instance, le nom de l'attribut et de sa valeur.Permet d'accéder dans le print à n'importe quel attribut du dictionnaire. Car la méthode items, à chaque initialisation, va transformer la clé du dico en nouvel attribut.
            setattr(self, attr_name, attr_value)

#Création d'une classe Position qui comprend comme attributs la latitude et la longitude
class Position:
    def __init__(self,longitude_degrees,latitude_degrees):
        self.latitude_degrees=latitude_degrees
        self.longitude_degrees=longitude_degrees
#Création d'une méthode pour effectuer le calcul de transformation de la position en radiant. Utilisation de la propriété pour que soit imprimé comme un attribut normal.
    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180    

class Zone:
    #Attribut de classe en liste pour contenir toutes les zones créées
    ZONES=[]
    #Création d'un attribut de classe, toujours avant la méthode et en majuscules
    #Création des lignes avec la longitude
    MIN_LONGITUDE_DEGREES=-180
    MAX_LONGITUDE_DEGREES=180
    WIDTH_DEGREES=1
    HEIGHT_DEGREES=1
    #Création des colonnes avec la latitude
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 # degrees of longitude
    HEIGHT_DEGREES = 1 # degrees of latitude
    EARTH_RADIUS_KILOMETERS = 6371


    def __init__(self,corner1,corner2):
        self.corner1=corner1
        self.corner2=corner2
        self.inhabitants=[]

    

    #Méthode qui trouve dans quelle zone habite l'agent
    @classmethod
    
    #Méthode transformée en propriété pour connaitre la population d'une zone (renvoie nombre total d'éléments dans la liste de population)
    @property
    def population(self):
        return len(self.inhabitants)
    #Méthode pour ajouter l'agent à une liste
    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)
    
    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    #Trouver l'index de la zone à partir de l'index de la position
    @classmethod
    def find_zone_that_contains(cls,position):
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index    
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone
      

    #Méthode pour initialiser la grille  
    #classmethod pour lancer une méthode sur une instance
    @classmethod
    def initialize_zones(cls): 
        #Boucle pour générer une zone entre chaque longitude et latitude max
        #Création d'une boucle dans une boucle
        cls.ZONES = []
        for latitude in range (cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(latitude, longitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

    @property
    def width(self):
        return (self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        #abs prend un paramètre en nombre et le transforme en valeur absolue
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS 

    #Méthode pour calculer la surface d'une zone puis la densité de population
    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        return self.population / self.area
    #List comprehension utilisée pour calculer agréabilité des habitants
    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population    

def main():
    #Chargement et transformation des agents du fichier json pour utilisation en Python
    for agent_attributes in json.load(open("agents-100k.json")):
        
        #Création des instances latitude et longitude.
        #pop() va les supprimer une fois utilisées car on en aura plus besoin
        longitude=agent_attributes.pop("longitude")
        latitude=agent_attributes.pop("latitude")
        #Création d'une instance position avec en paramètre la longitude et la latitude
        position=Position(longitude,latitude)
        #Création d'une instance d'Agent pour chaque ligne du JSON
        agent = Agent(position,**agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        print(type(zone))
        #Méthode d'instance pour ajouter un habitant
        zone.add_inhabitant(agent)

#Exécution de la fonction main             
main()