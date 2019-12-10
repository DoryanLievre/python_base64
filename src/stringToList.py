"""Convert a string to a list of chars
"""


def string_to_list(string):
    # Convert String to a list of chars
    return [char for char in string]



if  __name__ == "__main__":
    #
    # initialize list
    #
    test = "ABCD"
    print('Result : \n')
    print(string_to_list(test))
