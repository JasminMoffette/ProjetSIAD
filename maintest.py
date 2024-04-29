import saputo_problem1 as sp
import solveur_money as sm
import lecture_fichier as lf
import saputo_problem2 as sp2
import solveur_routes as sr
import saputo_solution as ss
import solveur_efficacite as se
import traitement as tr
import unittest as uni
fichier = lf.LectureFichier()
problem = sp.SaputoProbleme1(fichier)
solveur_argent = sm.SolveurMoney()

print("tests classe probleme saputo:")
print(problem.liens)
print(problem.gains)
print(problem.quantites)
print(problem.cadences)
print(problem.employe_ligne)
print(problem.operateur_ligne)
print(problem.nb_employes)
print(problem.nb_operateurs)
print(problem.journee)
print(problem.poids)
print(problem.sechages)


print("Tests pour solve en argent:")
solve1 = solveur_argent.solve(problem)
print(solve1)

print("Test pour probleme 2:")
probleme2 = sp2.SaputoProblem2(solve1, problem, fichier)
print(probleme2.besoins)
print(probleme2.chemins)
print(probleme2.journee)
print(probleme2.liens)
print(probleme2.temps_nettoyage)

print("Test pour solveur route:")
solveur_route = sr.SolveurRoute()
solve4= solveur_route.solve(probleme2)
print(solve4)

print("Test de la solution")
solution = ss.SaputoSolution(solve1, solve4)
print(solution)
traitement = tr.Traitement(fichier=fichier, solution=solution)
print(traitement.affichageSolution())

print("test pour solveur poids")
solveur_eff = se.SolveurEfficacite()
solve2 = solveur_eff.solve(problem)
print(solve2)
probleme22 = sp2.SaputoProblem2(solve2,problem,fichier)
solve42 = solveur_route.solve(probleme22)
print(solve42)


