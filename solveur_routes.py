import solveur
import saputo_problem2 as prob2
import lecture_fichier as lf
import amplpy
import os
import pandas as pd

class SolveurRoute(solveur.Solveur):

    def __init__(self):
        super().__init__()

    def solve(self, probleme = prob2.SaputoProblem2):
        
        #Générer l'environnement AMPL
        ampl_path = os.path.normpath('C:/Users/Darks/Desktop/ampl_mswin64')
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)

        #Gurobi
        ampl.setOption("solver", "gurobi")
        ampl.setOption('gurobi_options', 'timelim 600 outlev 0')
        #Lire le fichier .mod
        ampl.read(os.path.normpath('C:/Users/Darks/Desktop/ProjetSIAD/2.OptiRouteAmpl/phase4.mod'))

        #Générer les ensembles:
        ampl.set['F'] = list(range(0, len(probleme.list_valide)))
        ampl.set['L'] = list(range(0, len(probleme.chemins)))
        
        #Générer les datas pour les liens:
        df_liens = pd.DataFrame(probleme.liens)
        ampl.get_parameter("lien").set_values(df_liens)

        #Générer les datas pour le nettoyage:
        df_nettoyage = pd.DataFrame(probleme.temps_nettoyage)
        ampl.get_parameter("temps_nettoyage").set_values(df_nettoyage)

        #Générer la data pour le temps dans une journée:
        ampl.get_parameter("temps_max").set(probleme.journee)

        #Générer la data pour les besoins:
        df_besoins = pd.DataFrame(probleme.besoins)
        ampl.get_parameter("besoin").set_values(df_besoins)

        #Générer la data pour les besoins:
        df_chemins = pd.DataFrame(probleme.chemins)
        ampl.get_parameter("chemin").set_values(df_chemins)
        
  
        #Résoudre
        ampl.solve(verbose=False)

        solution_ampl = ampl.getVariable('x').get_values().to_list()
        valeurs_utilise = [quad for quad in solution_ampl if quad[3] != 0]
        valeurs_simplifie = [(x, y, z) for x, y, z, k in valeurs_utilise]
        return list(valeurs_simplifie)