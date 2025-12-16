"""
Source - https://stackoverflow.com/a
Posted by Tola, modified by community. See post 'Timeline' for change history
Retrieved 2025-12-02, License - CC BY-SA 4.0
"""
from pyaxidraw import axidraw   
import cherrypy 
import os

def index():
	return "Hello"
index.exposed = True

def recevoir(message,imprimer=True):
	#https://stackoverflow.com/questions/71104397/how-to-convert-svg-string-to-svg-file-using-python
	with open("svgTest.svg", "w") as svg_file:
			svg_file.write(message)
			print("fichier enregistré")
			
	if imprimer:
		ad = axidraw.AxiDraw()
		ad.plot_setup("svgTest.svg")
		ad.plot_run()
	
	print(message)
	return f"Chaine reçue : {message}"
	
recevoir.exposed = True


cherrypy.config.update({
        'server.socket_host': '0.0.0.0',   # Accessible depuis tout le réseau
        'server.socket_port': 5432,
        'server.thread_pool': 8,}
    )

cherrypy.tree.mount(index, "/")
cherrypy.tree.mount(recevoir, "/recevoir")

cherrypy.engine.start()
cherrypy.engine.block()


