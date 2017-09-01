file1=file('E:\\school\\schoolprovince\\zhuanyegrade_0')
file2=file('E:\\school\\schoolprovince\\zhuanyegrade_0e', "a+")
for lines in file1:
    lines=lines.replace("\xc2\xa0", "").replace(" ",'')
    file2.write(lines)
file2.close()
file1.close()