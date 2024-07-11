## Labels

Les labels sont des étiquettes qui permettent d'étiquetter des spec dans nos manifeste de deploiement.

Par exemple ici :
```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: httpd-server-deployment

  labels:

    app: httpd-server

spec:

  replicas: 4

  selector:

    matchLabels:

      app: httpd-server

  template:

    metadata:

      labels:

        app: httpd-server

    spec:

      containers:

      - name: httpd-server

        image: httpd:latest

        imagePullPolicy: Always

        ports:

        - containerPort: 80
```

On a une partie ```labels:``` avec une option app: et une valeur associée. Le nom donné ici (httpd-server) c'est le nom de notre label, et ca va nous etres util pour organiser et selectionner nos spec.


Pour lister uniquement mes pods qui font partie du label httpd-server je lance la commande :
```bash
kubectl get pods -l app=httpd-server
```

Pour la commande kubectl permettant d’afficher les logs en direct de tous les pods liés à notre application "httpd-server", on fait :
```bash
kubectl logs -f -l app=httpd-server
```

## Namespaces

Les namespaces servent à partitionner logiquement un cluster Kubernetes en plusieurs environnements virtuels isolés. Pour faire simple, on reste dans le même cluster, sauf qu'on va le scinder en plusieurs environnements virtuels.

### Comment ça marche ?

Pour créer un namespace :
```bash
# Ici on créer un namespace nommé "development"
kubectl create namespace development
```

Pour s'en servir dans un manifeste de déploiement :
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  namespace: development # Ici le nom de notre namespace development
spec:
  containers:
    - name: mycontainer
      image: nginx
```


## La différence entre namespace & labels

Les namespaces sont utilisés pour créer des partitions logiques isolées dans un cluster Kubernetes, ce qui est utile pour séparer des environnements (comme développement, test, production) ou des équipes.
Les labels sont des paires clé-valeur associée flexibles utilisées pour organiser, sélectionner et gérer des objets Kubernetes de manière fine, facilitant la gestion des ressources à grande échelle, mais ça n'a rien de technique, c'est juste des étiquettes qu'on met sur nos objets kubernetes.