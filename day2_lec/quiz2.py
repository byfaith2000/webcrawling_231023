continent = input('Enter the name of a continent: ')
continent = continent.title()

infile = open('UN.txt', 'r')
for line in infile:
    data = line.split(',')
    if data[1] == continent:
        print(data[0])