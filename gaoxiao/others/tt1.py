
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file1=file('C:\\Users\\Administrator\\Desktop\\tt1.txt')
a1=[]
for lines in file1:
    #print lines
    a1.append(lines)
file1.close()

j=0
file3=file('C:\\Users\\Administrator\\Desktop\\tt4.txt','a+')
flag=False
for i in range(0,a1.__len__()):
    print repr(str(a1[i]).split("\t")[5])
    file2 = file('C:\\Users\\Administrator\\Desktop\\tt2.txt')
    for lines1 in file2:
        if lines1.split('\t')[0].replace(" ",'').replace("\xc2\xa0",'')==str(a1[i]).split("\t")[5].replace("\n",'').replace(" ",'').replace("\xc2\xa0",''):
            #print str(a1[i]).replace("\n",'')+lines1
            file3.write(str(a1[i]).replace("\n",'').replace(" ",'').replace("\xc2\xa0",'')+'\t'+str(lines1.split('\t')[1]).replace("\n",'').replace(" ",'').replace("\xc2\xa0",'')+"\n")
            j+=1
            flag=True

    if flag:
        flag=False
    else:
        file3.write(str(a1[i]).replace("\n",'')+"\n")
    file2.close()
file3.close()
print j

