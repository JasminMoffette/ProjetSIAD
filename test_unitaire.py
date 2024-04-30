import unittest
import saputo_problem1 as sp
import solveur_money as sm
import lecture_fichier as lf
import saputo_problem2 as sp2
import solveur_routes as sr
import saputo_solution as ss
import solveur_efficacite as se
import traitement as tr

class TestUnitaire(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets nécessaires pour les tests
        self.fichier = lf.LectureFichier()
        self.problem = sp.SaputoProbleme1(self.fichier)
        self.solveur_argent = sm.SolveurMoney()
        self.solve1 = self.solveur_argent.solve(self.problem)
        self.probleme2 = sp2.SaputoProblem2(self.solve1, self.problem, self.fichier)
        self.solveur_route = sr.SolveurRoute()
        self.solve4 = self.solveur_route.solve(self.probleme2)
        self.solution = ss.SaputoSolution(self.solve1, self.solve4)
        self.traitement = tr.Traitement(fichier=self.fichier, solution=self.solution)
        self.solveur_eff = se.SolveurEfficacite()
        self.solve2 = self.solveur_eff.solve(self.problem)
        self.probleme22 = sp2.SaputoProblem2(self.solve2, self.problem, self.fichier)
        self.solve42 = self.solveur_route.solve(self.probleme22)

    def test_fichier(self):
        # Test pour les attributs de fichier
        self.assertIsInstance(self.fichier.dict_cadence, dict)
        self.assertIsInstance(self.fichier.dict_employes, dict)
        self.assertIsInstance(self.fichier.dict_nettoyage, dict)
        self.assertIsInstance(self.fichier.dict_operateurs, dict)
        self.assertIsNot(self.fichier.employes, 0)
        self.assertIsNot(self.fichier.journee, 0)
        self.assertIsNot(self.fichier.operateurs, 0)
        self.assertIsInstance(self.fichier.produits, list)

    def test_classe_probleme_saputo(self):
        # Test pour les attributs de problem
        self.assertIsNotNone(self.problem.liens)
        self.assertIsNotNone(self.problem.gains)
        self.assertIsNotNone(self.problem.quantites)
        self.assertIsNotNone(self.problem.cadences)
        self.assertIsNotNone(self.problem.employe_ligne)
        self.assertIsNotNone(self.problem.operateur_ligne)
        self.assertIsNotNone(self.problem.nb_employes)
        self.assertIsNotNone(self.problem.nb_operateurs)
        self.assertIsNotNone(self.problem.journee)
        self.assertIsNotNone(self.problem.poids)
        self.assertIsNotNone(self.problem.sechages)

    def test_solveur_argent(self):
        # Test pour le résultat du solveur d'argent
        self.assertIsNotNone(self.solve1)

    def test_probleme2(self):
        # Test pour les attributs de probleme2
        self.assertIsNotNone(self.probleme2.besoins)
        self.assertIsNotNone(self.probleme2.chemins)
        self.assertIsNotNone(self.probleme2.journee)
        self.assertIsNotNone(self.probleme2.liens)
        self.assertIsNotNone(self.probleme2.temps_nettoyage)

    def test_solveur_route(self):
        # Test pour le résultat du solveur de route
        self.assertIsNotNone(self.solve4)

    def test_solution(self):
        # Test pour vérifier l'objet solution
        self.assertIsNotNone(self.solution)

    def test_affichage_solution(self):
        # Test pour l'affichage de la solution
        affichage = self.traitement.affichageSolution()
        self.assertIsInstance(affichage, tuple)

    def test_solveur_poids(self):
        # Test pour le résultat du solveur de poids
        self.assertIsNotNone(self.solve2)
        self.assertIsNotNone(self.solve42)