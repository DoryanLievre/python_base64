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



if  __name__ == "__main__":
    #
    # initialize list
    #
    test = "ABCD"
    print('Result : \n')
    print(string_to_list(test))
