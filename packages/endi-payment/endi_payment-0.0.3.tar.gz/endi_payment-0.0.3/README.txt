Endi : Module paiement
=======================

Ce module a pour objectif de fournir une librairie cloisonnée de manipulation
et de journalisation des encaissements.

Les techniques de cloisonnement :

    -  Séparation du code en chaarge de l'insertion, de la mise à jour et de la
       suppression des paiements du code générale d'Endi (Autonomie).
    -  Journalisation des actions menées sur les encaissements;
    -  Possibilité d'utiliser une connexion mysql séparée pour la
       journalisation.


Mise en place d'une base de données dédiée
-------------------------------------------

Utilisez le script ci-joint pour créer une base de données dédiée.

Celui-ci

-  Crée la base de données
-  Crée un utilisateur spécifique
-  Affecte des privilèges restreints à l'utilisateur spécifique

Liste des privilèges octroyait par le script

- CREATE : L'utilisateur peut créer des tables
- INSERT : L'utilisateur peut écrire dans la base de données
- SELECT : L'utilisateur peut lire dans la base de données

L'utilisateur ne peut donc pas modifier le contenu existant de la base de
données.
