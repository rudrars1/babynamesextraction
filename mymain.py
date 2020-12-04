import os
import re
import sys

path='/home/rudrars1/Downloads/google-python-exercises/babynames/'

filelist=os.listdir(path)
filelistcopy=[]
for x in filelist:
    if x.endswith('html'):
        filelistcopy.append(x)
filelist=filelistcopy
#print(filelist)


for file in filelist:
    f = open(path+file, 'r')
    data = f.read()
    rank = {}
    names = []
    text = []
    woo = re.findall(r'<td>\d+</td><td>\w+</td><td>\w+</td>', data)
    yearlist = re.findall(r'Popularity\sin\s(\d\d\d\d)', data)
    year = yearlist[0]
    for x in woo:
        element = re.findall(r'<td>\w+</td>', x)

        # trimming the unnecessary and assigning ranks
        for e in range(3):
            if (e == 0):
                xrank = element[e][4:-5]
            elif (e == 1):
                ele = element[e][4:-5]
                rank[ele] = xrank
                names.append(ele)
            elif (e == 2):
                ele = element[e][4:-5]
                rank[ele] = xrank
                names.append(ele)

    names = list(set(names))
    # note that names.sort() has no return value so do not put it in the print statement
    names.sort()
    # print(names)

    text.append(year)
    for name in names:
        text.append(name + ' ' + rank[name])
    # convert list to text
    text = '\n'.join(text)
    text=text+'\n'
    fn=file[:-5]
    writefile=open('/home/rudrars1/Downloads/google-python-exercises/babynames/writtendata/'+fn+'.txt','w')
    writefile.write(text)
    writefile.close()
    # print('\n'.join(text))










