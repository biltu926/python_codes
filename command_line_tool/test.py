import sys


class CommandLiner:

    def __init__(self, name = 'Default'):
        self.name = name

    def show_name(self):
        print('The name provided: {}'.format(self.name))


def main():

    print(sys.argv[1])


if __name__=='__main__':
    main()
