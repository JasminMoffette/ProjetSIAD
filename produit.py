
class Produit():

    def __init__(self, lot, type, ligne, priorite, quantite, gain, poids):
        self.lot = lot
        self.type = type
        self.ligne = ligne
        self.priorite = priorite
        self.quantite = quantite
        self.gain = gain
        self.poids = poids

    def __str__(self):
        return f"{self.lot}, {self.type}, {self.ligne}, {self.priorite}, {self.quantite}"
    
    