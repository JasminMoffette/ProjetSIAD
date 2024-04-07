set F;
set L;

#défini le temps perdu en  nettoyage entre différent type de fromage
param temps_nettoyage{i in F, j in F};
#défini le temps perdu en changement de format entre différent fromages
param temps_format{i in F, j in F};

#Besoin en temps pour faire le lot
param besoin{i in F};

#Temps d'une journée de travail
param temps_max;

#nb Chemin par ligne
param chemin{k in L};

param lien{i in F};

#utilisation d'un chemin: 1 si la machine prend le chemin, 0 autrement.
var x {i in F, j in F, k in L} binary;
#variable pour implémenter une élimination des soustours (MTZ)
var u {i in F, k in L} >= 0, <= card(F)-1;

#Fonction objective pour minimiser le temps de production total sur les lignes
minimize objectif: 
sum{i in F, j in F, k in L} (temps_nettoyage[i,j] + temps_format[i,j]) * x[i,j,k]  + sum{i in F} besoin[i];


#obliger un arrivÃ© Ã  chaque lieu
subject to c2{j in F, k in L}: sum{i in F} x[i,j,k] <= 1;

# obliger un dÃ©part Ã  chaque lieu
subject to c1{i in F, k in L}: sum{j in F} x[i,j,k] <= 1;

#S'assurer d'avoir le nb exacte de chemins pour éviter les cycles sur chaque ligne
subject to c3{k in L}: sum{j in F, i in F: i <> j} x[i,j,k] = chemin[k];

#temps max ligne
subject to c4{k in L}: 
sum{i in F,j in F} (temps_nettoyage[i,j] + temps_format[i,j] + besoin[i]) * x[i,j,k] <= temps_max; 

#Figer la ligne
subject to choix_ligne{i in F, j in F, k in L : k != lien[i]}: x[i,j,k] = 0; 

#MTZ
subject to soustour{i in F, j in F, k in L: i <> j}: u[i,k] - u[j,k] + card(F) * x[i,j,k] <= card(F) - 1;