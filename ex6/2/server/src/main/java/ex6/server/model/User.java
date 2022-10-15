package ex6.server.model;

import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.util.HashMap;

import ex6.server.security.PasswordHasher;

public class User {
    private String userName;
    private String password;

    static HashMap<String, User> users = new HashMap<String, User>();

    public User(String userName, String password) throws NoSuchAlgorithmException, InvalidKeySpecException {
        this.userName = userName;
        this.password = PasswordHasher.generatePasswordHash(password);
    }

    public String getUserName() {
        return this.userName;
    }

    public String getPassword() {
        return this.password; 
    }

}
