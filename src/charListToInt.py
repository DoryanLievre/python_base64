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
    test = ['A','B','C','D']
    print('Result : \n')
    print(char_list_to_int(test))
