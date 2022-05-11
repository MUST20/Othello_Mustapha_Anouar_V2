# Othello_game 
Intelligence artificielle pour le jeu Othello

Pour lancer le serveur de jeu : cloner le répertoire de l'enseignant : https://github.com/qlurkin/PI2CChampionshipRunner

Exécuter la commande suivante dans le répertoire cloné :

$ python server.py othello

Pour lancer le client :

$ python ClientIA.py [port]  

Stratégie :

Calculer tous les mouvements possibles , pour ceci on a utilisé les fonctions de prof. On a ensuite rajouté une intelligence qui consiste à calculer le nombre de pions à éliminer pour chaque mouvement possible. Donc on aura 2 listes qui ont la même longueur et qui correspondent aux mouvements possibles et au nombre des pions à éliminer. On calcule le maximum de la liste PawnsDestroyed ainsi l'indice de ce maximum et on prend le mouvement correspondant comme BestMove. La fonction SendMove sert à envoyer le mouvement à faire comme réponse à la requête "play", ou à envoyer Null si aucun mouvement n'est possible ( la liste PossibleMoves est vide).

Bibliothèques utilisées :

socket : pour faire les communications avec le serveur

JSON : pour envoyer du JSON au serveur

sys : pour utiliser d'éventuels arguments lors de l'exécution du client et définir un port

time : afin de pouvoir calculer le temps pour trouver le meilleur move
