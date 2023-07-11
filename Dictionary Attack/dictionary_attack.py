import os
import itertools

def xor_encrypt_decrypt(input_string, key):
    """This function can be used to both encrypt and decrypt a string with XOR encryption."""
    output_string = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(input_string, itertools.cycle(key)))
    return output_string

def is_decryption_successful(plaintext):
    """Check if the plaintext contains the word 'Password'."""
    return 'Password' in plaintext

def dictionary_attack(encrypted_file_path, dictionary_path):
    with open(encrypted_file_path, 'rb') as ef:
        ciphertext = ef.read().decode('utf-8')

    with open(dictionary_path, 'r') as f:
        for index, line in enumerate(f):
            password = line.strip()
            plaintext = xor_encrypt_decrypt(ciphertext, password)
            if is_decryption_successful(plaintext):
                return password

    return None

# Encrypt a string and save it to a file
plaintext = "This is a secret message. Password is doge1234."
key = "doge1234"
encrypted_text = xor_encrypt_decrypt(plaintext, key)

with open("encrypted.txt", 'w') as ef:
    ef.write(encrypted_text)

# Run dictionary attack
found_password = dictionary_attack("encrypted.txt", "dictionary.txt")
print(f"[!] Found password: {found_password}")
