"""utilisation dune fonction"""
import httplib
import sys
import pdb
LOG = False
if len(sys.argv) > 2:
    LOG = True
def logger(fichier, message):
    """ fonction logger"""
    if LOG : 
        fichier.write (message) 
def fonction1():
    """fonction principale"""
    pdb.set_trace()
    conn = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128 )
    conn.request("GET", "http://www.python.org/index.html")
    reponse = conn.getresponse()
    print reponse.status, reponse.reason
    data1 = reponse.read()
    compteur = 0
    for variable in data1:
        if variable == " " :
            compteur = compteur+1
    print " le nombre de mots est :"
    print compteur
    fichier = open("log.txt","w")
    logger(fichier,"statut : %s" %str(reponse.status))
    fichier.close()
    conn.close()
fonction1()
