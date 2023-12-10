import dundername1

print(f"The name attribute of dundername2.py is {__name__}")

if __name__ == '__main__':
    print("This file is being executed as a main program")
else:
    print("This file is being imported into another program")
