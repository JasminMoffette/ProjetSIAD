import saputo_problem1 as sp
import solveur_money as sm
import lecture_fichier as lf
import saputo_problem2 as sp2

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
probleme2 = sp2.SaputoProblem2(solve1, problem, fichier)

