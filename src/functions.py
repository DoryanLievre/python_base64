""" All function to Encode/ Decode

"""
################################################################
#
# Step 1
#


"""Convert a string to a list of chars
"""


def string_to_list(string):
    """Convert String to a list of chars


    Args:
        string: A string to convert to a list

    Returns:
        A list of each characters in the given string

    """
    return [char for char in string]


if __name__ == "__main__":
    #
    # initialize list
    #
    test = "ABCD"
    print('Result : \n')
    print(string_to_list(test))

################################################################
#
# Step 2
#


"""Convert a list of chars to a list of ints
"""


def char_list_to_int(list):
    """ Convert String list to ascii values

    Args:
        list: A list of string

    Returns:
       A list of each ASCII values in the given list of strings

    """
    list_of_int = []
    for elements in list:
        list_of_int.extend(ord(num) for num in elements)
    return list_of_int


if __name__ == "__main__":
    #
    # initialize list
    #
    test = ['A', 'B', 'C', 'D']
    print('Result : \n')
    print(char_list_to_int(test))


################################################################
#
# Step 3
#

"""Convert a list of int to a list of binary number on 8 bit
"""


def list_of_int_to_binary_numbers(list):
    """ Convert a list of int to a list of binary number on 8 bit

    Args:
        list: A list of int to convert to a list of binary numbers

    Returns:
        binary_list: A list of binary numbers

    """

    binary_list = []
    for element in list:
        binary_list.append(format(element, '08b'))
    return binary_list


if __name__ == "__main__":
    #
    # initialize list
    #
    test = [65, 66, 67, 68]
    print('Result : \n')
    print(list_of_int_to_binary_numbers(test))

################################################################
#
# Step 4
#

""" Convert a list of binary numbers to a list of one big binary string

"""


def binary_list_to_binary_string(list):
    """Convert a list of binary numbers to a list of one big binary string

    Args:
        list: A list of binary numbers

    Returns:
        binary_string: A list of one big binary string

    """
    binary_string = "".join(list)
    return binary_string


if __name__ == "__main__":
    #
    # initialize list
    #
    test = ['01000001', '01000010', '01000011', '01000100']
    print('Result : \n')
    print(binary_list_to_binary_string(test))

################################################################
#
# Step 5
#


def binary_string_to_binary_list_of_6(String):
    """ Convert a String to a list of binary numbers string


    Args:
        list: A list of string

    Returns:
        binary_tab: A binary_list of list of 6 bit

    """

    binary_list = []
    # Convert the string into items of 6 characters long into a list
    for i in range(0, len(String), 6):
        binary_list.append(String[i: i+6])
        # We get the length of the last element of the list
    length_last_item = len(binary_list[len(binary_list)-1])
    if length_last_item < 6:
        str1 = binary_list.pop()
        # Calculate how many 0 you need to add
        # Concat the pop and the number of "0" required
        binary_list.append(str1 + "0" * (6 - length_last_item))
    return binary_list

# binary_list[len(binary_list)-1] => Get the index of the last element of binary_list(binary_list[5]and retrun'00')
# binary_list.pop() => Get the last item of my lits and remove it from it (My list no longer contains'00')


if __name__ == "__main__":
    #
    # initialize list
    #
    test = '01000001010000100100001101000100'
    print('Result binary_list_of_6_bit : \n')
    print(binary_string_to_binary_list_of_6(test))

################################################################
#
# Step 6
#

def binary_to_int(list):
    """

    Args:
        list: A list of binary numbers on 6 bits

    Returns:
        list_of_int : A list of int

    """
    binary_list = []
    for bits in list:
        binary_list.append(int(bits, 2))
    return binary_list


if __name__ == "__main__":
    #
    # initialize list
    #
    test = ["010000", "010100", "001001", "000011", "010001", "000000"]
    print('Result list_of_int : \n')
    print(binary_to_int(test))


################################################################
#
# Step 7
#


def list_to_base64(int_list):
    """

    Args:
        list: A list of int

    Returns:
        list_base64: A list of of converted int into base64

    """
    base64_dictionary = {
        'A': 0, 'Q': 16, 'g': 32, 'w': 48,
        'B': 1, 'R': 17, 'h': 33, 'x': 49,
        'C': 2, 'S': 18, 'i': 34, 'y': 50,
        'D': 3, 'T': 19, 'j': 35, 'z': 51,
        'E': 4, 'U': 20, 'k': 36, '0': 52,
        'F': 5, 'V': 21, 'l': 37, '1': 53,
        'G': 6, 'W': 22, 'm': 38, '2': 54,
        'H': 7, 'X': 23, 'n': 39, '3': 55,
        'I': 8, 'Y': 24, 'o': 40, '4': 56,
        'J': 9, 'Z': 25, 'p': 41, '5': 57,
        'K': 10, 'a': 26, 'q': 42, '6': 58,
        'L': 11, 'b': 27, 'r': 43, '7': 59,
        'M': 12, 'c': 28, 's': 44, '8': 60,
        'N': 13, 'd': 29, 't': 45, '9': 61,
        'O': 14, 'e': 30, 'u': 46, '+': 62,
        'P': 15, 'f': 31, 'v': 47, '/': 63
    }
    list_base64 = []

    # for each element of the given list => to obtain its equivalent in base 64 and add it to the empty list
    for element in int_list:
        list_base64.append(list(base64_dictionary.keys())[list(base64_dictionary.values()).index(element)])
    return list_base64


if __name__ == "__main__":
    #
    # initialize list
    #
    test = [16, 20, 9, 3, 17, 0]
    print('Result list_to_base64 : \n')
    print(list_to_base64(test))


################################################################
#
# Step 8
#

def add_equals(char_list):
    """

    Args:
        char_list: A list of char

    Returns:
        char_list: A list of char with 2 equals

    """
    tmp = True
    while tmp:
        # If the number of elements is a multiple of 4 => stop looping and display the list
        if (len(char_list) % 4) == 0:
            tmp = False
        # If the number of elements is not a multiple of 4 => continue to loop by adding "="
        if (len(char_list)%4) != 0:
            char_list.append("=")

    return char_list

if __name__ == "__main__":
    #
    # initialize list
    #
    test = ["Q", "U", "J", "D", "R", "A"]
    print('Result list_add_equals : \n')
    print(add_equals(test))


################################################################
#
# Step 8
#

def list_to_string(list_of_char):
    """

    Args:
        list_of_char: A list of char

    Returns:
        list_of_string: A list of string

    """
    list_of_string = ""
    for element in list_of_char:
        list_of_string += element
    return list_of_string


if __name__ == "__main__":
    #
    # initialize list
    #
    test = ["Q", "U", "J", "D", "R", "A", "=", "="]
    print('Result list_to_string : \n')
    print(list_to_string(test))



