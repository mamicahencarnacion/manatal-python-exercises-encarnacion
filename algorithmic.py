def convert_to_roman_numeral(number: int):
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    if not isinstance(number, int):
        raise TypeError("Supports conversion of positive integers only.")

    if number < 1 or number >= 4000:
        # 4000 and up cannot be accommodated by the listed roman numeral equivalents
        raise ValueError(
            "Conversion of less than 1 or 4000 and up to roman numerals is currently not supported."
        )

    num_in_roman_numeral = ""
    for k, v in roman_numerals.items():
        base = number // k
        number %= k

        while base:
            num_in_roman_numeral += v
            base -= 1

    return num_in_roman_numeral


if __name__ == "__main__":
    input_num = input("Number: ")

    print(convert_to_roman_numeral(int(input_num)))
