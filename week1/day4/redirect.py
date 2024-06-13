# Ici on importe le module sys
import sys

# la sortie standard sera dans output.txt (stdout = standard output)
# la stdout c'est la sortie de quand un programme s'est bien executé sans erreur
sys.stdout = open('output.txt', 'w')
print('toto')
# la sortie d'erreur sera dans error.txt
# la stderr c'est la sortie de quand un programme ne s'est pas bien executé (erreur)
sys.stderr = open('error.txt', 'w')

# ca sera ecrit dans output
print("Ceci est un message.")
print("toto tata")

# sys.stdout.close()
# sys.stdout.fileno()
# print("toto tata")

# ca sera ecrit dans error
raise ValueError("Ceci est une erreur.")
