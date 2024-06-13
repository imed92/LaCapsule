# Importe le module shutil qui contient des fonctions pour la gestion de fichiers et de répertoires.
import shutil
def exclude_txt(file_name, path):
    # Cette fonction prend en entrée le nom d'un fichier et son chemin.
    # Elle retourne True si le fichier ne se termine pas par .txt, sinon False.
    return not file_name.endswith('.txt')

# Utilise shutil.copytree pour copier le contenu d'un répertoire source vers un répertoire de destination.
# Le troisième argument 'ignore' utilise la fonction exclude_txt pour exclure les fichiers .txt de la copie.
shutil.copytree('/chemin/source', '/chemin/destination', ignore=exclude_txt)
