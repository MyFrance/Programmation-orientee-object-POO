projets= ["pr_GameOfThrones", "HarryPotter", "pr_avengers"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
       return (f"Utilisateur {self.nom}, {self.prenom}")
    
    def Affichage(self):
        print(f"- {self.prenom} travaille sur les projets  {projets}")

# Classe héritage
class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        # Utilisation de la fonction super
        super().__init__(nom, prenom)

    def restriction(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(f"- {self.prenom} ne travaillera que sur le projet non protégé {projet} ")


sara = Utilisateur("Martin", "Sarah")
sara.Affichage()
marc = Junior("Marc", "Hugo")
marc.restriction()

