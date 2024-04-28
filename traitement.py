import saputo_solution as ss
import lecture_fichier as lf


class Traitement():
    
    def __init__(self, fichier=lf.LectureFichier, solution=ss.SaputoSolution, solveur1=str):
        self.fichier = fichier
        self.solution = solution
        self.solveur1 = solveur1

    def affichageSolution(self):
        liste_emballage= []
        liste_route = [[]] * len(self.fichier.dict_cadence)
        
        #Récupérer les valeurs de la première solution
        for element in self.solution.resolu1:
            
            for produit in self.fichier.produits:
                if element[0] == self.fichier.produits.index(produit):
                    lot = produit.lot
                    quantite = round(element[2]* produit.quantite)

            for index, key in enumerate(self.fichier.dict_cadence.keys()):
                if element[1] == index:
                    ligne = key   
            liste_emballage.append((lot, quantite, ligne))

        print(liste_emballage)

        #Récupérer les valeurs de la deuxième solution

        for ligne in range(len(self.fichier.dict_cadence)):
            valeurs_ligne = [triplet for triplet in self.solution.resolu2 if triplet[2] == ligne]
            combinaison = [(x, y) for x, y, z in valeurs_ligne]
            print(combinaison)
            if len(combinaison) != 0:
                for j in combinaison:
                    if j[0] not in [i[1] for i in combinaison]:
                        tuple = j
                        break
                print(tuple)
                combinaison.remove(tuple)
                liste_tuple = [tuple]
                while len(liste_tuple) < len(combinaison)+1:
                    for j in combinaison:

                        if tuple[1] == j[0]:
                            liste_tuple.append(j)
                            tuple = j

                liste_route[ligne] = [liste_tuple[0][0]]
                for i in liste_tuple:
                    liste_route[ligne].append(i[1])
            
        print(liste_route)

        