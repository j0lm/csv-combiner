import os

def main():
    os.system("echo running tests... > output.txt")
    path = "./fixtures"
    file_list = os.listdir(path)
    size = len(file_list)


    # test if program copies one file
    runnum = 0
    for file in file_list:
        test_files = [file]
        os.system("python csv-combiner.py ./fixtures/" + file + " > ./output/output" + str(runnum))
        run_test(test_files, runnum)
        runnum = runnum + 1


    # combine two files
    index = 0
    for file in file_list:
        test_files = [file_list[index], file_list[(index + 1) % size]]
        cmd = "python csv-combiner.py"
        for f in test_files:
            cmd = cmd + " ./fixtures/" + f
        cmd = cmd + " > ./output/output" + str(runnum)
        os.system(cmd)
        run_test(test_files, runnum)
        runnum = runnum + 1
        index = index + 1

    #combine three files
    index = 0
    for file in file_list:
        test_files = [file_list[index], file_list[(index + 1) % size], file_list[(index + 2) % size]]
        cmd = "python csv-combiner.py"
        for f in test_files:
            cmd = cmd + " ./fixtures/" + f
        cmd = cmd + " > ./output/output" + str(runnum)
        os.system(cmd)
        run_test(test_files, runnum)
        runnum = runnum + 1
        index = index + 1
    

def run_test(file_list, runnum):
    output = open("./output/output" + str(runnum))
    first = True
    for file in file_list:
        cur_file = open("./fixtures/" + file)
        
        for line in cur_file:
            if first:
                titles = line.strip() + ",\"filename\""
                output_title = output.readline().strip()
                if titles != output_title:
                    print("failed test with files: " + str(file_list))
                    return
                first = False
                continue
            
            original_line = line.strip() + ",\"" + file + "\""
            output_line = output.readline().strip()
            if original_line != output_line:
                print("failed test with files: " + str(file_list) + "\toriginal: " + original_line + "\toutput: " + output_line)
                return
        cur_file.close()
    output.close()
    print("passed test with files: " + str(file_list))
        
    
    

if __name__ == "__main__":
    main()