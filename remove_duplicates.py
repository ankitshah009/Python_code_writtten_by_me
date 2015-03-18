lines = open('HCORDIC/HCORDIC_complete/output1.txt', 'r').readlines()

lines_set = set(lines)

out  = open('workfile.txt', 'w')

for line in lines_set:
    out.write(line)
