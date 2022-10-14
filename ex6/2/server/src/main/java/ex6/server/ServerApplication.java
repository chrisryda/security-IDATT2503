package ex6.server;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ServerApplication {

	public static void main(String[] args) {
		//System.setProperty("server.servlet.context-path", "/api");
		SpringApplication.run(ServerApplication.class, args);
	}

}
