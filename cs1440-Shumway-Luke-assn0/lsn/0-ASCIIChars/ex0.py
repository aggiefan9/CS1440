def displayASCII():
    # TODO: Display all printable ASCII characters in the range [32, 126].
    for i in range(32,127):
        print(f"Character #{str(i)} is {chr(i)}")

if __name__ == '__main__':
    displayASCII()
