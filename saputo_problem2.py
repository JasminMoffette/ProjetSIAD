import probleme
import saputo_problem1 as sp1
import lecture_fichier as lf
import copy

class SaputoProblem2(probleme.Probleme):
    

    def __init__(self, list_valide=list, probleme=sp1.SaputoProbleme1, fichier= lf.LectureFichier):
        super().__init__()
        self.list_valide = list_valide
        self.probleme = copy.deepcopy(probleme)
        self.fichier = copy.deepcopy(fichier)
        self.liens = []
        self.journee = probleme.journee
        self.besoins = []  
        self.chemins = [0] * len(self.fichier.dict_cadence) 
        self.temps_nettoyage = [[0 for x in range(len(list_valide))] for y in range(len(list_valide))] 

        self.setBesoins()
        self.setChemins()
        self.setTempsNettoyage()
        self.SetLiens()
        
    def setBesoins(self):
        for element in self.list_valide:
            ajout = round(self.probleme.quantites[element[0]]/self.probleme.cadences[element[1]]* element[2])
            self.besoins.append(ajout)

    def setChemins(self):

        for element in self.list_valide:
            for i in range(len(self.chemins)):
                if i == element[1]:
                    self.chemins[element[1]] += 1
                    
        
        for i in range(len(self.chemins)):
            if self.chemins[i] != 0: self.chemins[i] -= 1
            

    def setTempsNettoyage(self):
        for i in range(len(self.list_valide)):
            produit1 = self.fichier.produits[self.list_valide[i][0]].type
            for j in range(len(self.list_valide)):
                produit2 = self.fichier.produits[self.list_valide[j][0]].type
                
                for element in self.fichier.dict_nettoyage.keys():
                    if (produit1, produit2) == element:
                        self.temps_nettoyage[i][j] = self.fichier.dict_nettoyage[element]
                        self.temps_nettoyage[j][i] = self.fichier.dict_nettoyage[element]
                        break
    
    def SetLiens(self):
        for element in self.list_valide:
            for i in range(len(self.probleme.liens)):
                if i == element[0]:
                    self.liens.append(self.probleme.liens[i])
        
