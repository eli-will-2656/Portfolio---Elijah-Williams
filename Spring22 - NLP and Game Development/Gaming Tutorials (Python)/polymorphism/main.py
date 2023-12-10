from Animals import *

def describe(object):
    object.talk()
    object.coat()


def main():

    bill = Duck()
    mickey = Mouse()

    describe(bill)
    describe(mickey)

    print(__name__)


if __name__ == '__main__':
    main()
