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

var y{i in F, j in F} binary;
var x{f in F, l in L};


maximize objectif: sum{f in F, l in L} x[f,l] * gain[f];


#Permettre des fractions de lot
subject to c1{f in F, l in L}: x[f,l] >= 0;
subject to c2{f in F, l in L}: x[f,l] <= 1;

#Obliger la bonne ligne
subject to choix_ligne{f in F, l in L : l != lien[f]}: x[f, l] = 0;
