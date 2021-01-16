# Overview

L'objectif de ce repository est la récupération des verbatims du *Ben Shapiro Show* sur YouTube. Ben Shapiro est un commentateur politique américain, proche des républicains et qualifié de conservateur. Il anime quotidiennement depuis plus de trois ans, un  podcast intitulé *The Ben Shapiro Show* dans lequel il donne son avis sur l'actualité politique américaine. La collecte de ces données peut servir à différentes tâches NLP, comme : 
 * Identifier ses interventions publicitaires
 * Retracer l'histoire politique de l'amérique du point de vue d'un conservateur, reconstituez les grands événements, leurs durées, leurs intensités, etc.
 * Identifier les moments *chauds* avec l'analyse des commentaires et les moments plus *calmes*

<img src="img/benshap.jpg" width="512">


# Références

Les packages utilisés dans ce repository sont les suivants : 
 * [youtube-dl](https://github.com/ytdl-org/youtube-dl)
 * [download-youtube-subtitle](https://github.com/xsthunder/download-youtube-subtitle)
 * [youtube-comment-downloader](https://github.com/egbertbouman/youtube-comment-downloader)


# Environnement Conda

Les applications tournent sur un environnement conda nommé *music*. Afin de le reproduire :

```
conda env create -f environment.yml
conda activate music
```

# Partie 1, récupération des urls du podcast **The Ben Shapiro Show**

Téléchargement des urls de la playlist *The Ben Shapiro Show* dont l'id est *PLX_rhFRRlAG58_4z9KWPUYrnTM6QZDJrT*. L'output est le fichier `urls`. D'après [youtube-dl](https://github.com/ytdl-org/youtube-dl) :

```
conda activate music
(music) bash grabb_urls.sh PLX_rhFRRlAG58_4z9KWPUYrnTM6QZDJrT urls
```

# Partie 2, récupération des commentaires

Téléchargement (dans le dossier `/comments`) des commentaires dans le dossier des vidéos dont les urls se trouvent dans le fichier `urls`. D'après [youtube-comment-downloader](https://github.com/egbertbouman/youtube-comment-downloader) :

```
conda activate music
(music) bash grabb_comments.sh urls comments
```

# Partie 3, récupération des verbatims

Téléchargement (dans le dossier `/verbatims`) des verbatims des vidéos dont les urls se trouvent dans le fichier `urls`. D'après [download-youtube-subtitle](https://github.com/xsthunder/download-youtube-subtitle) :

```
conda activate music
(music) python grabb_captions.py -f urls -s verbatims
```
