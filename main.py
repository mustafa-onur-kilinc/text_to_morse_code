from morse_converter import MorseConverter


def main():
    converter = MorseConverter()

    print("Welcome to Text to Morse Converter!")
    print("-" * 60)

    user_input = input("Please enter the text you wish to convert: ")

    result = converter.convert_to_morse(user_input)

    print("The morse code equivalent:")
    print(result)

    if converter.is_invalid_char_found():
        print("Invalid characters represented with '?' sign.")


if __name__ == "__main__":
    main()
