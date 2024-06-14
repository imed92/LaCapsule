#!/usr/bin/env python3

import shutil
import psutil

# Fonction pour surveiller l'espace disque total et disponible sur un lecteur spécifié
def check_disk_usage(disk):
    # Récupère les informations sur l'utilisation du disque pour le chemin spécifié.
    # La fonction shutil.disk_usage(disk) renvoie un tuple (total, used, free).
    total, used, free = shutil.disk_usage(disk)
    # Affiche le chemin du disque ou du point de montage.
    print(f"Disque: {disk}")
    # Calcule et affiche l'espace disque total en gigaoctets (Go).
    # La division par (2**30) convertit les octets en gigaoctets.
    print(f"  Espace total: {total // (2**30)} Go")
    # Calcule et affiche l'espace disque utilisé en gigaoctets (Go).
    # La division par (2**30) convertit les octets en gigaoctets.
    print(f"  Espace utilisé: {used // (2**30)} Go")
    # Calcule et affiche l'espace disque libre en gigaoctets (Go).
    # La division par (2**30) convertit les octets en gigaoctets.
    print(f"  Espace libre: {free // (2**30)} Go")
    # Calcule et affiche le pourcentage de l'espace disque utilisé.
    # La formule (used / total * 100) donne le pourcentage.
    # Le format :.2f arrondit le résultat à deux chiffres après la virgule.
    print(f"  Pourcentage utilisé: {used / total * 100:.2f}%")

# Fonction pour surveiller le niveau d’utilisation du processeur
def check_cpu_usage():
    # Utilise la fonction psutil.cpu_percent pour obtenir le pourcentage d'utilisation du processeur.
    # L'argument interval=1 signifie que la fonction va mesurer l'utilisation du CPU sur une période d'une seconde.
    cpu_usage = psutil.cpu_percent(interval=1)
    # Affiche le pourcentage d'utilisation du processeur.
    # print(cpu_usage)
    print(f"Utilisation du processeur: {cpu_usage}%")


# Fonction pour surveiller le niveau total et disponible d’utilisation de la mémoire vive (RAM)
def check_ram_usage():
    # Utilise la fonction psutil.virtual_memory pour obtenir les informations sur la mémoire vive.
    mem = psutil.virtual_memory()
    # Affiche la quantité totale de mémoire vive (RAM) en gigaoctets (Go).
    # La division par (2**30) convertit les octets en gigaoctets.
    print(f"Mémoire totale: {mem.total // (2**30)} Go")
    # Affiche la quantité de mémoire vive disponible en gigaoctets (Go).
    # La division par (2**30) convertit les octets en gigaoctets.
    print(f"Mémoire disponible: {mem.available // (2**30)} Go")
    # Affiche le pourcentage de mémoire vive utilisée.
    print(f"Pourcentage de mémoire utilisée: {mem.percent}%")

disk = "/"  # Remplacez par le disque que vous souhaitez surveiller
print("Monitoring du système:\n")

# check_disk_usage(disk)
# print()
check_cpu_usage()
# print()
# check_ram_usage()