package ex6.server.controller;

import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.web.bind.annotation.*;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;

import java.util.HashMap;

import ex6.server.model.User;

@RestController
@EnableAutoConfiguration
@CrossOrigin
public class Controller {
    
    private static final Logger LOGGER = LogManager.getLogger(Controller.class);

    User userDB;
    HashMap<String, User> users = new HashMap<String, User>();

    // Method to mock DB implementation, we pretend a user has been created and added to the DB (HashMap)
    // Password is "supersecretpass" hashed by the client, i.e. using CryptoJS (see LoginComponent.vue for source code)
    private void init() throws NoSuchAlgorithmException, InvalidKeySpecException {
        userDB = new User("molly", "d3745aa9c27561f559c67c8586693a211911e9f8a67472bf8f8b390bf1ed1794e0f7ec237bf89033b9b8c8fe9d5b42e84a84bf2369a6073d671c757128f34b43aff8d4226fceea8c04ac50e9cfe02a3a40f2415c7736580e8085009114b7304d54d43e162d08451824478f478873d04e11c4f14a7c4d73d963fcb4dcb13139b4");
        users.put(userDB.getUserName(), userDB);
    } 
    
    @PostMapping("/login")
    public String login(@RequestBody User user) throws NoSuchAlgorithmException, InvalidKeySpecException {
        init();

        LOGGER.info("Attempting login of user " + user.getUserName());
        if(users.containsKey(user.getUserName())) {
            String passwordFromDb = users.get(user.getUserName()).getPassword();
            if (user.getPassword().equals(passwordFromDb)) {
                LOGGER.info("Login of user " + user.getUserName() + " successful");
                return "Login: Success";
            } 
        }

        LOGGER.error("Login of user " + user.getUserName() + " failed: invalid username or password");
        return "Login failed: invalid username or password";
    }
}
