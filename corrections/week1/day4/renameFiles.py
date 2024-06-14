# Ici je mets en place le shebang qui dit que ce code sera lu par python
# /bin/python3 c'est le chemin absolue du logiciel python3
#!/bin/python3

import os
import sys

# Ici le chemin absolu du sossier exo1
# Ici etape 1
# directory = '/home/imed/Documents/LaCapsule/corrections/week1/day4/exo1'
# prefixe = 'le_'
# suffixe = '_backup'

# Ici etape 2
# Stocker ledirectory, suffixe et prefixe via les arguments
directory = sys.argv[1] # Ici premier argument
prefixe = sys.argv[2] # Ici deuxieme argument
suffixe = sys.argv[3] # Ici troisieme argument

# Ici on parcours tous les éléments du dossier directory
for filename in os.listdir(directory):
    # Ici on stock le chemin complet du fichier de base 
    old_path = os.path.join(directory, filename)
    if os.path.isfile(old_path):
        # /home/imed/Documents/LaCapsule/corrections/week1/day4/exo1 + fichier1.txt
        # base = fichier1
        # extension = .txt
        # Ici os.path.splitext(filename) retourne une tuples avec 2 elements : le nom du fichier sans l'extension ET l'extension seul
        # Donc base sera = au nom du fichier sans l'extension 
        # extension sera = a l'extension (.txt)
        base, extension = os.path.splitext(filename)
        print(base)
        # Ici new_name sera = a la concatenation du prefixe + le nom du fichier de base + le suffixe + l'extension du fichier
        # Ca donnera le_ + fichier1 + _backup + .txt
        new_name = f"{prefixe}{base}{suffixe}{extension}"
        # Ici on concatene le chemin absolue du dossier avec notre nouveau nom de fichier
        # Ca donnera /home/imed/Documents/LaCapsule/corrections/week1/day4/exo1 + le_fichier1_backup.txt
        new_path = os.path.join(directory, new_name)
        # Et enfin on renomme via la methode rename du module os
        os.rename(old_path, new_path)

