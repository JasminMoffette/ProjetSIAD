import pandas as pd
import produit

class LectureFichier():
    
    def __init__(self):
        self.produits = []
        self.operateurs = 0
        self.employes = 0
        self.journee = 0
        self.dict_cadence = {}
        self.dict_employes = {}
        self.dict_operateurs = {}
        self.dict_nettoyage = {}
        
        self.setProduits()
        self.setOperateurs()
        self.setEmployes()
        self.setDictCadence()
        self.setDictEmployes()
        self.setDictOperateurs()
        self.setJournee()
        self.setDictNettoyage()

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
            gain = df_produits["Gain"][index]

            produit_ajout = produit.Produit(lot, type, ligne, limite, quantite, gain)
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

    def setJournee(self):

        #récupérer le temps d'une journée
        df_journee =  pd.read_excel('etat.xlsx', sheet_name= "infos" ,usecols= [2,2])

        #Ajuter le nombre d'employé
        self.journee = df_journee["Temps journée"][0]

    def setDictCadence(self):

        #recupérer les cadences pour chaque ligne
        df_cadence = pd.read_excel('etat.xlsx', sheet_name= "lignes" ,usecols= [0,1])

        #générer le dictionnaire de combinaisons
        for index in df_cadence.index:
            self.dict_cadence[df_cadence["nom"][index]] = df_cadence["cadence"][index]
    
    def setDictEmployes(self):
       
        #recupérer le nombre d'employe pour chaque ligne
        df_employes = pd.read_excel('etat.xlsx', sheet_name= "lignes" ,usecols= [0,2])

        #générer le dictionnaire de combinaisons
        for index in df_employes.index:
            self.dict_employes[df_employes["nom"][index]] = df_employes["nombre d'employé"][index]

    def setDictOperateurs(self):

        #recupérer le nombre d'employe pour chaque ligne
        df_operateurs = pd.read_excel('etat.xlsx', sheet_name= "lignes" ,usecols= [0,3])

        #générer le dictionnaire de combinaisons
        for index in df_operateurs.index:
            self.dict_operateurs[df_operateurs["nom"][index]] = df_operateurs["nombre d'opérateur"][index]
        
    def setDictNettoyage(self):

        df_nettoyage = pd.read_excel('etat.xlsx', sheet_name= "Nettoyage", index_col=0, header=0)
        for index, row in df_nettoyage.iterrows():
            for column in df_nettoyage.columns:
                self.dict_nettoyage[(index, column)] = row[column] 
        

        

