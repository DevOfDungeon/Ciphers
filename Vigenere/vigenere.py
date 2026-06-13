def vigenere(text,key,direction=1):
    
    if not key.isalpha():
        raise ValueError("Key must consist of alphabetic characters only.")
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final =''
    key_index = 0

    for char in text:
   
    # Append any non letter to the final string without changing it
        if not char.isalpha():
            final += char
        else:
            # Find the right key character to use
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset= alphabet.index(key_char)
            index=alphabet.find(char)
            new_index= (index + direction * offset) % len(alphabet)
            final += alphabet[new_index]
    return final

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
