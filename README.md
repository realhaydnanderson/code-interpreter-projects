# Code Interpreter Projects

This repository is a compilation of experiments done with OpenAI's Code Interpreter.

## Dictionary Attack

### XOR Encryption and Decryption

The provided Python code demonstrates XOR encryption and decryption techniques, along with a dictionary attack for password recovery.

#### xor_encrypt_decrypt Function

The `xor_encrypt_decrypt` function is responsible for handling both encryption and decryption processes using XOR operations. It takes an input string and a key as parameters and performs the XOR operation character by character. The result is returned as the encrypted or decrypted output.

#### is_decryption_successful Function

The `is_decryption_successful` function checks whether the provided plaintext contains the word "Password". If the word is present, it indicates a successful decryption process.

#### dictionary_attack Function

The `dictionary_attack` function conducts a dictionary attack on an encrypted file. It takes the paths to the encrypted file and a dictionary file as input. The function reads the contents of the encrypted file, retrieves passwords from the dictionary file, and attempts decryption using each password. If a successful decryption occurs, the corresponding password is returned.

#### Usage

In the script, a plaintext message is encrypted and saved to a file. The `dictionary_attack` function is then utilized to perform a password recovery by trying passwords from a dictionary file. If a successful password is found, it is printed as the output.

This code provides a practical demonstration of XOR encryption, decryption, and the implementation of a dictionary attack for password retrieval.
