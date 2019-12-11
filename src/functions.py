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


if  __name__ == "__main__":
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

    binary_list =[]
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
    """

    Args:
        list: A list of binary numbers

    Returns:
        binary_string: A list of one big binary string

    """
    binary_string ="".join(list)
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
