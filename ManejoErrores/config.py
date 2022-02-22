def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("got a problem trying to read the file:",err)
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError:
        print("find config.txt but couldn't read it")
if __name__ == '__main__':
    main()