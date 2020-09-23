

# TP2

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 27 septembre 2020 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

Ce TP poursuit votre apprentissage à l'algorithmie avec le langage de programmation Python.
Celui-ci est composé de 5 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir téléchargé les fichiers exercices1-5.py que vous devrez compléter.
Pour ce TP, vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.


## Exercice 1:
Tri : Écrire un programme qui saisit un tableau d’entiers (pas de vérification nécessaire) de taille 10 et le trie. Le tri est fait en trouvant le plus petit élément entre la case 0 et 9 et en inversant ce minimum avec la case 0. Ensuite, il doit trouver le plus petit élément entre la case 1 et 9 et inverser ce minimum avec la case 1 et ainsi de suite. Le programme doit ensuite afficher le tableau trié.
Exemple d’affichage :
Entrez dix nombres entiers : 8 4 12 58 3 9 7 8 11 1
Voici le tableau trie : 1 3 4 7 8 8 9 11 12 58

## Exercice 2:


## Exercice 3:
Hauteur de rebond : Écrivez un programme qui détermine la hauteur atteinte par une balle en tenant
compte de la hauteur initiale et du nombre de rebonds. Les données à demander et à lire du clavier sont
donc : la hauteur initiale, le nombre de rebonds au bout duquel on souhaite connaître la hauteur de la balle,
ainsi que le coefficient de rebond. Vous devrez vérifier la validité des données entrées par l’utilisateur
(hauteur et nombre de rebonds positifs, et coefficient compris entre 0 et 1) et réutilisant la fonction écrite
à la question précédente.
Les variables sont les suivantes :
- hi est la hauteur avant le rebond numéro i, et hi+1 la hauteur après le rebond numéro i.
- vi est la vitesse de la balle avant le rebond numéro i, et vi+1 est la vitesse après le rebond.
Les relations entre les variables sont les suivantes :
-  = 2 ∙  ∙ ℎ , avec g la constante de gravité égale à 9,81 dans notre cas.
-  = 2 ∙  , avec c le coefficient de rebond.
- ℎ = 

∙
Utilisez une structure de répétition pour répéter le calcul autant de fois qu’il y a de rebonds souhaités.
Vous ne devez pas utiliser de tableau.

## Exercice 4:
Approximation de pi : Écrivez un programme qui permet de calculer une valeur approchée de pi par la
méthode de Monte‐Carlo basée sur les probabilités.
L’idée est la suivante : si on insère un cercle de rayon 1 (ce qui correspond à une aire de pi) dans un carré
de côté 2 (et donc d’aire 4), la probabilité qu’un point placé aléatoirement dans le carré soit également
dans le cercle est pi/4 (le rapport des aires).
Voici donc ce qu’il faut faire :
- Vous allez générer deux nombres réels aléatoires x et y, tous deux compris entre -1 et 1.
- Si x2 + y2 < 1 , le point est dans le cercle.
Il faut donc demander et lire du clavier le nombre d’itérations souhaité, puis afficher la valeur approchée
de pi par cette méthode puis l’écart relatif entre cette valeur approchée et la valeur précise à 10−6 :
3,141593. Vous veillerez à afficher votre valeur approchée avec une précision de 6 chiffres après la
virgule.
Vous devez utiliser les fonctions srand() et rand() pour la génération de nombres aléatoires. Ces fonctions
exigent d’inclure les fichiers cstdlib et ctime (voir le programme dans la « Question 4 » des « Exercices
sur les variables (II) » sur Moodle). Écrivez une fonction pour générer un nombre aléatoire entre -1 et 1.

## Exercice 5:
Dans cet exercice, vous allez participé à la conception d'un système de filtrage des spams <b>RENEGE</b> (use<b>R</b> awar<b>E</b> bayesia<b>N</b> filt<b>E</b>rin<b>G</b> syst<b>E</b>m). Ce système permet d’étiqueter les e-mails en déduisant si ce sont des c<b>spams</b> (non désirés) ou des <b>hams</b> (messages ok).  Il s’agit essentiellement d’un classificateur bayésien associé à des règles heuristiques. 

Vous ne devrez pas implémenter l'entièreté du système, mais simplement créer un vocabulaire qui sera utilisé pour entrainer les algorithmes d'intelligence artificielle de RENEGE. Dans le fichier email.json, vous avez une liste de 1000 emails, avec les atributs suivant:
- <b>From</b>: le destinataire de l'email.
- <b>Date</b>: la date de l'email.
- <b>Body</b>: la liste des mots qui sont contenus dans l'email.
- <b>Spam</b>: si la valeur est 'true', l'email est un Spam, sinon c'est un Ham.

Le fichier email.json à été sauvegardé dans la variable 'emails' sous forme d'une liste de dictionnaire avec la fonction 
```python
        with open('email.json') as json_data:
            emails = json.load(json_data)
```
Voici à quoi ressemble la structure de la variable <b>emails:</b>
<p align="center">
     <img alt="figure 6.1" src="img/new1.PNG?raw=true"/>
</p>
Vous devez calculer, pour les mots du <b>Body</b> de chaque mails, la probabilité que le mot soit dans un <b>spam</b> ou dans un <b>ham</b>. Par exemple, la probabilité qu'un mot soit dans un <b>spam</b> se calcule ainsi: 
<p align="center">
     <img src="img/spamss.PNG?raw=true"/>
</p>
De l'autre coté, la probabilité qu'un mot soit dans un <b>ham</b> se calcule ainsi:
<p align="center">
     <img src="img/hams.PNG?raw=true"/>
</p>
Finalement ses probabilités seront insérés dans un dictionnaire où l'on distiguera le résultat pour les spams de ceux des hams ainsi:
<p align="center">
     <img title="figure 6.2" src="img/new2PNG.PNG?raw=true"/>
</p>
votre résultat final sera injécté dans fichier results.json, avec la fonction:

```python
        with open('results.json', 'w') as fp:
            json.dump(result, fp, indent=4)
```
Où la variable result contient le dictionnaire en question.

Voici à quoi ressemble la fonction à compléter:


```python
        def createVocabulary():
            #les mails contient la structure de donnée présente dans mail.json
            with open("mails.json") as json_data:
                email = json.load(json_data)
                
           #TODO: Affécté à la variable 'result' le résultat final
           
            result = {}
            with open('results.json', 'w') as fp:
                json.dump(result, fp, indent=4)         
```

Vous etes libre de créer de nouvelles structures de données et d'implémenter d'autre fonctions si cela clarifie le code. La fonction createVocabulary() doit avoir un temps d'éxécution acceptable.












