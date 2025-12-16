# importation des bibliothèques
import requests 

url = "http://172.16.100.30:5432/recevoir"

def imprimer_svg_client(svg,url):
	'''envoie sur le serveur le fichier svg pour imprimer'''

	# création du dictionnaire "chaine" contenant le svg
	chaine = {'message' : svg}
	# transfert du svg au serveur
	response = requests.post(url, data = chaine)
	# retourne la reponse
	return response.text
