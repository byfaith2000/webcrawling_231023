# file1 = open('States.txt', 'r')
# rstr = file1.read()
# print(rstr)


infile2 = open('States.txt', 'r')
for line in infile2:
    print(line, end='')

print()
infile3 = open('States.txt', 'r')
ldata = [line for line in infile3]
#ldata = [line.rstrip() for line in infile3]

ldata.sort()
print(ldata)

outfile = open('StatesAlpha.txt', 'w')
outfile.writelines(ldata)
