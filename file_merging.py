def merge_txt_file():
    data = data2 = ""

    # Reading data from file1
    print("Reading data from first file")
    with open('file1.txt') as fp:
        data = fp.read()

    # Reading data from file2
    print("Reading data from second file")
    with open('file2.txt') as fp:
        data2 = fp.read()

        # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
    print("*************Combined data**************\n"+data)
    print("Writing combined data into third file")
    with open('file3.txt', 'w') as fp:
        fp.write(data)

if __name__ == "__main__":
    merge_txt_file()