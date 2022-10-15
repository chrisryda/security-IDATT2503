package ex6.server.security;

import java.math.BigInteger;

import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;

import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

public class PasswordHasher {

    public static String generatePasswordHash(String password) throws NoSuchAlgorithmException, InvalidKeySpecException {
        int iterations = 2048;
        char[] chars = password.toCharArray();
        byte[] salt = getSalt();

        PBEKeySpec spec = new PBEKeySpec(chars, salt, iterations, 64 * 8);
        SecretKeyFactory skf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");

        byte[] hash = skf.generateSecret(spec).getEncoded();
        return toHex(salt) + toHex(hash);
    }

    private static byte[] getSalt() throws NoSuchAlgorithmException {
        // Unsecure, done for the purpose of time-saving for this exercise
        String saltString = "supersecretsalt";
        byte[] salt = saltString.getBytes();
        
        return salt;
    }

    private static String toHex(byte[] array) throws NoSuchAlgorithmException {
        BigInteger bi = new BigInteger(1, array);
        String hex = bi.toString(16);

        int paddingLength = (array.length * 2) - hex.length();
        if (paddingLength > 0) {
            return String.format("%0" + paddingLength + "d", 0) + hex;
        } else {
            return hex;
        }
    }

}
