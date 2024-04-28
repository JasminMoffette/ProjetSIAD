set F;
set L;
param lien{f in F};

param delai_peremption{f in F};
param quantite{f in F};

param cadence{l in L}; 
param nb_employe{l in L};
param nb_operateur{l in L};

param employe;
param operateur;
param temps_journee;

var y{l in L} binary;
var x{f in F, l in L};
var debut_production{F, L} binary;

#maximize le gain en $
maximize objectif: sum{f in F, l in L} x[f,l]  * quantite[f];

#Permettre des fractions de lot, assure le respect des quantites
subject to c1{f in F, l in L}: x[f,l] >= 0;
subject to c2{f in F, l in L}: x[f,l] <= 1;

#Obliger la bonne ligne
subject to choix_ligne{f in F, l in L : l != lien[f]}: x[f, l] = 0;

#Respecter le temps d'une journÃ©e
subject to c3{l in L}:  sum{f in F} (1 / cadence[l]) * quantite[f] * x[f,l] <= temps_journee;

#Ouvrir les lignes
subject to c4{l in L}: sum{f in F} x[f,l] <= 9999* y[l]; 

#Respecter les employes
subject to c5: sum{l in L} y[l] * nb_employe[l] <= employe;

#Respecter les operateurs
subject to c6: sum{l in L} y[l] * nb_operateur[l] <= operateur;  

# Contrainte pour respecter l'ordre de priorité basé sur le délai avant péremption
# Contrainte pour respecter l'ordre de priorité basé sur le délai avant péremption
subject to priorite_delai_péremption {f1 in F, f2 in F: f1 < f2}:
    forall{l in L}
        debut_production[f2,l] >= debut_production[f1,l] + x[f1,l];
#subject to priorite_delai_péremption {f1 in F: f1 > 0}:
	#forall{l in L}
    	#x[f1, l] <= x[f1-1, l];
#subject to priorite_delai_péremption {f in F: f > 0}:
    #forall{l in L}
        #x[card(F)+1,l] <= x[card(F),l];