
class Produit():

    def __init__(self, lot, type, ligne, priorite, quantite):
        self.lot = lot
        self.type = type
        self.ligne = ligne
        self.priorite = priorite
        self.quantite = quantite

    def __str__(self):
        return f"{self.lot}, {self.type}, {self.ligne}, {self.priorite}, {self.quantite}"
    
    