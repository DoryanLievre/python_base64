from src.functions import *


def b64():
    """The base 64 table

    Returns: The base 64 table
    """
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(s_to_encode):
    """Base 64 encode

    Args:
        s_to_encode: The string to encode

    Returns: The base 64 encoded string
    """
    encode = string_to_list(s_to_encode)
    encode2 = char_list_to_int(encode)
    encode3 = list_of_int_to_binary_numbers(encode2)
    encode4 = binary_list_to_binary_string(encode3)
    encode5 = binary_string_to_binary_list_of_6(encode4)
    encode6 = binary_to_int(encode5)
    encode7 = list_to_base64(encode6)
    encode8 = add_equals(encode7)
    encode9 = list_to_string(encode8)

    print("The encoded result is: " + "'" + encode9 + "'")
    return encode9


def decode(s_to_decode):
    """Base 64 encode

    Args:
         s_to_decode: The string to decode

    Returns: The base 64 decoded string
    """
    def to_b64(s):
        """
        Args:
            s: The base 64 string to decode

        Returns: The base 64 representation
        """
        return ''.join(
                (
                    format(b64().index(chr(car)), '0>6b')
                    for car in s.strip('=').encode()
                )
        )

    def to_eight(s):
        """Suppress the un-needed trailing zeros

        Args:
            s: The string to be shortend

        Returns: The string with a length modulus eight
        """
        return to_b64(s)[:len(to_b64(s)) - len(to_b64(s)) % 8]

    return int(to_eight(s_to_decode), base=2).to_bytes(len(to_eight(s_to_decode)) // 8, byteorder='big').decode()


def main():
    print('Base 64 encoder/decoder')
    #
    # Infinite loops until user enters 'x' to exit
    #
    while True:
        user_choice = input('(E)ncode, (D)ecode or e(X)it:')
        if user_choice.upper() == 'X':
            print('Exiting!')
            break
        if user_choice.upper() not in ('E', 'D', 'X'):
            print('Invalide choice!')
            continue
        while True:
            user_input = input('Enter your string or e(X)it:')
            if user_input.upper() == 'X':
                break
            if user_choice.upper() == 'E':
                print('Encoded string: {}'.format(encode(user_input)))
            else:
                print('Decoded string: {}'.format(decode(user_input)))


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()