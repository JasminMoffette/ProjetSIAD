import saputo_problem1 as sp
import solveur_money as sm
import lecture_fichier as lf
import saputo_problem2 as sp2
import solveur_routes as sr
import saputo_solution as ss
import traitement as tr
import sys

print("\033[91m====================================================")
print("\033[1mBienvenue dans le SIAD pour l'emballage de fromages!")
print("====================================================\033[0m")

print("\033[1mLecture du fichier...\033[0m", end="")
fichier = lf.LectureFichier()
print("\033[92m done\033[0m")
print("\033[1mGénération du problème...\033[0m", end="")
probleme1 = sp.SaputoProbleme1(fichier)
print("\033[92m done\033[0m")
print("====================================================")
texte_solveur = input("\033[1mQuel solveur souhaitez vous utiliser(gain, poids, sechage)?\033[0m ")


if texte_solveur.lower() == "gain":
    print(f"\033[1msolveur sélectionné:\033[0m {texte_solveur}")
    solveur = sm.SolveurMoney()
    print("\033[1mSélection des lots et quantités...\033[0m", end="")
    solution1 = solveur.solve(probleme1)
    print(" \033[92mdone\033[0m")
elif texte_solveur.lower == "poids":
    pass
elif texte_solveur.lower == "sechage":
    pass
else:
    print("erreur, veuillez relancer.")
    sys.exit()

print("====================================================")
print("\033[1mGénération du deuxième problème...\033[0m", end="")
probleme2 = sp2.SaputoProblem2(solution1, probleme1, fichier)
print(" \033[92mdone\033[0m")
print("\033[1mSélection des routes...\033[0m", end="")
solveur = sr.SolveurRoute()
solution2 = solveur.solve(probleme2)
print(" \033[92mdone\033[0m")
print("====================================================")
print("\033[1mTraitement des solutions...\033[0m", end="")
solution_final = ss.SaputoSolution(solution1, solution2)
solution_traite = tr.Traitement(fichier, solution_final)
valeurs =solution_traite.affichageSolution()
print(" \033[92mdone\033[0m")

texte1=f"\033[1mLa solution optimale est de:\033[0m\n"
for element in valeurs[0]:
    texte1 += f"- Emballer \033[94m{element[1]}\033[0m fromages du lot \033[94m{element[0]}\033[0m sur la ligne \033[94m{element[2]}\033[0m.\n"

text2= "\033[1mVoici maintenant l'orde d'emballage:\033[0m\n"
for index,ligne in enumerate(fichier.dict_cadence.keys()):
    if len(valeurs[1][index])  != 0:
        text2+=f"- Pour la ligne \033[94m{ligne}\033[0m, l'ordre est"
        for element in valeurs[1][index]:
            text2 +=f" \033[94m{element}\033[0m,"
        text2 = text2[:-1]
        text2 += ".\n"

print("\033[94m====================================================")
print("SOLUTION")
print("====================================================\033[0m")
print(texte1)
print(text2)    