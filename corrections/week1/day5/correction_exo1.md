# Correction exo 1

## Projet Django avec python

Ici il faut initialiser un projet Django nommé "my_first_django_backend"

### 1ere étape : installer python et ses dépendances
```bash
sudo apt update && sudo apt install -y python3-venv python3-pip
```

### 2me étape : On créer notre environnement virtuel 
On va créer un environenement virtuel pour notre projet
```bash
# Ici on crée un environnement qui s'appelle env à l'aide de python3 -m venv
python3 -m venv env
# Ici on active notre environnement nommé 'env'
source env/bin/activate
```

Pour sortir de l'environnement quand on est dedans :
```bash
deactivate
```

### 3eme étape : On installe Django à l'aide de pip et on génère notre projet
```bash
# Ici on installe Django
pip3 install django
# Ici on génère notre projet qui va s'apeller my_first_django_backend
django-admin startproject my_first_django_backend
```

### 4ème étape : Lancer le serveur
Pour lancer le serveur, on rentre dans notre projet, puis on le run
```bash
cd my_first_django_backend
# On run notre projet
python3 manage.py runserver
```

## Projet Spring Boot avec JAVA

Ici il faut initialiser un projet Django nommé "my_first_django_backend"

### 1ere étape : installer Java et ses dépendances
```bash
sudo apt update && sudo apt install -y default-jdk openjdk-17-jdk openjdk-17-jre
```

### 2eme étape : Ajouter au PATH le chemin de JAVA une fois qu'il est installé
On ouvre le fichier /etc/environment avec nano et les droits sudo
```bash
sudo nano /etc/environment
```
Puis on y ajoute cette ligne :
```bash
JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
```

### 3eme étape : On crée notre projet
On va sur https://start.spring.io/ et on va y paramétrer notre projet puis on télécharge notre projet au format .zip.
Une fois que c'est fait, on déplace notre fichier zip depuis le dossier de téléchargements vers notre dossier courant
```bash
# On déplace
mv ~/Downloads/demo.zip .
# On dézippe
unzip demo.zip
```
Et voilà, on a notre projet demo sous forme de dossier.
Un premier fichier .java est créé dans le dossier src/main/java/[chemin de l’application]
On devra créer nos fichiers de Controller dans ce dossier.
On va y créer un controller nommé DateController.java avec ce contenu :
```java
package academy.lacapsule.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import java.util.Date;
import java.util.HashMap;

@RestController
public class DateController {
	// Ci dessous une annotation 
	// Une annotation c'est un moyen de créer une route avec un mot clé ici GetMapping
	// Cette annotation me permet de créer une route en methode GET sur la route '/'
    @GetMapping("/")
    public ResponseEntity<Object> index() {
        HashMap<String, Date> data = new HashMap<>();
        Date now = new Date();
        data.put("now", now);
		// Cette méthode retourne la date courante
        return new ResponseEntity(data, HttpStatus.OK);
    }
}
```

Puis on lance notre serveur : 
```bash
./mvnw spring-boot:run
```

Et on teste notre route '/' en méthode GET via Thunder Cient et ça devrait fonctionner.

#### NOTE : Si une dépendance manque sur SpringBoot
Pour installer une dépendance qui manque, il faut deja determiner la dépendance qui manque, puis on l'ajoute au fichier pom.xml
Le fichier pom.xml est un fichier qui contient des données sur notre projets, y compris les dépendances du projet.
Exemple : si on veut ajouter la dépendance web, on ajoute ca dans pom.xml dans la partie ```<dependencies>``` :
```xml
		<dependency>
      		<groupId>org.springframework.boot</groupId>
    		<artifactId>spring-boot-starter-web</artifactId>
	    </dependency>
```
Puis pour 'refresh' nos dépendances, on execute la commande :
```bash
./mvnw clean install
```
