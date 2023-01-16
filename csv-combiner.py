import sys, os


def main(file_paths):
    print('combining csv files...')
    for fp in file_paths:
        # get file name
        file_name = os.path.basename(fp)
        file = open(fp)
        # output each line and append filename
        for line in file:
            print(line + "," + file_name)
        file.close()


if __name__ == "__main__":
    main(sys.argv[1:])