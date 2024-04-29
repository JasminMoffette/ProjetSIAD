import solveur
import saputo_problem1 as prob1
import lecture_fichier as lf
import amplpy
import os
import pandas as pd

class SolveurMoney(solveur.Solveur):

    def __init__(self):
        super().__init__()

    def solve(self, probleme = prob1.SaputoProbleme1):
        
        #Générer l'environnement AMPL
        ampl_path = os.path.normpath('C:/Users/Darks/Desktop/ampl_mswin64')
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)

        #Gurobi
        ampl.setOption("solver", "gurobi")
        ampl.setOption('gurobi_options', 'timelim 600 outlev 0')
        #Lire le fichier .mod
        ampl.read(os.path.normpath('C:/Users/Darks/Desktop/ProjetSIAD/1.OptiGainAmpl/phase1.mod'))

        #Générer les ensembles:
        ampl.set['F'] = list(range(0, len(probleme.fichier.produits)))
        ampl.set['L'] = list(range(0, len(probleme.cadences)))
        
        #Générer les datas pour les liens:
        df_liens = pd.DataFrame(probleme.liens)
        ampl.get_parameter("lien").set_values(df_liens)

        #Générer les datas pour les gains:
        df_gains = pd.DataFrame(probleme.gains)
        ampl.get_parameter("gain").set_values(df_gains)

        #Générer les datas pour les quantités:
        df_quantite = pd.DataFrame(probleme.quantites)
        ampl.get_parameter("quantite").set_values(df_quantite)

        #Générer les datas pour les cadences:
        df_cadences = pd.DataFrame(probleme.cadences)
        ampl.get_parameter("cadence").set_values(df_cadences)

        #Générer les datas pour les quantités:
        df_quantite = pd.DataFrame(probleme.quantites)
        ampl.get_parameter("quantite").set_values(df_quantite)

        #Générer les datas pour le nombre d'employé par ligne:
        df_employes = pd.DataFrame(probleme.employe_ligne)
        ampl.get_parameter("nb_employe").set_values(df_employes)

        #Générer les datas pour le nombre d'opérateur par ligne:
        df_operateurs = pd.DataFrame(probleme.operateur_ligne)
        ampl.get_parameter("nb_operateur").set_values(df_operateurs)

        #Générer la data pour le nombre d'employé total:
        ampl.get_parameter("employe").set(probleme.nb_employes)

        #Générer la data pour le nombre d'opérateur total:
        ampl.get_parameter("operateur").set(probleme.nb_operateurs)

        #Générer la data pour le temps dans une journée:
        ampl.get_parameter("temps_journee").set(probleme.journee)
        
  
        #Résoudre
        ampl.solve(verbose=False)

        solution_ampl = ampl.getVariable('x').get_values().to_list()
        ampl.close()
        valeurs_utilise = [triplet for triplet in solution_ampl if triplet[2] != 0]
        valeurs_utilise_arrondies = [(triplet[0], triplet[1], round(triplet[2], 2)) for triplet in valeurs_utilise]
        return valeurs_utilise_arrondies