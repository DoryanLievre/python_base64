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