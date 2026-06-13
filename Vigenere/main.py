from vigenere import encrypt, decrypt

def vigenere_cipher():
    print("=== Vigenere Cipher ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()

    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if choice == 'e':
        print ("Encrypted :", encrypt(text,key))
    elif choice == 'd':
        print ("Decrypted :", decrypt(text,key))
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    vigenere_cipher()