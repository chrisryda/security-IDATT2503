package ex6.server;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.util.ArrayList;
import java.util.List;

@RestController
//@RequestMapping("v1")
public class Controller {
    List<User> users = new ArrayList<User>();

    @GetMapping("/hello")
    public String hello(@RequestParam("name") String name) {
        return String.format("Hello %s!", name);
    }

//    @GetMapping("/hello/{name}")
//    public String hello(@PathVariable("name") String name) {
//        return String.format("Hello %s!", name);
//    }

    @GetMapping("/users")
    public List<User> getUsers(){
        System.out.println("****GET USERS****");
        return users;
    }

    @PostMapping("/users")
    public User createUser(@RequestBody User user){
        System.out.println("****ADD USER****");
        user.setId(users.size());
        users.add(user);
        return user;
    }

    @PutMapping("/users/{id}")
    public User changeUser(@RequestBody User userNewData, @PathVariable int id){
        System.out.println("****CHANGE USER****");
        for (int i = 0; i < users.size(); i++){
            User current = users.get(i);
            if (current.getId() == id){
                users.set(i,userNewData);
                return userNewData;
            }
        }
        return null;
    }
    
    //Oppgave til deg som leser!
    //Legg til muligheten for å slette en bruker
}

