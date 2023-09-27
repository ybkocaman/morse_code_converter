morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}


def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for character in text:
        if character in morse_code_dict:
            morse_code.append(morse_code_dict[character])
        else:
            morse_code.append(character)
    return ' '.join(morse_code)


if __name__ == "__main__":
    input_text = input("Enter a text to convert to Morse Code:\n")
    converted_message = text_to_morse(input_text)
    print(f"Morse Code: {converted_message}")
