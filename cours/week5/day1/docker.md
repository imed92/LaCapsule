## Qu'est-ce que la Conteneurisation ?

La conteneurisation est une technologie qui permet d'isoler des applications et leurs dépendances dans des environnements appelés "conteneurs". Chaque conteneur est léger, portable et s'exécute de manière isolée, ce qui facilite le déploiement et la gestion des applications. Voici les points clés :

- **Isolation** : Chaque conteneur fonctionne de manière isolée, ce qui signifie que les applications et leurs dépendances ne se mélangent pas.
- **Léger** : Les conteneurs partagent le noyau de l'OS, ce qui les rend plus légers que les machines virtuelles.
- **Portabilité** : Les conteneurs peuvent être exécutés de manière cohérente sur n'importe quel système compatible, que ce soit sur un développeur local ou sur des serveurs de production.

### Avantages de la Conteneurisation

- **Portabilité** : Les applications peuvent être facilement déplacées d'un environnement à un autre.
- **Isolation** : Les applications sont isolées les unes des autres, évitant ainsi les conflits.
- **Efficacité** : Moins de ressources sont utilisées par rapport aux machines virtuelles.

---

## Qu'est-ce que Docker ?

Docker est une plateforme de conteneurisation qui facilite la création, le déploiement et l'exécution de conteneurs. Il simplifie le processus de conteneurisation et rend les applications plus faciles à gérer et à déployer. Voici une explication simple :

### Composants Clés de Docker

- **Docker Engine** : Le moteur qui exécute les conteneurs. Il est installé sur l'hôte et gère les conteneurs.
- **Images Docker** : Des modèles statiques qui contiennent tout ce qui est nécessaire pour exécuter une application (code, runtime, bibliothèques, etc.).
- **Conteneurs Docker** : Des instances exécutables des images. Ils sont légers et isolés.
- **Docker Hub** : Un registre public où vous pouvez trouver et partager des images Docker. 

### Fonctionnement de Docker

1. **Création d'une Image** : Utilisez un `Dockerfile` pour définir l'image de votre application. Cela inclut tout ce dont l'application a besoin pour fonctionner.
   
2. **Construction de l'Image** : Utilisez la commande `docker build` pour créer une image à partir du `Dockerfile`.
   
   ```bash
   docker build -t my_image .
   ```

3. **Exécution du Conteneur** : Utilisez la commande `docker run` pour démarrer un conteneur à partir de l'image.

   ```bash
   docker run -d -p 8080:80 my_image
   ```

4. **Gestion des Conteneurs** : Utilisez des commandes Docker pour gérer vos conteneurs (lister, arrêter, supprimer, etc.).

   ```bash
   docker ps         # Liste les conteneurs en cours d'exécution
   docker stop <id>  # Arrête un conteneur
   docker rm <id>    # Supprime un conteneur
   ```

### Exemple Simple

- **Dockerfile** : Créer un conteneur Docker pour une base de données SQL (par exemple, PostgreSQL) et changer le port par défaut est une tâche courante. Voici un exemple de Dockerfile pour PostgreSQL où le port par défaut est modifié :
  
 ```Dockerfile
    # Utiliser l'image officielle de PostgreSQL comme image de base
    FROM postgres:latest

    # Définir les variables d'environnement pour la base de données
    ENV POSTGRES_DB=mydatabase
    ENV POSTGRES_USER=myuser
    ENV POSTGRES_PASSWORD=mypassword

    # Exposer le port modifié
    EXPOSE 5433

    # Ajouter un fichier de configuration pour changer le port par défaut
    COPY postgres.conf /etc/postgresql/postgresql.conf

    # Définir le point d'entrée
    CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]

 ```

- **Construction de l'Image** :

  ```bash
  docker build -t my_postgres_image .
  ```

- **Exécution du Conteneur** :

  ```bash
  docker run -d --name my_postgres_container -p 5433:5433 my_postgres_image
  ```

---

### Conclusion

- **Conteneurisation** : Technique pour isoler des applications avec leurs dépendances.
- **Docker** : Outil facilitant la création, le déploiement et l'exécution de conteneurs.

Docker rend le processus de conteneurisation simple et efficace, permettant ainsi de déployer des applications de manière cohérente et fiable.