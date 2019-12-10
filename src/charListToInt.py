"""Convert a list of chars to a list of ints
"""

# Convert String list to ascii values
def charListToInt(list):
    listOfInt = []
    for elements in list:
        listOfInt.extend(ord(num) for num in elements)
    return listOfInt


# initialize list
# test = ['A','B','C','D']
# print('Result : \n')
# print(charListToInt(test))