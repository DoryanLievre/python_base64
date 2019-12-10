"""Convert a list of chars to a list of ints
"""


def char_list_to_int(list):
    # Convert String list to ascii values
    listOfInt = []
    for elements in list:
        listOfInt.extend(ord(num) for num in elements)
    return listOfInt


if  __name__ == "__main__":
    #
    # initialize list
    #
    test = ['A','B','C','D']
    print('Result : \n')
    print(char_list_to_int(test))
