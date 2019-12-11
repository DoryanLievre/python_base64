from src import *

def main():
    print('Base 64 encoder.')
    while True :
        user_input = input('Enter a string to encode or e(X)it: ')
        #
        # Exit if user types 'x' or 'X'
        #
        if user_input.upper() == 'X':
            print('Exiting Base 64 encoder')
            break
        #
        # Calling the first function (step #1 of the algorithm)
        #
        encoded_string = string_to_list(user_input)
        print(f'{encoded_string}')

if __name__ == '__main__':
    #
    # Execute main when the module is directly given to Python Interpreter
    # but not when the module is imported in another module
    #
    main()