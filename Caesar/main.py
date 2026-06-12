from caesar import encrypt, decrypt

def caesar_cipher():
    print("=== Caesar Cipher ===")
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))

    if choice == "e":
        print("Encrypted:", encrypt(text, shift))
    elif choice == "d":
        print("Decrypted:", decrypt(text, shift))
    else:
        print("Invalid choice")