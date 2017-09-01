# -*- coding: utf-8 -*


file1 = file('E:\\school\\schoolprovince\\schoolprovince\\9w-end')
i = 1
file2 = file('E:\\school\\schoolprovince\\schoolprovince\\9w-end_0','a+')
file3 = file('E:\\school\\schoolprovince\\schoolprovince\\9w-end_0_ex','a+')
for lines in file1:
    print i
    lines_l=lines.split("*")
    if lines_l.__len__()==11:
        file2.write(lines)
    else :
        file3.write(lines)
    i += 1
file3.close()
file2.close()
file1.close()