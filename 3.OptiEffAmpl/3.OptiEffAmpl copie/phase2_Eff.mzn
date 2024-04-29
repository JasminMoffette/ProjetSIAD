

set of int: F; % lots
set of int: L; % machine

array[F] of int: lien; % lien entre la machine (l) selon le lot (f)
array[F] of float: poids; % Poids par fromage en float selon le lot (f)
array[F] of float: quantite; % Nombre de fromages par type en float selon le lot (f)

array[L] of float: cadence; % Cadence de chaque machine en float selon la machine (l)
array[L] of int: nb_employe; % Nombre d'employés selon la machine (l)
array[L] of int: nb_operateur; % Nombre d'opérateurs selon la machine (l)

int: employe;
int: operateur;
float: temps_journee; % Temps d'une journée en float

array[L] of var bool: y; % Si une machine est ouverte
array[F, L] of var 0.0..1.0: x; % Fraction de lot produite sur chaque machine (l) pour chaque lot (f) en float

var float: objectif = sum(f in F, l in L) (x[f,l] * poids[f] * quantite[f]); % maximiser la quantité de fromage produit

% Permettre des fractions de lot, assure le respect des quantites
constraint forall(f in F, l in L) (x[f,l] >= 0.0); 
constraint forall(f in F, l in L) (x[f,l] <= 1.0);

% Obliger le lien du bon lot (f) sur la bonne machine (l)
constraint forall(f in F, l in L) (if l != lien[f] then x[f, l] = 0 endif);

% Respecter le temps d'une journee
constraint forall(l in L) (sum(f in F) (quantite[f] / cadence[l] * x[f,l]) <= temps_journee);

% Ouvrir les mahine (l)
constraint forall(l in L) (sum(f in F) (x[f,l]) <= 9999 * y[l]);

% Respecter les employes par mahine (l)
constraint sum(l in L) (y[l] * nb_employe[l]) <= employe;

% Respecter les operateurs par machine (l)
constraint sum(l in L) (y[l] * nb_operateur[l]) <= operateur;

solve maximize objectif;
