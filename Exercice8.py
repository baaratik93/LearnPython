# Demander des informations concernant l’étudiant tant que l’utilisateur désire continuer.
# Vous devez demander le téléphone, nom, prénom, classe, note de devoir, note de projet et
# note d’examen pour ensuite calculer la moyenne et afficher le résultat sous forme du tableau
# ci- dessous lorsque l’utilisateur terminera sa saisie.
# Le numéro de téléphone doit être unique et doit répondre aux critères définis dans l’exo 4
# Les notes et la moyenne sont des décimales à 2 chiffres comprises entre 0 et 20.
# Ci-dessous un tableau vous montrant l’affichage comme il se doit.
# Contraintes techniques
# ● Vous utiliserez une page ou vous mettrez toutes vos fonctions et vous les appelez dans
# les autres pages.
# ● Dès l’exécution de votre fichier vous devez avoir un menu comme suit:
# ○ Afficher tout
# ○ Trier et afficher (par ordre décroissant de la moyenne)
# ○ Rechercher selon un critère (téléphone, nom, prénom ou classe)
# ○ Modification de notes pour un étudiant choisit par l’utilisateur en donnant le
# numéro de téléphone.
# ○ Sortir (permet de terminer l’application)
# ● A chaque fois que vous terminez avec une étape (1 à 5) vous devez réafficher le menu
# ● Tous les affichages doivent se faire sous forme de tableau
# ● Tous les contrôles de saisie doivent être faits par vos propres fonctions.
from fn.functions import Menu

e = [
        {
            "prenom": "Mamadou",
            "nom": "Thiam",
            "telephone": 776280909,
            "classe":"L1",
            "dev":12.75,
            "projet":15.45,
            "exam":14.25,
            "moy":0.0
        },
        {
            "prenom": "Fama",
            "nom": "Mbow",
            "telephone": 776549987,
            "classe":"L1",
            "dev":10,
            "projet":10,
            "exam":10,
            "moy":0.0
        },
        {
            "prenom": "Demba",
            "nom": "BA",
            "telephone": 789854432,
            "classe":"L1",
            "dev":10,
            "projet":10,
            "exam":10,
            "moy":0.0
        },
        {
            "prenom": "Oumy",
            "nom": "DIAW",
            "telephone": 769453476,
            "classe":"L1",
            "dev":10,
            "projet":10,
            "exam":10,
            "moy":0.0
        }
    ]
# Saiisie des informations l'étudiant
# Controler la saisie d'informations
# Gérer les fonctions externes
# Gêrer le menu
# Trie et affichage
# Recherche selon le critère
# Modification de note pour un étudiant
# Sortir de l'application
# Gestion de la navigation
Menu(e)