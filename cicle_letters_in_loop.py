def shift_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
