import pandas as pd
import produit

class LectureFichier():
    
    def __init__(self):
        self.produits = []
        self.operateurs = 0
        self.employes = 0

    def __str__(self) -> str:
        return f"{self.produits}, {self.operateurs}, {self.employes}"

    def setProduits(self):
        
        #Récupérer les produits de excel
        df_produits = pd.read_excel('etat.xlsx', sheet_name = "Fromage")
        
        #Les ajouter dans la liste de produits
        for index in df_produits.index:
            lot = df_produits["# de lot"][index]
            type = df_produits["Type"][index]
            ligne = df_produits["Ligne"][index]
            limite = df_produits["Limite de séchage"][index]
            quantite = df_produits["Quantité"][index]

            produit_ajout = produit.Produit(lot, type, ligne, limite, quantite)
            self.produits.append(produit_ajout)

    def setOperateurs(self):
        
        #Récupérer le nombre d'opérateur 
        df_operateurs = pd.read_excel('etat.xlsx', sheet_name= "infos" ,usecols= [0,0]) 
        
        #Ajuster le nombre d'opérateur
        self.operateurs = df_operateurs["nombre d'opérateurs"][0]

    def setEmployes(self):
          
          #Récupérer le nombre d'employé
          df_employes = pd.read_excel('etat.xlsx', sheet_name= "infos" ,usecols= [1,1])

          #Ajuter le nombre d'employé
          self.employes = df_employes["employés"][0]     

fichier = LectureFichier()
fichier.setProduits()
fichier.setOperateurs()
fichier.setEmployes()
print(fichier)