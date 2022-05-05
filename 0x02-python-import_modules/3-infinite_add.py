if __name__ == "__main__":
    """Print the addition of all arguments."""
    from sys import argv
    add = sum(int(arg) for arg in argv[1:])
    print(add)
