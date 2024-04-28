
import solution

class SaputoSolution(solution.Solution):
    
    def __init__(self, resolu1, resolu2):
        super().__init__()
        self.resolu1 = resolu1
        self.resolu2 = resolu2

    def __str__(self):
        return f"Liste des produits:{self.resolu1}\nListe des routes sur les lignes:{self.resolu2}"
