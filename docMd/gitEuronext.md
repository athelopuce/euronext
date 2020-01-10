# GIT<a id="gitEuronext"></a>
    *[Retour sommaire](#Sommaire)\
    <a id="titre"></a>
    *[Retour sommaire](#Sommaire)\
    [Titre](#lien)\

## Sommaire<a id="gitEuronext_Sommaire"></a>
---
[Historique](#gitEuronext_Historique)\
[MODIFIER](#gitEuronext_Modifier)\
[BRANCHES](#gitEuronext_BRANCHES)\
[LOG](#gitEuronext_LOG)\
[TAG](#gitEuronext_TAG)\
[COMMIT](#gitEuronext_COMMIT)\
[CLONE](#gitEuronext_CLONE)\
[CONFIGURER](#gitEuronext_CONFIGURER)\
[GIT SUR LE SERVEUR KEY USB](#gitEuronext-GIT_SERVEUR_SUR_KEY_USB) \
[PULL](#gitEuronext_PULL)\
[PUSH](#gitEuronext_PUSH) \
[Code sommaire](#gitEuronext_Codesommaire)

### Historique<a id="Historique"></a>
```
    git init
    echo "# euronext" >> README.md
    git add README.md
    git add Release.md
    git commit -m "first commit"
    git add gitEuronext.txt
    git reset HEAD
    git status
    git commit --amend
    git reset --soft HEAD^
    
    git add README.md
    git add Release.md
    git add gitEuronext.txt
    git status
    git commit -m "first commit"
    git remote add euronext https://github.com/dhazel38/euronext.git
    
    git pull
    git tag -a v1.0 -m 'version initiale'
    
    git commit -m "New organisation de l'appli Flask appEuro"
    git tag v1.0.0
    git branch demarrer_Flask
    git commit -m "avant nouvelle branche"
    git checkout demarrer_Flask

    git add tests/
    git add appEuro/
    
    git push -u euronext master --tags
    git clone \.git ../EuronextClone
    ... passe sur EuronextClone
    git commit -a
    git push
    ... revient sur Euronext - branche
    git merge demarrer_Flask
    git branch -d demarrer_Flask
    ... mettre à jour master de EuronextClone
    cd ../EuronextClone
    git checkout master
    git pull
    git branch -d demarrer_Flask
    ... revient sur Euronext - master
    cd ../Euronext
    # créer une nouvelle branche demarrer_FlaskV2
    git branch dev
    git checkout dev
    git rm Release.md
    git clone \.git ../Euronext_dev
    
```
---
*[Retour sommaire](#gitEuronext_Sommaire)\
# MODIFIER<a id="gitEuronext_Modifier"></a>

## code et effectuer des commits
**Faire appel** à  `git add`  est **indispensable** lorsque vous venez de créer de nouveaux fichiers que Git ne connaît pas encore. 
Cela lui permet de les prendre en compte pour le prochain commit.

**après modif**

    git status
    git add -u   // Update

**visualiser un fichier modifié**

    git diff tests/__init.py__

* pour « commiter » tous les fichiers qui étaient listés dans  git status
     `git commit -a`

* fichiers nouveaux
```
git add nomfichier1 nomfichier2, puis
git status, puis
git commit
```
* fichiers connus
```
git commit nomfichier1 nomfichier2
```

**Rename**

    git mv trading_test.py test_trading.py

## Add et delete of Git
Supprimer des fichiers de la branche dev

    (dev)...
    git rm Release.md
    git rm euronext_service_tuto.txt
    git rm setuputils.md
    git rm README.md
    git rm appFlask.md

---
*[Retour sommaire](#gitEuronext_Sommaire)\
# BRANCHES<a id="gitEuronext_BRANCHES"></a>
**Créer une branche**

    git branch demarrer_FlaskV2

Crée une branche cs et remote origin correctionserveur

    git checkout -b cs origin/correctionserveur
    
Remote push pull configurer option -u ou --set-upstream-to

    git branch -u origin/correctionserveur
    git branch --set-upstream-to origin/correctionserveur
    git branch -vv

**Changer de branche**

    git commit -a -m "avant nouvelle branche"
    git checkout demarrer_Flask
    
ou

     git checkout -b firstProg  // créer la branche et switch

**Demandez ensuite à y intégrer** le travail que vous avez fait dans « demarrer_Flask » :

    git merge demarrer_Flask

**Gestion des conflits**

    git fletch ** a revoir
    git mergetool

**Effacer une branche**

    git branch -d demarrer_Flask

**Commandes utiles**

    git branch -v ; détail des branches

    git branch --merged 
    indique uniquement les branches qui ont déjà été fusionnées.
    
    git branch --no-merged 
    indique uniquement les branches qui n'ont pas encore été fusionnées.

## Branches de suivi à distance
https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Branches-de-suivi-%C3%A0-distance

    git ls-remote
    git remote show


---
*[Retour sommaire](#gitEuronext_Sommaire)\
# LOG<a id="gitEuronext_LOG"></a>
**les logs**

    git log
    git log -p // par page
    plus court des commits avec:
    git log --stat

    git log --pretty=oneline

Pour voir où les branches pointent : --decorate.

    git log --oneline --decorate
    git log --oneline --decorate --graph --all


---
*[Retour sommaire](#gitEuronext_Sommaire)\
# TAG<a id="gitEuronext_TAG"></a>
A best practice is to consider Annotated tags as public, and Lightweight tags as private

**Annotated tag:**

    git tag -a v1.0 -m 'version initiale'

**Lightweight tag**

    git tag v1.0.0
    git tag v1.0.0-rc

**Tager un old commit**

    git tag -a v1.2 bee37ce

**Pour supprimer un tag créé**

    git tag -d NOMTAG

**Recharger une ancienne version**

    git checkout v1.4
    git switch - // annuler et revenir à la version précédente

**list**

    git tag
    git log --pretty=oneline

**Filtrer**

    git tag -l *-rc*
    
    git show someTagValue 
    renvoie les informations du tag et une description du commit associé.

---
*[Retour sommaire](#gitEuronext_Sommaire)\
# COMMIT<a id="gitEuronext_COMMIT"></a>

    git add gitEuronext.txt
    git status
    git commit -m "text des modications"

## Modifier le dernier message de commit

    git commit --amend

## Annuler le dernier commit (soft)
**Si l'on juge que les 3 dernières versions**
n'étaient pas bonnes et que l'on souhaite tout annuler

    git reset HEAD~3

**Delete si first commit**

    git update-ref -d HEAD
    git rm --cached -r .  // ne pas oublier le point

**Si vous voulez annuler votre dernier commit**

    git reset HEAD^

Seul le commit est retiré de Git ; vos fichiers, eux, restent modifiés.

### Annuler un commit plus ancien après un push

mettre n° du commit précédant celui à éditer \

    git rebase --interactive 39140650eb976
    
Il convient alors de remplacer *pick* par **reword** pour chaque commentaire de commit à corriger. Une fois ces modifications effectuées, git va lancer une session texte pour chaque commentaire.\
Si erreur faire: `git rebase --abort`

    git rebase --continue
    
modifier la ligne

## Annuler tous les changements du dernier commit (hard)
Cela annulera sans confirmation tout votre travail ! \
 **Faites donc attention** et vérifiez que c’est bien ce que vous voulez faire !

    git reset --hard HEAD^   /!\ Annule les commits et perd tous les changements

**Annuler les modifications d’un fichier avant un commit**

    git checkout nomfichier

**Annuler/Supprimer un fichier avant un commit**\
Après un git add fichier_à_ajouter, et avant commit

    git reset HEAD -- fichier_a_supprimer

## Git rm --cached
On utilise `git rm --cached <fichier>` pour sortir de l'index un fichier suivi par git mais qui n'est pas modifié (c'est indiqué dans la doc via cette phrase : The files being removed have to be identical to the tip of the branch) tout en le conservant sur le disque,


---
*[Retour sommaire](#gitEuronext_Sommaire)\
# CLONE<a id="gitEuronext_CLONE"></a>
Copie conforme de l'original.
## Clone dans EuronextGit

    git clone https://github.com/dhazel38/euronext.git

## Suivre les modifications

    gitk --follow Release.md

## Clone en local

    Utilisateur@DELL_E6410 MINGW64 ~/Documents/Python Scripts/Euronext (demarrer_Flask)
    git clone \.git ../EuronextClone
    
### Tenir à jour le clone

*git pull* pour maintenir à jour une copie locale d'un dépôt de référence

    git pull   // depuis le clone

**Pour récapituler :** \
Le dépôt de référence fait donc un cycle classique :
1. modifications,
1. git add,
1. git commit.

Le dépôt clone se maintient à jour en faisant "git pull".

### git push pour propager sur le dépôt d'origine les modifications que vous avez faites en local
**Pour récapituler :** \

* depuis le dépôt clone
1. n'oubliez pas de commencer par un "git pull" pour être certain de partir de la dernière version de référence
1. créez une nouvelle branche avec git checkout -b nomNouvelleBranche
1. faites un ou plusieurs cycles classiques
 * modifications,
 * git add
 * git commit
1. faites un "git push" (comme nous l'avons vu précédemment, il est possible de faire plusieurs cycles de "commit" atomiques puis un "git push" lorsque l'on est satisfait)

* depuis le dépôt origine
1. assurez-vous d'être sur la bonne branche (par exemple master) avec un "git checkout nomBonneBranche"
1. faites un "git merge nomNouvelleBranche" de la branche que vous venez de pousser depuis le dépôt clone
1. résolvez les conflits éventuels (cf. section suivante)
1. faites un "git branch -d nomNouvelleBranche" pour supprimer la  branche qui est devenue inutile maintenant que vous l'avez intégrée

* depuis le dépôt clone
1. repassez dans la bonne branche (par exemple master)
1. faites un "git pull" pour récupérer la dernière version à jour avec les modifications que vous venez de pousser, les modifications éventuelles d'autres utilisateurs et la résolution des conflits éventuels.
1. faites un "git branch -d nomNouvelleBranche" sur la nouvelle branche pour la supprimer également


---
*[Retour sommaire](#gitEuronext_Sommaire)\
# CONFIGURER<a id="gitEuronext_CONFIGURER"></a>
## fichier .git/info/exclude
Voir [fichier exclude](gitExclude.md)

## Configurer

    git config --global user.name "dhazel38"
    git config --global user.email dhazel@free.fr

    vim ~/.gitconfig

### Créer un nouveau dépôt

    cd "Documents\Python Scripts\Tuto"
    mkdir git_plusoumoins
    cd git_plusoumoins

    git init

### Push
**Créer un Repertory** \
https://github.com/repositories/new

**Crée un remote nommé** \
"essai1" pointant votre dépôt GitHub

    git remote add essai1 https://github.com/dhazel38/essai1.git
    git remote -v

**renomer:** `git remote rename essai1 essai2`
**retirer:** `git remote rm proj1`

**Envoie vos commits** \
dans la branche "master" sur GitHub

    git push [nom-distant] [nom-de-branche]
    git push -u essai1 master


---
*[Retour sommaire](#gitEuronext_Sommaire)\
## GIT SUR LE SERVEUR KEY USB<a id="gitEuronext-GIT_SERVEUR_SUR_KEY_USB"></a>
### Remote git
**Remote Repository** : Le Remote Repository est le dépôt distant \
**Local Repository** : Le Local Repository est le dépôt local. C'est le dossier .git stocké dans votre espace de travail. 

**CAP1*: key de sauvegarde CAP1 Droite\
**key*:  Key sauvegarde normale\
**backup*: ordinateur ..Documents/Python Scripts/Euronext/.git\
**origin* : remote Repository - serveur github

    # sur la clé
	cd /opt/git
	cd /Git
    mkdir euronext.git
    cd euronext.git
    git init --bare

    # Sur l'ordinateur
    git remote add CAP1 E:/Git/euronext.git
    git push CAP1 master
	git push CAP1 --all
	git remote -v
	
	# pour key
	git remote add key F:/Git/euronext.git
    git push key --all
    
    # git remote -v sur ordinateur
    CAP1    E:/Git/euronext.git (fetch)
    CAP1    E:/Git/euronext.git (push)
    backup  C:/Users/Utilisateur/Documents/Python Scripts/Euronext/.git (fetch)
    backup  C:/Users/Utilisateur/Documents/Python Scripts/Euronext/.git (push)
    key     F:/Git/euronext.git (fetch)
    key     F:/Git/euronext.git (push)
    origin  https://github.com/dhazel38/euronext.git (fetch)
    origin  https://github.com/dhazel38/euronext.git (push)
	
**Enlever un remote(dépôt distant):** `git remote remove CAP1`

**Gestion conflis**

	git push origin  // probleme
	git log --oneline --decorate --graph --all

	git fetch origin master
	git log --oneline --decorate --graph --all
	
	git pull origin master
	git status
	git commit -a
	git push origin master
    
### Cloner le dépôt de sauvegarde

    cd emplacement désiré
	cd "C:\Users\Utilisateur\Documents\Python Git"
	git clone F:/Git/euronext.git
	cd euronext
	git remote -v
	...
	origin  F:/Git/euronext.git (fetch)
	origin  F:/Git/euronext.git (push)
    
    git branch -a
    ...
    remotes/origin/HEAD -> origin/master
    remotes/origin/dbModif1
    remotes/origin/master
    
    git checkout dbModif1


---
*[Retour sommaire](#gitEuronext_Sommaire)\
# PULL<a id="gitEuronext_PULL"></a>
**descente du serveur**

    git pull


---
*[Retour sommaire](#gitEuronext_Sommaire)\
# PUSH<a id="gitEuronext_PUSH"></a>
**push sauve sur serveur**

    git push -u euronext master --tags


### Code sommaire<a id="gitEuronext_Codesommaire"></a>

    *[Retour sommaire](#appFlask_Sommaire)\
    <a id="titre"></a>
    *[Retour sommaire](#appFlask_Sommaire)\
    [Titre](#appFlask_lien)\
