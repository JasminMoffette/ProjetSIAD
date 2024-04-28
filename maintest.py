import saputo_problem1 as sp
import solveur_money as sm
import lecture_fichier as lf
import saputo_problem2 as sp2
import solveur_routes as sr
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
