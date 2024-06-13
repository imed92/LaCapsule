# On importe subprocess
import subprocess

# subprocess.run exécute la commande shell spécifiée. Dans ce cas, la commande est sort fichier_source.txt.
# shell=True signifie que la commande est exécutée dans un shell. Cela permet d'utiliser des fonctionnalités spécifiques au shell, comme la redirection des flux ou les commandes enchaînées. Cependant, cela peut aussi présenter des risques de sécurité si la commande inclut des entrées non fiables.
# stdout=output_file redirige la sortie standard (stdout) de la commande vers le fichier sorted_output.txt.
# Ce que fait la commande sort
# sort fichier_source.txt est une commande shell qui trie les lignes du fichier fichier_source.txt par ordre alphabétique.
# Ici on ouvre sorted_output.txt 
with open('sorted_output.txt', 'w') as output_file:
    subprocess.run('sort fichier_source.txt', shell=True, stdout=output_file)