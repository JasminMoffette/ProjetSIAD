set F;
set L;
param lien{f in F};

param gain{f in F};
param quantite{f in F};

param cadence{l in L}; 
param nb_employe{l in L};
param nb_operateur{l in L};

param employe;
param operateur;
param temps_journee;

param nettoyage{i in F, j in F};

var y{l in L} binary;
var x{f in F, l in L};

#maximize le gain en $
maximize objectif: sum{f in F, l in L} x[f,l] * gain[f];

#Permettre des fractions de lot, assure le respect des quantites
subject to c1{f in F, l in L}: x[f,l] >= 0;
subject to c2{f in F, l in L}: x[f,l] <= 1;

#Obliger la bonne ligne
subject to choix_ligne{f in F, l in L : l != lien[f]}: x[f, l] = 0;

#Respecter le temps d'une journée
subject to c3{f in F}:  sum{l in L} cadence[f] / quantite[f] * x[f,l] <= temps_journee;

#Ouvrir les lignes
subject to c4{l in L}: sum{f in F} x[f,l] <= 9999* y[l]; 

#Respecter les employes
subject to c5: sum{l in L} y[l] * nb_employe[l] <= employe;

#Respecter les operateurs
subject to c6: sum{l in L} y[l] * nb_operateur[l] <= operateur;  