from src import *

def main():
    print('Base 64 encoder.')
    while True :
        user_input = input('Enter a string to encode or e(X)it: ')
        #
        #Exit if user types 'x' or 'X'
        #
        if user_input.upper() == 'X':
            print('Exiting Base 64 encoder')
            break
        #
        #Calling the first function (step #1 of the algorithm)
        #
        encoded_string = stringToList(user_input)
        print(f'{encoded_string}')

if __name__ == '__main__':
    main()