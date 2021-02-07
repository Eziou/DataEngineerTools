# Rapport du Projet "Data Engineering"

## Installer et Lancer

Pour clone l'environnement, utiliser la command 
```
pip install -r requirement.txt 
conda env create -n <nom> -f conda_environment.yml
```

#### Lancer votre MongoDB


Dans votre terminal, taper le commande:

```
mongod --dbpath="<directory du projet>+/data"
```

#### Lancer le scrapy

Au début, vous devez entrer le dossier`/Projet/channels/`

Commandes:

```
scrapy crawl channelsSpi
```

Comme le website a utiliser le technologie de javascript pour dynamique presentation, donc on doit utiliser le Selenium simuler le navigateur pour scrapy.

#### lancer le Flask application

Entrer le dossier `/Projet/Twitch/`

Commandes:

```
python3 views.py
```



## Le contenu de notre projet

On crée un environnement virtuel qui contient des packages et Python interpréteur. Dans "Projet/Twitch/", '/templates' dossier contient des modèles HTML, et '/static' dossier contient ''/css' et '/js' qu'on utilise pour personnaliser des html pages plus commode.

'/views.py' est un fichier qui permet de servir des pages html.

On utilise le package 'pyecharts' pour visualiser des données qu'on a obtenu de Twitch.tv. Et ranger les jeux par le nombre de spectateurs.



## Le fonctionnement du projet

Vous pouvez chercher des chaînes les plus populaires sur Twitch, et récuperer quels jeux sont les plus populaires en ce moment. vous pouvez accéder à Twitch.tv via le lien.