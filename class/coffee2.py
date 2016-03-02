import random
import math


def generaterating():
    return(int(math.ceil(5*random.random())))

def main():
    print("This won't be printed when importing this module")


if __name__ == '__main__':
    main()
