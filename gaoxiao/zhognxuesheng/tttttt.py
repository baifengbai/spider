file1=file('E:\\school\yangguanggaokao\\zhongxuesheng')
for lines in file1:
    lines=lines.replace("\n",'')
    #print lines
    temp=lines.split("*")
    #print temp.__len__()
    file2 = file('E:\\school\yangguanggaokao\\zhongxuesheng-ex','a+')
    for tempp in range(1,temp.__len__()):
        print temp[0]+'\t'+temp[tempp]

        file2.write(temp[0]+'\t'+temp[tempp]+'\n')
    file2.close()
file1.close()