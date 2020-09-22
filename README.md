# TP2

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 27 septembre 2020 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

Ce TP poursuit votre apprentissage à l'algorithmie avec le langage de programmation Python.
Celui-ci est composé de 5 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir téléchargé les fichiers exercices1-5.py que vous devrez compléter.
Pour ce TP, certaines contraintes sont à respecter:
- Vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.


## Exercice 1:


## Exercice 2:

## Exercice 3:

## Exercice 4:

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
            email = json.load(json_data)
```
voici à quoi ressemble la structure de la variable <b>emails:</b>
<p align="center">
     <img src="img/new1.PNG?raw=true"/>
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
     <img src="img/new2PNG.PNG?raw=true"/>
</p>
votre résultat final sera injécté dans fichier results.json, avec la fonction:
```python
        with open('results.json', 'w') as fp:
            json.dump(vocabulary, fp, indent=4)
```

