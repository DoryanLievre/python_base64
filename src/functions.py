""" All function to Encode/ Decode

"""

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

#
# Step 7
#

