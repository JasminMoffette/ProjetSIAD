import solveur
import saputo_problem1 as prob1
import lecture_fichier as lf
import minizinc as mzn
import os
import pandas as pd

class SolveurEfficacite(solveur.Solveur):

    def __init__(self):
        super().__init__()

    def solve(self, probleme = prob1.SaputoProbleme1):
        
        #Chemin vers le modèle
        mini_path = os.path.normpath("/Users/Darks/Desktop/ProjetSIAD/3.OptiEffAmpl/3.OptiEffAmpl copie/phase2_Eff.mzn")

        #Importer le solveur Gerobi
        coin = mzn.Solver.lookup("coin-bc")

        #Importer le modele à partir du path
        mini_model = mzn.Model(mini_path)

        #Générer l'instance avec le modèle et le solveur
        instance = mzn.Instance(coin, mini_model)

        #Ajouter les données provenant du problème(prob)
        instance["F"] = list(range(1,len(probleme.fichier.produits)+1))
        print(list(range(1,len(probleme.fichier.produits))))
        instance["L"] = list(range(1,len(probleme.cadences)+1))

        instance["lien"] = probleme.liens
        instance["poids"] = probleme.poids
        instance["quantite"] = probleme.quantites
        instance["nb_employe"] = probleme.employe_ligne
        instance["nb_operateur"] = probleme.operateur_ligne
        instance["temps_journee"] = probleme.journee
        instance["cadence"] = probleme.cadences
        instance["employe"] = probleme.nb_employes
        instance["operateur"] = probleme.nb_operateurs


        resolution = instance.solve()
        solution = resolution["x"]
        print(solution)
        valeurs_utilise= []
        for i in range(0,len(probleme.cadences)):
            for j in range(0,len(probleme.fichier.produits)):
                if solution[i][j] != -0.0:
                    valeurs_utilise.append((j,i,solution[i][j]))
        
        print(valeurs_utilise)