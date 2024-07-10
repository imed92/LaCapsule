# Kubernetes
Kubernetes est un outil qui permet de déployer ses applications et qui permet d'assurer la haute disponibilité d'une application.

Grace a Kubernetes on va pouvoir faire en sorte que notre applciation soit dupliqué sur plusieurs serveurs : on parle alors de worker node

Dans Kubernetes on a :
- 1 master node : c'est le serveur qui va se charger d'administrer tous les worker node
- Des worker node : c'est le/les serveurs qui vont lancer nos pods

### Qu'est-ce qu'un pod ?

C'est un ensemble de conteneur qui servent à quelque chose dans une application. Dans un pod on peut retrouver plusieurs conteneurs comme un contenur nginx, un conteneur django, un conteneur mysql, etc

### En résumé

On a un gros cluster => c'est l'ensemble de toute notre architecture Kubernetes (le master node et les worker nodes)
On a 1 master node
On a des worker node
Et dans nos worker node on a un/des pods

## Comment ca marche ?
#### 1ere étape installer kubectl et minikube
Minikube est un logiciel permettant de simuler un cluster Kubernetes en local.

Pour l'installer on fait : 
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```
Une fois que c'est fait, on s'assure que minikube ets bien installé
```bash
minikube version
```

Ensuite, on va installer kubectl
```bash
curl -LO https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
kubectl version --client
```
Une fois que c'est fait, on s'assure que kubectl est bien installé
```bash
kubectl version
```

Maintenant on va lancer notre cluster
```bash
minikube start
```

Si on a une erreur qui dit que le driver de minikube n'est pas docker (que c'est qemu par exemple), voila ce qu'il faut faire :
```bash
# Ci dessous, on dit que le driver par defaut de minikube sera docker
minikube config set driver docker
# Ci dessous, on dit qu'on va créer un cluster minikube basé sur le driver docker mais seulement pour ce cluster qu'on créer
minikube start --driver=docker
```

Une fois que le minikube start a terminé, on va checker si notre cluster est bien lancé :
```bash
minikube status
```
Et voilà.

On va démarrer un premier pod.
Dans ce pod on va y installer un seul conteneur qui va run l'image docker ```hello-world```
```bash
# Ici on dit qu'on va créer un pod qui va se nommer myfirstpod et qui va run l'image docker hello-world a la verison latest
kubectl run myfirstpod --image=hello-world:latest
```
Une fois que c'est fait, on check l'etat de notre pod :
```bash
kubectl get pods
```
Cette commande nous retourne plusieurs infos :
- NAME : c'est le nom du pod
- READY : a/b => a c'est le nombre de container en cours d'execution et b c'est le nombre total de contai,er qu'il y a dans le pod
- STATUS : c'est le status du pod
- RESTARTS : c'est le nombre de fois qu'un pod a du redémarrer
- AGE : c'est l'age du pod (depuis quand il existe)

Pour récupérer les logs d'un pod :
```bash
kubectl logs myfirstpod
```

Enfin, pour supprimer un pod :
```bash
kubectl delete pod myfirstpod
```

Maintenant si je relance la commande pour voir tous mes pods, il n'y a rien qui s'affiche.
