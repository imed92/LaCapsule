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
