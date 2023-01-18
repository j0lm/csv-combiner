import sys, os


def main(file_paths):
    # add checks for file columns
    first = True
    for fp in file_paths:
        # get file name and open file
        file_name = os.path.basename(fp)
        file = open(fp)
        
        # print first line only once
        if (first):
            titles = file.readline().strip()
            print(titles + ",\"filename\"")
            first = False
        else:
            file.readline()
        
        # output each line and append filename
        for line in file:
            print(line.strip() + ",\"" + file_name+"\"")
        file.close()


if __name__ == "__main__":
    main(sys.argv[1:])