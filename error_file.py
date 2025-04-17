try:
    with open("sample.txt", "r") as file2:
        read3_file=file2.read()
        print(read3_file)
except IndentationError:
    print("")
finally:
    print("Error: The file 'sample.txt' was not found.")