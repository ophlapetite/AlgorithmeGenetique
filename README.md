# ProjetPython
algorithme génétique - M1 MEEF INFO - UE Programmation
Auteurs: CLUZEL Ophélie et MAURICE Benjamin

Comment utiliser le programme ?

Lancer le fichier algorithmeGenetique.pyde
Exécutez le programme

Options?

Affichage fenêtre graphique: 

-Si vous souhaitez afficher uniquement le meilleur individu de la population finale(option par défaut): mettre en commentaire la ligne 488 et décommenter la ligne 486 "nouvellePop.meilleurIndividu()"

-Si vous voulez afficher la population finale entière: mettre en commentaire la ligne 486 et décommenter la ligne 488 "nouvellePop.drawPop()"

Sauvegarde fichiers csv:

-Si vous voulez sauvegarder les statistiques de coût: mettre la variable saveStats à True (ligne 21)

-Si vous voulez sauvegarder les statistiques de temps d'exécution: mettre la variable saveTmpExec à True (ligne 22)

Réglages:

-Si vous souhaitez changer le glyphe à approximer il suffit de changer la valeur de la variable lettre (ligne 13)

-Si vous souhaitez modifier le nombre de générations de population à générer vous pouvez changer la valeur de la variable nbGeneration (ligne 10)

-Si vous souhaitez changer le nombre de gènes par individus vous pouvez modifier la valeur de la variable nbRect (ligne 11)

-Si vous souhaitez modifier la proportion d'individus sélectionnés, engendrés par reproduction croisée ou mutés vous pouvez moddifier les valeurs 
des variables nbSelection, nbReproCroisee, nbMutation (lignes 17-19) attention cependant! la somme des 3 doit être égale à la valeur de indParPopulation.

-Si vous souhaitez changer le coeficient de mutation (coefficient minimum du coût initial de l'individu à atteindre après mutation) il suffit de modifier
la valeur de la variable coefMutation (ligne 20) en lui donnant une valeur entre 0 et 1. Plus le coefficient est élevé plus le résultat est bon, 
mais plus le temps d'exécution augmente.

