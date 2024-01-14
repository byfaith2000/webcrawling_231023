
infile1 = open('USPres.txt')
infile2 = open('VPres.txt')

sdata1 = {line for line in infile1}
sdata2 = {line for line in infile2}

idata = sdata1.intersection(sdata2)
ldata = sorted(idata)
print(ldata)

outfile = open('both.txt', 'w')
outfile.writelines(ldata)
