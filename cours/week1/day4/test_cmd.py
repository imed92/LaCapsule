import subprocess
result = subprocess.run(['ls', './'], capture_output=True, text=True)
if result.returncode == 0:
    subprocess.run(['echo', 'La première commande a réussi'])
    print("La première commande a resussi  :", result.stdout)
else:
    print("La première commande a échoué avec l'erreur :", result.stderr)