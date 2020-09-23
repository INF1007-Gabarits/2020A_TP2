

# TP2

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 27 septembre 2020 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

Ce TP poursuit votre apprentissage à l'algorithmie avec le langage de programmation Python.
Celui-ci est composé de 5 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir téléchargé les fichiers exercices1-6.py que vous devrez compléter.
Pour ce TP, vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.


## Exercice 1:
Écrire un programme qui saisit un tableau d’entiers et le trie. Attention, vous ne pouvez pas utiliser de fonction de tri, et toutes les manipulations doivent se faire sur un seul tableau. Le programme doit ensuite afficher le tableau trié.

```python
        def exercice1(tableau):
            #TODO: trier le tableau

            return tableau

        if __name__ == '__main__':
            #Voici un exemple de tableau à trier:
            tableau_a_trier = [2,4,6,4,6,7,8,9,7,5,4,3]

            resultat = exercice1(tableau_a_trier)
            print(resultat)
```


## Exercice 2:


Dans cet exercice, le mot expression désigne une chaîne de caractères ne contenant que des parenthèses ouvrantes et fermantes comme par exemple "(()())", "(()()" et "(()))(".
Une expression est bien parenthésée si le nombre de parenthèses ouvrantes est égal au nombre de parenthèses fermantes, et si quelque soit la position dans l'expression, le nombre de parenthèses ouvrantes qui précèdent cette position est toujours supérieur ou égal au nombre de parenthèses fermantes qui précèdent.

• "(()())" est une expression bien parenthésée.

• "(()()" est mal parenthésée car il y a 3 parenthèses ouvrantes et 2 parenthèses fermantes seulement.

• "(()))()" est mal parenthésée car le cinquième caractère est la troisième parenthèse fermante, alors qu'il n'y a que deux parenthèses ouvrantes qui précèdent.


Dans cet exercice l'utilisateur vas entrer une expression, si l'expression est mal parenthésée, la fonction retourne "Incorrect", sinon elle retourne la meme expresion, mais en insérant des '.' à chaque fois qu'une parenthèse ouvrante et suivi d'une parenthèse fermante. Voici un exemple pour illustrer ce que l'on attends:
<p align="center">
     <img src="img/exo2.png?raw=true"/>
</p>

 

## Exercice 3:
Ici vous devez Écrire un programme qui détermine le nombre de rebonds effectuer par la balle avant que la hauteur du rebond soit inferieure à 0.01 mètre. Les données à demander et à lire du clavier: la hauteur initiale, le coefficient de rebond. 
Les variables sont les suivantes :

<img src="https://render.githubusercontent.com/render/math?math=h_{i}"> est la hauteur avant le rebond numéro <img src="https://render.githubusercontent.com/render/math?math=i">, et <img src="https://render.githubusercontent.com/render/math?math=h_{i+1}"> la hauteur après le rebond numéro <img src="https://render.githubusercontent.com/render/math?math=i">.

<img src="https://render.githubusercontent.com/render/math?math=v_{i}"> est la vitesse de la balle avant le rebond numéro <img src="https://render.githubusercontent.com/render/math?math=i">, et <img src="https://render.githubusercontent.com/render/math?math=v_{i+1}"> est la vitesse après le rebond <img src="https://render.githubusercontent.com/render/math?math=i">.

Les relations entre les variables sont les suivantes :

<img src="https://render.githubusercontent.com/render/math?math=v_{i}"> = <img src="https://render.githubusercontent.com/render/math?math=$\sqrt{2*g*h_{i}}$">, avec <img src="https://render.githubusercontent.com/render/math?math=g">  la constante de gravité égale à <img src="https://render.githubusercontent.com/render/math?math=9.81"> dans notre cas.

<img src="https://render.githubusercontent.com/render/math?math=v_{i+1}"> = <img src="https://render.githubusercontent.com/render/math?math=v_{i}*c"> avec c le coefficient de rebond.

<img src="https://render.githubusercontent.com/render/math?math=h_{i+1}"> = <img src="https://render.githubusercontent.com/render/math?math=(v_{i+1})^2/2*g"> 
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
Il faut faire ainsi  jusqu'à qu l’écart relatif entre cette valeur approchée et la valeur précise à 10−3 :
3,141xxxx. 

Vous veillerez à afficher votre valeur approchée avec une précision de 4 chiffres après la
virgule, ainsi que le nombre d'itérations que le programme a pris.
Vous devez utiliser la fonctions random() pour la génération de nombres aléatoires. 

## Exercice 5:

```python
        def multiplierMatrices(A, B):

            #TODO: Si les matrices ne peuvent pas etre multipliées, affecter à C une matrice nulle [nbLignesA x nbColonnesB]
            C =



            #TODO: Sinon faire la multiplication et mettre dans C le résultat
            C =

            return C

```

```python
        def matriceZero(nbLignes, nbColonnes):
            A = []

            #TODO: Remplir la matrice A de 0, selon les dimensions données

            return A
```
## Exercice 6:
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

Vous etes libre de créer de nouvelles structures de données et d'implémenter d'autre fonctions si cela clarifie le code. La fonction createVocabulary() doit avoir un temps d'éxécution acceptabl e.












