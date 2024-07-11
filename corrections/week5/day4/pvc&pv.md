# PV & PVC

Les PersistentVolumes (PV) et PersistentVolumeClaims (PVC) travaillent ensemble pour fournir un stockage persistant dans Kubernetes. Les PVs sont des ressources de stockage provisionnées et gérées par le cluster, tandis que les PVCs permettent aux utilisateurs de demander et d'utiliser ce stockage de manière abstraite et indépendante des détails d'implémentation. Cela facilite la gestion et l'utilisation du stockage persistant dans un environnement Kubernetes.

## PersistentVolume (PV)

Un PersistentVolume est une ressource de stockage dans le cluster Kubernetes. C'est un volume qui a une durée de vie indépendante des pods qui l'utilisent. Les PVs sont provisionnés par les administrateurs du cluster ou dynamiquement via des StorageClasses.
Exemple dans un manifest de deploiement :
```yaml
apiVersion: v1                   # La version de l'API Kubernetes utilisée pour créer cet objet PersistentVolume
kind: PersistentVolume           # Le type de ressource, ici un PersistentVolume (PV)
metadata:
  name: my-pv                    # Le nom de ce PersistentVolume, utilisé pour l'identifier dans le cluster
spec:
  capacity:                      # Spécifie la capacité du volume
    storage: 10Gi                # La taille de stockage disponible sur ce PV, ici 10 gigaoctets
  accessModes:                   # Les modes d'accès autorisés pour ce volume
    - ReadWriteOnce              # Le volume peut être monté en lecture-écriture par un seul nœud à la fois
  persistentVolumeReclaimPolicy: Retain # Politique de récupération de ce PV une fois que le PVC associé est supprimé; 'Retain' signifie que le PV reste disponible mais non réclamé
  storageClassName: manual       # Le nom de la classe de stockage associée à ce PV, utile pour le provisionnement dynamique
  hostPath:                      # Spécifie le chemin d'accès à un répertoire sur le nœud hôte (utilisé pour le stockage local)
    path: /mnt/data              # Le chemin d'accès réel sur le nœud hôte où les données seront stockées
```

## PersistentVolumeClaim (PVC)

Un PersistentVolumeClaim est une demande de stockage par un utilisateur. Les PVCs permettent aux pods de réclamer un espace de stockage sans connaître les détails de l'infrastructure de stockage sous-jacente.

Exemple dans un manifest de déploiement :
```yaml
apiVersion: v1                   # La version de l'API Kubernetes utilisée pour créer cet objet PersistentVolumeClaim
kind: PersistentVolumeClaim      # Le type de ressource, ici un PersistentVolumeClaim (PVC)
metadata:
  name: my-pvc                   # Le nom de ce PersistentVolumeClaim, utilisé pour l'identifier dans le cluster
spec:
  accessModes:                   # Les modes d'accès demandés pour ce volume
    - ReadWriteOnce              # Le volume peut être monté en lecture-écriture par un seul nœud à la fois
  resources:                     # Spécifie les ressources demandées
    requests:
      storage: 10Gi              # La quantité de stockage demandée, ici 10 gigaoctets
  storageClassName: manual       # Le nom de la classe de stockage associée à ce PVC, utilisé pour le provisionnement dynamique
```

### Mais concrètement, comment un utilisateur va faire une demande de stockage vers un PVC ?

Une fois que le PVC est créé avec succès (my-pod), on peut l'utiliser dans les spécifications d'un Pod pour monter le volume de stockage associé.

Voici un exemple de spécification de Pod qui utilise le PVC my-pvc créé précédemment :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: mycontainer
      image: nginx
      volumeMounts:
        - mountPath: "/data"
          name: my-volume
  volumes:
    - name: my-volume
      persistentVolumeClaim:
        claimName: my-pvc # le nom du pvc créée précédemment
```

#### En résumé, comment ça marche

Etape par étape, pour qu'un utilisateur fasse une demande de stockage à travers un PersistentVolumeClaim (PVC) :

1. Il crée un fichier YAML décrivant le PVC avec les spécifications de stockage requises.
2. Il applique ce fichier YAML au cluster Kubernetes à l'aide de kubectl apply.
3. Une fois créé, il peut utiliser le PVC dans les spécifications d'un Pod pour fournir un stockage persistant à ses applications conteneurisées.

Cela permet aux utilisateurs de gérer efficacement le stockage persistant dans Kubernetes, en séparant la demande de stockage des détails d'implémentation spécifiques à l'infrastructure sous-jacente.