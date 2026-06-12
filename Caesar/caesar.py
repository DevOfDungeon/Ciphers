def caesar(text, shift, encrypt=True):
    if shift < 1 or shift > 25:
        raise ValueError("Shift must be an integer between 1 and 25.")
    
    alphabet ='abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    final_text = text.translate(translation_table)
    
    return final_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)