#!/usr/bin/python3

import os
import sys
import pwd
import grp

# Vérification du nombre d'arguments
if len(sys.argv) != 4:
    print("Usage: ./make_executable.py <file> <user> <group>")
    sys.exit(1)

# Variables pour le fichier, l'utilisateur et le groupe
file_to_make_executable = sys.argv[1]
user = sys.argv[2]
group = sys.argv[3]

# Donner les droits d'exécution au fichier pour l'utilisateur et le groupe spécifiés
os.chmod(file_to_make_executable, 0o755)

# Obtenir les UID et GID de l'utilisateur et du groupe
# uid = int(os.popen('id -u ' + user).read().strip())
# gid = int(os.popen('id -g ' + group).read().strip())
uid = pwd.getpwnam(sys.argv[2]).pw_uid
gid = grp.getgrnam(sys.argv[3]).gr_gid

# Changer le propriétaire et le groupe du fichier
os.chown(file_to_make_executable, uid, gid)

print(f"Le fichier '{file_to_make_executable}' a été rendu exécutable pour l'utilisateur '{user}' et le groupe '{group}'.")
