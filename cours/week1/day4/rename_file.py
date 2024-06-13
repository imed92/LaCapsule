# J'importe le module os
# Le module os c'est le module qui permet  de communiquer avec le systeme via un script en Python
import os

# On crée une variable directory avec pouir valeur './test'
# Il a pour valeur le dossier test qui est dans le dossier courant
directory = './test'
# On parcoure la liste des elements du dossier './test'
for filename in os.listdir(directory):
    # a chaque tour de boucle on check si le fichier courant finit par .txt
    if filename.endswith('.txt') and filename.endswith('_backup.txt') != True:
        new_name = filename.replace('.txt', '_backup.txt')
        # Ici grace au module os je vais utiliser la methode rename
        # Cette methode permet de renommer un fichier avec au autre nom de fichier
        # Elle prend 2 parametre :
        # 1er : le chemin du fichier qu'on veut modifier => ici os.path.join(directory, filename) concatene le dossier suivi du fichier pour avoir le chemin complet du fichier a renommer
        # 2eme : le chemin du fichier de destination (la ou le fichier doit etre + son nouveau nom) => os.path.join(directory, new_name) on concatene le chemin du dossier avec son nouveau nom de fichier
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))