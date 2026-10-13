"""
This module includes Python code for converting an input string into a Morse code text.

For more information about Morse code, check out the Wikipedia page:
https://en.wikipedia.org/wiki/Morse_code

Resources used to write this code:

Kanchan_Ray 2025, "string.punctuation in Python", Sanchhaya Education Private Limited,
accessed 12 October 2026, <https://www.geeksforgeeks.org/python/string-punctuation-in-python/>

kartik 2026, "Python Dictionary get() Method", Sanchhaya Education Private Limited,
accessed 12 October 2026, <https://www.geeksforgeeks.org/python/python-dictionary-get-method/>

Vlad H 2011, "How to convert a file into a dictionary?", Stack Exchange Inc.,
accessed 12 October 2026, <https://stackoverflow.com/a/4804039>
"""

from string import punctuation


def read_morse_code_table(table_filepath: str) -> dict:
    """
    Reads table at `table_filepath` location, returns a dictionary
    where keys are characters and values are the Morse code equivalent of
    those characters

    :param table_filepath: Directory of Morse code table file
    :return: morse_code_dict: Morse code table as a dictionary
    """

    morse_code_dict = {}

    with open(table_filepath, encoding="utf8") as file:
        for line in file:
            char, morse_char = line.split()
            morse_code_dict[char] = morse_char

    return morse_code_dict


class MorseConverter:
    def __init__(self):
        """
        This class converts a string into Morse code
        by finding Morse code equivalents of each character in string
        and appending those codes together
        """

        self.invalid_char_found = False

        self.letters_dict = read_morse_code_table(table_filepath="morse_code_tables/letters.txt")
        self.numbers_dict = read_morse_code_table(table_filepath="morse_code_tables/numbers.txt")
        self.punctuation_dict = read_morse_code_table(table_filepath="morse_code_tables/punctuation.txt")

    def find_morse_code_equivalent(self, character: str) -> str:
        """
        Gets a string type `character`, checks its type (letter, number, punctuation, space) and
        returns its Morse code equivalent

        Forward slash ("/") is used to separate words

        If `character` does not exist in any table or is an unknown type,
        question mark ("?") is returned

        :param character: String character to convert
        :return: Morse code equivalent of `character` if it exists, "?" otherwise
        """

        morse_character = "?"

        if str.isspace(character):
            morse_character = "/"
        elif str.isalpha(character):
            morse_character = self.letters_dict.get(str.upper(character), "?")
        elif str.isdigit(character):
            morse_character = self.numbers_dict.get(str.upper(character), "?")
        elif character in punctuation:
            morse_character = self.punctuation_dict.get(character, "?")

        return morse_character

    def convert_to_morse(self, input_str: str) -> str:
        """
        Converts `input_str` to Morse code letter by letter,
        returns the resulting Morse code string

        Sets the invalid_char_found flag as True if `input_str` includes
        character(s) without their Morse code equivalent(s)

        :param input_str: String to convert to Morse code
        :return: Converted Morse code string
        """

        morse_code = ""

        for char in input_str:
            morse_char = self.find_morse_code_equivalent(char)

            if morse_char == "?":
                self.invalid_char_found = True

            morse_code += f"{morse_char} "

        return morse_code

    def is_invalid_char_found(self) -> bool:
        return self.invalid_char_found


def main():
    morseConverter = MorseConverter()

    result = morseConverter.convert_to_morse(input_str="Hello, World!")

    print(result)


if __name__ == "__main__":
    main()
