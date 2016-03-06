import sys

if __name__ == "__main__":

    param = sys.argv

    print(param)
    
    for index, str in enumerate(param):
        print(index, str)
