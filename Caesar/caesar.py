def caesar(text, shift, encrypt=True):
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer.")
    if shift < 1 or shift > 25:
        raise ValueError("Shift must be between 1 and 25.")
    