import pandas as pd
import produit

class LectureFichier():
    
    def __init__(self):
        self.produits = []
        self.operateurs = 0
        self.employe = 0

    def __str__(self) -> str:
        return f"{self.produits}, {self.operateurs}, {self.employe}"

    def setProduits(self):
        
        #Récupérer les produits de excel
        df_produits = pd.read_excel('etat.xlsx', sheet_name = "Fromage")
        
        #Les ajouter dans la liste de produits
        for index in df_produits.index:
            lot = df_produits["# de lot"][index]
            type = df_produits["Type"][index]
            form = df_produits["Format"][index]
            priorite = df_produits["Priorité"][index]
            quantite = df_produits["Quantité"][index]

            produit_ajout = produit.Produit(lot, type, form, priorite, quantite)
            self.produits.append(produit_ajout)

    def setOperateurs(self):
        pass

    def setEmployes(self):
        pass      

fichier = LectureFichier()
fichier.setProduits()
