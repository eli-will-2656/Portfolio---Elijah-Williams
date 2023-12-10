from re import *

pattern = \
    compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9+\.])+[a-z]{2,6}(\s|$)')


def get_address():
    address = input("Enter your email address: ")
    is_valid = pattern.match(address)

    if is_valid:
        print("Valid address: ", is_valid.group())
    else:
        print("Invalid address")
        get_address()


if __name__ == '__main__':
    get_address()

