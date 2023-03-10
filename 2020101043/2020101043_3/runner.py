import sys
import os

# command line arguments: 
# 1. hadoop file address
# 2. input file address
# 3. input directory address (where to copy input files in HDFS)
# 4. output directory address (where to copy output files in HDFS)
# 5. address of the directory where mappers and reducers are stored

# get args
hadoop_file = sys.argv[1]
input_file = sys.argv[2]
input_dir = sys.argv[3]
output_dir = sys.argv[4]
mappers_reducers_dir = sys.argv[5]

# modify the input format in input file 
f = open(input_file, 'r+')
lines = f.readlines()
f.truncate(0)

i, row = 0, 0
m, n, p = -1, -1, -1
second = False
first_dict = {}

for line in lines:
    line = line.strip()
    if i == 0:
        m, n = [ int(x) for x in line.split() ]
        i += 1
        row = 0
        continue 
    if m != -1 and n != -1 and i == m + 1:
        n, p = [ int(x) for x in line.split() ]
        for key, v in first_dict.items():
            for k in range(p):
                f.write('%s %s\t%s' % (str(key), str(k), "0 " + v) )   
                # with open ("t2.txt", "a+") as f:  
                    # f.write("first: ") 
                    # f.write('%s %s\t%s\n' % (str(key), str(k), "0 " + v) )
        i += 1
        row = 0
        second = True
        continue

    # with open ("t2.txt", "a") as f:
    #     f.write(line)

    if second == False:
        first_dict[row] = line 
    else:
        j = 0
        words = line.split()
        for word in words:
            # word = word.strip()
            for k in range(p):
                f.write('%s %s\t%s %s %s %s' % (str(k), str(j), "1", word, str(row), str(p)))
                # with open ("t2.txt", "a+") as f:
                    # f.write("second: ")
                    # f.write('%s %s\t%s\n' % (str(k), str(j), "1 " + word + ' ' + str(row) + ' ' + str(p)))
            j += 1

    i += 1
    row += 1

# hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -input /input/input.txt -output /output -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file mapper.py -file reducer.py

# copy input file to HDFS
os.system('hdfs dfs -mkdir ' + input_dir)
os.system('hdfs dfs -put ' + input_file + ' ' + input_dir)

# run hadoop
os.system('hadoop jar ' + hadoop_file + ' -input ' + input_dir + ' -output ' + output_dir + ' -mapper "python3 ' + mappers_reducers_dir + '/mapper.py" -reducer "python3 ' + mappers_reducers_dir + '/reducer.py" -file ' + mappers_reducers_dir + '/mapper.py -file ' + mappers_reducers_dir + '/reducer.py')
