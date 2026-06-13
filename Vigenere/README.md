# Vigenere Cipher in Python

A simple implementation of the Vigenère Cipher encryption & decryption algorithm.

## How it works :

The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to determine how much each letter is shifted.

Each letter of the key corresponds to a shift value.... The key is repeated until it matches the length of the plaintext.

```text
A = 0
B = 1
C = 2
...
Z = 25
```

The key is repeated until it matches the length of the plaintext.

### Example

Plaintext:

```text
HELLO
```

Key:

```text
KEYKE
```

Encryption:

```text
H + K = R
E + E = I
L + Y = J
L + K = V
O + E = S
```

Ciphertext:

```text
RIJVS
```

While decrypting, the shifts are reversed using the same key.

## Run

```bash
python main.py
```

## Screenshots containing example usage