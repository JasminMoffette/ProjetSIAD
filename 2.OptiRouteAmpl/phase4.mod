set F;
set L;

#d�fini le temps perdu en  nettoyage entre diff�rent type de fromage
param temps_nettoyage{i in F, j in F};

#Besoin en temps pour faire le lot
param besoin{i in F};

#Temps d'une journ�e de travail
param temps_max;

#nb Chemin par ligne
param chemin{k in L};

param lien{i in F};

#utilisation d'un chemin: 1 si la machine prend le chemin, 0 autrement.
var x {i in F, j in F, k in L} binary;
#variable pour impl�menter une �limination des soustours (MTZ)
var u {i in F, k in L} >= 0, <= card(F)-1;

#Fonction objective pour minimiser le temps de production total sur les lignes
minimize objectif: 
sum{i in F, j in F, k in L} (temps_nettoyage[i,j]) * x[i,j,k]  + sum{i in F} besoin[i];


#obliger un arrivé à chaque lieu
subject to c2{j in F, k in L}: sum{i in F} x[i,j,k] <= 1;

# obliger un départ à chaque lieu
subject to c1{i in F, k in L}: sum{j in F} x[i,j,k] <= 1;

#S'assurer d'avoir le nb exacte de chemins pour �viter les cycles sur chaque ligne
subject to c3{k in L}: sum{j in F, i in F: i <> j} x[i,j,k] = chemin[k];

#temps max ligne
subject to c4{k in L}: 
sum{i in F,j in F} (temps_nettoyage[i,j] + besoin[i]) * x[i,j,k] <= temps_max; 

#Figer la ligne
subject to choix_ligne{i in F, j in F, k in L : k != lien[i]}: x[i,j,k] = 0; 

#MTZ
subject to soustour{i in F, j in F, k in L: i <> j}: u[i,k] - u[j,k] + card(F) * x[i,j,k] <= card(F) - 1;