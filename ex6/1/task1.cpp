#include <iomanip>
#include <iostream>
#include <openssl/evp.h>
#include <openssl/sha.h>
#include <sstream>
#include <string>

/// Return hex string from bytes in input string.
std::string hex(const std::string &input) {
	std::stringstream hex_stream;
	hex_stream << std::hex << std::internal << std::setfill('0');
	
	for (auto &byte : input) {
		hex_stream << std::setw(2) << (int)(unsigned char)byte;
	}
	return hex_stream.str();
}

std::string pbkdf2(const std::string &password, const std::string &salt) {
	int key_length = 20; //SHA1 standard 
	
	std::string hash;
	hash.resize(key_length);

	PKCS5_PBKDF2_HMAC_SHA1((const char *)&password[0], password.size(), (const unsigned char *)&salt[0], salt.size(), 2048, key_length, (unsigned char *)&hash[0]);

	return hash;
}

std::string brute_force(const std::string &hash, const std::string &salt, int max_length, int current_length, std::string attempt) {
	
	// ASCII A-Za-z, assumes password contains only letters  
	for (unsigned char c = 65; c < 123; ++c) {
		attempt[current_length - 1] = c;
		if (current_length < max_length) {
			std::string res = brute_force(hash, salt, max_length, current_length + 1, attempt);
			
			//Needed to break recursion
			if (!res.empty()) {
				return res;
			}
		} 
		else {
			std::cout << attempt << std::endl;
			if (hex(pbkdf2(attempt, salt)) == hash) {
				return attempt;
			}
		}
	}
	return "";
}

std::string find_password(const std::string &hash, const std::string &salt, int max_length) {
	std::string attempt;
	for (int i = 1; i <= max_length; ++i) { 
		attempt = "";
		attempt.resize(i);

		std::string res = brute_force(hash, salt, i, 1, attempt);
		if (!res.empty()) {
			return res;
		}
	}
	return "";
}

int main() {
	const std::string hash = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6";
	const std::string salt = "Saltet til Ola";
	
	std::string password = find_password(hash, salt, 10);
	std::cout << "The password is: " << password << std::endl;

	return 0;
}
