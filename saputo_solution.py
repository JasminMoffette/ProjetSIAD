import lecture_fichier as lf
import saputo_problem1 as sp1
import saputo_problem2 as sp2
import solution

class SaputoSolution(solution.Solution):
    
    def __init__(self, fichier=lf.LectureFichier, resolu1 = list, resolu2=list):
        super().__init__()
        self.fichier = fichier
        self.resolu1 = resolu1
        self.resolu2 = resolu2

    def __str__(self):
        return f"Liste des produits:{self.resolu1}\nListe des routes sur les lignes:{self.resolu2}"
