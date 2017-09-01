new_n=[]
new_n.append('zcdef')
new_n.append('asdfg')
new_n.append('qwert')
print new_n
for lines in new_n:
    print lines
path='E:\\school\\eolmajor1\\'+'ss'
path1 = unicode(path, 'utf-8')
file2 = file(path1, 'a+')
for lines in new_n:
    file2.write(lines)
file2.close()