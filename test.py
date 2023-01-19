import os, sys

def main(argv):
    print("running tests...")
    path = str(argv[1])
    file_list = os.listdir(path)
    size = len(file_list)


    # test if program copies one file
    runnum = 0
    for file in file_list:
        test_files = [file]
        # run command
        os.system("python csv-combiner.py "+ path + file + " > ./output/output" + str(runnum) + ".csv")
        
        run_test(test_files, runnum, path)
        runnum = runnum + 1


    # combine two files
    index = 0
    for file in file_list:
        test_files = [file_list[index], file_list[(index + 1) % size]]
        
        # create command
        cmd = "python csv-combiner.py"
        for f in test_files:
            cmd = cmd + " " + path + f
            
        #run command
        cmd = cmd + " > ./output/output" + str(runnum) + ".csv"
        os.system(cmd)
        run_test(test_files, runnum, path)
        runnum = runnum + 1
        index = index + 1

    #combine three files
    index = 0
    for file in file_list:
        test_files = [file_list[index], file_list[(index + 1) % size], file_list[(index + 2) % size]]
        
        # create command
        cmd = "python csv-combiner.py"
        for f in test_files:
            cmd = cmd + " " + path + f
        cmd = cmd + " > ./output/output" + str(runnum) + ".csv"
        
        # run command
        os.system(cmd)
        
        run_test(test_files, runnum, path)
        runnum = runnum + 1
        index = index + 1
    

def run_test(file_list, runnum, path):
    output = open("./output/output" + str(runnum) + ".csv")
    first_title = True
    # go through every file to check if program output is correct
    for file in file_list:
        cur_file = open(path + file)
        first_line = True;
        for line in cur_file:
            # compare first line of output and skip first lines of input files
            if first_line:
                if first_title:
                    titles = line.strip() + ",\"filename\""
                    output_title = output.readline().strip()
                    if titles != output_title:
                        print("failed test with files: " + str(file_list))
                        return
                    first_title = False
                first_line = False
                continue
            else:            
                original_line = line.strip() + ",\"" + file + "\""
                output_line = output.readline().strip()
                if original_line != output_line:
                    print("failed test with files: " + str(file_list))
                    print("original: " + original_line)
                    print("output: " + output_line)
                    return
        cur_file.close()
    output.close()
    print("passed test with files: " + str(file_list))
           

if __name__ == "__main__":
    main(sys.argv)