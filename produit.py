
class Produit():

    def __init__(self, lot, type, form, priorite, quantite):
        self.lot = lot
        self.type = type
        self.form = form
        self.priorite = priorite
        self.quantite = quantite

    def __str__(self):
        return f"{self.lot}, {self.type}, {self.form}g, {self.priorite}, {self.quantite}"
    
    