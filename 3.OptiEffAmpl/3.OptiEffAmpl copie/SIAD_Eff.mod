
# lots
set F;
# machine
set L;

# lien avec la machine (l) selon le lot (f)
param lien{f in F};

# Nombre de fromages par type en float selon le lot (f)
param quantite{f in F};

# Poids par fromage en float selon le lot (f)
param poids{f in F};

# Cadence selon la machine (l)
param cadence{l in L};

# Nombre d'employés selon la machine (l)
param nb_employe{l in L};

# Nombre d'opérateurs selon la machine (l)
param nb_operateur{l in L};

param employe;
param operateur;
param temps_journee;

var y{l in L} binary;
var x{f in F, l in L};

# maximiser la quantité de fromage produit
maximize objectif: sum{f in F, l in L} x[f,l] * poids[f] * quantite[f];


#Permettre des fractions de lot, assure le respect des quantites
subject to c1{f in F, l in L}: x[f,l] >= 0;
subject to c2{f in F, l in L}: x[f,l] <= 1;

#Obliger le lien du bon lot (f) sur la bonne machine (l)
subject to choix_ligne{f in F, l in L : l != lien[f]}: x[f, l] = 0;

#Respecter le temps d'une journ�e
subject to c3{l in L}:  sum{f in F} (1 / cadence[l]) * quantite[f] * x[f,l] <= temps_journee;

#Ouvrir les mahine (l)
subject to c4{l in L}: sum{f in F} x[f,l] <= 9999* y[l]; 

#Respecter les employes
subject to c5: sum{l in L} y[l] * nb_employe[l] <= employe;

#Respecter les operateurs
subject to c6: sum{l in L} y[l] * nb_operateur[l] <= operateur;  