import sys, os


def main(file_paths):
    # add checks for file columns
    first = True

    # check if first line is the same in all files being combined
    first_line = ""
    
    for fp in file_paths:
        # get file name and open file
        file_name = os.path.basename(fp)
        file = open(fp)
        
        # print first line only once
        if (first):
            first_line = file.readline().strip()
            print(first_line + ",\"filename\"")
            first = False
        else:
            # make 
            new_first_line = file.readline().strip()
            if first_line != new_first_line:
                print("combining failed, file column headings do not match")
                print(first_line)
                print(new_first_line)
                return
        
        # output each line and append filename
        for line in file:
            print(line.strip() + ",\"" + file_name+"\"")
        file.close()


if __name__ == "__main__":
    main(sys.argv[1:])