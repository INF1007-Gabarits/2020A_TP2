# TP1

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
Dans cet exercice, vous allez participer à la conception d'un système de filtrage des spams <b>RENEGE</b> (use<b>R</b> awar<b>E</b> bayesia<b>N</b> filt<b>E</b>rin<b>G</b> systEm). Ce système permet d’étiqueter les e-mails comme <b>spam</b> (non désirés) et <b>ham</b> (messages ok).  Il s’agit essentiellement d’un classificateur bayésien associé à des règles heuristiques. Il est composé de plusieurs modules qui traitent la classification du spam et du ham. 

Nous n'allons pas nous demandez d'implémenter le système RENEGE mais simplement de créer un vocabulaire qui sera utilisé pour entrainer les algorithmes d'intelligence artificielle de RENEGE. Dans le fichier email.json, vous avez une liste de 1000 emails, avec les atributs suivant:
- <b>From</b>: le destinataire de l'email.
- <b>Date</b>: la date de l'email.
- <b>Body</b>: la liste de mots qui sont contenus dans l'email (excluant les pronoms).
- <b>Spam</b>: si la valeur est 'true', l'email est un spam, sinon c'est un Ham.

Le fichier email.json est sous la forme d'une liste de dictionnaire que nous avons sauvegarder dans la variable 'emails' avec la fonction 
```python
        with open('email.json') as json_data:
            email = json.load(json_data)
```
voici à quoi la structure de la variable <b>email:</b>
```python
        def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

            module = trouverModule(nombreComplexe)
            angle = trouverAngle(nombreComplexe)

            # TODO: Afficher le module et l'angle du nombre complexe (3 decimales de précision)


            # TODO: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'

            resultat =

            nouveauModule = trouverModule(resultat)
            nouvelAngle = trouverAngle(resultat)

            # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)

            return resultat
```
Si votre programme a été correctement écrit, vous devriez voire une simulation visuelle du nombre complexe avant et apres rotation:
<p align="center">
     <img src="img/complexe.PNG?raw=true"/>
</p>

