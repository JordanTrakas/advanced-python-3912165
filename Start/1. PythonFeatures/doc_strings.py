# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def my_function(arg1, arg2=None):
    """
    :param arg1: This parameter is the first parameter
    :param arg2: This parameter is the second parameter
    :return: Prints out the two parameters and returns None
    :raises TypeError: If arg1 is not a string
    Example >>> my_function(1, 2)
    1 2
    """
    print(arg1, arg2)


def main():
    print(my_function.__doc__)


if __name__ == "__main__":
    main()
