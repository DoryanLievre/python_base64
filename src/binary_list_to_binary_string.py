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
