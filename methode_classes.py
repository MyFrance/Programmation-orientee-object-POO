class Voiture():
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix
    
    @classmethod
    def peugeot(cls):
        return cls(marque = "Peugeot", vitesse = 150, prix = 17000)
    
    @classmethod
    def renault(cls): 
        return cls(marque = "Renault", vitesse = 140, prix = 18000)
    
    # fonction pour l'affichage
    def __str__(self):
        return f"Voiture de marque {self.marque} avec une vitesse de {self.vitesse} km/h"

    
peug = Voiture.peugeot()
renau = Voiture.renault()
affichage = str(peug)
print(peug)
        


