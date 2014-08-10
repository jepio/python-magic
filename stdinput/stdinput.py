import fileinput

i = 0
for line in fileinput.input():
    i += 1
    line = line.strip()
    print("The ", i, " line is: ", line)
