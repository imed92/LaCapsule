# On importe le module sys
import sys

# Ici on check si il y a bien un argument donné en parametre
# sys.argv est une liste qui contient tous les arguments du script
# dans python3 rename_file.py toto => argv[0] = rename_file.py et argv[1] = toto
if len(sys.argv) < 2:
    print("Veuillez fournir un nom de fichier.")
    # On quitte le script si il manque un argument
    sys.exit(1)
# Si il y a bien un argument, alors on le stock dans la variable filename
filename = sys.argv[1]
# try permet de gérer les exceptions
try:
    # with open sert a stocker la valeur de lecture en mode read 'r' dans file (d'ou le as file)
    # donc le contenu du fichier sera stocké dans file
    with open(filename, 'r') as file:
        # Ici je lis toutes les lignes du fichier file
        lines = file.readlines()
        # Ici j'affiche le nombre de lignes du fichier
        print("# lignes: "+ str(len(lines)))
# on gere l'excepetion quand y a une erreur fichier non trouvé
except FileNotFoundError:
    print("Fichier non trouvé.")
# Ci dessous on affiche la liste de tous les arguments
print(sys.argv)
