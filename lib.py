import json
import os
import logging

from constants import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def Ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError(f"Vous devez ajouter une chaine de caractère")
        
        if element in self:
            LOGGER.error(f"L'élément {element} est déja dans la liste")
            return False
        
        self.append(element)
        return True
    
    def Retirer(self, element):
        if element in self: 
            self.remove(element)
            print(f"L'élément {element} a bien été rétiré de la liste")
            return True
        return False

    def Afficher(self): 
        print(f"Les éléments contenus dans la liste {self.nom} sont:")
        for element in self: 
            print(f" - {element}")

    def Sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.mkdir(DATA_DIR)

        with open(chemin, "w", encoding='utf-8') as f:
            json.dump(self, f, indent=4)


            

if __name__=="__main__":
    liste = Liste("Course")
    liste.Ajouter("poire")
    liste.Ajouter("pomme")
    liste.Ajouter("banane")
    liste.Ajouter("gâteau")
    liste.Retirer("pomme")
    liste.Afficher()
    liste.Sauvegarder()
    