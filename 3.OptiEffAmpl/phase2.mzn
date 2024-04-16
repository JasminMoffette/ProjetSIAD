% Déclaration des ensembles F et L
set of int: F;
set of int: L;
% Variables de décision
array[L] of var 0..1: y;
array[F, L] of var 0..1: x;

% Objectif
var int: objectif = sum(f in F, l in L)(x[f, l] * quantite[f]);

% Contraintes
constraint forall(f in F, l in L)(x[f, l] >= 0);
constraint forall(f in F, l in L)(x[f, l] <= 1);
constraint forall(f in F where l != lien[f], l in L)(x[f, l] = 0);
constraint forall(l in L)(sum(f in F)(1 / cadence[l] * quantite[f] * x[f, l]) <= temps_journee);
constraint forall(l in L)(sum(f in F)(x[f, l]) <= 9999 * y[l]);
constraint sum(l in L)(y[l] * nb_employe[l]) <= employe;
constraint sum(l in L)(y[l] * nb_operateur[l]) <= operateur;

% Objectif à maximiser
solve maximize objectif;

% Affichage des résultats
output ["Objectif = \(objectif)\n"];
output ["y = \(y)\n"];
output ["x = \(x)\n"];