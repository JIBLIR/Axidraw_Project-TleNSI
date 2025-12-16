## Methodologie

### Pour le réseau:
Notre architecture réseau est composé d'un client et d'un serveur.
Pour le client, nous avons utiliser la méthode POST du module request ainsi que les adresses IP des ordinateurs en réseau afin de permettre la connection et transférer le svg.
Ainsi, on choisi l'url du serveur ainsi qu'un fichier svg et cela est transférer au serveur.

Pour le serveur, nous utilisons cherrypy, os et axidraw. 
Avec cherrypy nous créons un serveur web accessible partout sur le réseau et nous vérifions si un fichier svg est disponible.
Si un fichier et disponible (via os) on l'enregistre et on l'imprime, le module axidraw s'occupant de la conversion svg à action.

