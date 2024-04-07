import probleme
import copy
import lecture_fichier as lf

#Cette classe permet de formater les données provenant de la lecture fichier en données utilisables dans notre solveur.
#Il s'agit ainsi de générer le problème à résoudre pour la première résolution.
class SaputoProbleme1(probleme.Probleme):
    
    def __init__(self, fichier = lf.LectureFichier()):
        super().__init__()
        self.fichier = copy.deepcopy(fichier)
        self.liens = []
        self.gains = []
        self.quantites = []
        self.cadences = []
        self.employe_ligne = []
        self.operateur_ligne = []
        self.nb_employes = self.fichier.employes
        self.nb_operateurs = self.fichier.operateurs
        self.journee = self.fichier.journee
        self.setLiens()
        self.setGain()
        self.setQuantite()
        self.setCadences()
        self.setEmployes()
        self.setOperateurs()

    def setLiens(self):
        self.liens = []
        for produit in self.fichier.produits:
            ligne = produit.ligne
            nombre_ligne = 0
            for element in self.fichier.dict_cadence.keys():
                if ligne == element:
                    self.liens.append(nombre_ligne)
                    break
                nombre_ligne+=1
    
    def setCadences(self):
        self.cadences = []
        numero = 0
        for element in self.fichier.dict_cadence:
            self.cadences.append((numero, self.fichier.dict_cadence.get(element)))
            numero+=1
    
    def setEmployes(self):
        self.employe_ligne = []
        numero = 0
        for element in self.fichier.dict_employes:
            self.employe_ligne.append((numero, self.fichier.dict_employes.get(element)))
            numero+=1
        

    def setOperateurs(self):
        self.operateur_ligne = []
        numero = 0
        for element in self.fichier.dict_operateurs:
            self.operateur_ligne.append((numero, self.fichier.dict_operateurs.get(element)))
            numero+=1
        

    def setGain(self):
        self.gains = []
        for i in range(len(self.fichier.produits)):
           self.gains.append((i, self.fichier.produits[i].gain))
    
    def setQuantite(self):
        self.quantites = []
        for i in range(len(self.fichier.produits)):
            self.quantites.append((i, self.fichier.produits[i].quantite))
        
        


fichier = lf.LectureFichier()
problem = SaputoProbleme1(fichier)
print(problem.liens)
#print(problem.gains)
#print(problem.quantites)
#print(problem.cadences)
#print(problem.employe_ligne)
#print(problem.operateur_ligne)
#print(problem.nb_employes)
#print(problem.nb_operateurs)
#print(problem.journee)