file3 = file('E:\\school\\schoolprovince\\zhuanyegrade_0_ex','a+')
file4 = file('E:\\school\\schoolprovince\\zhuanyegrade_0_ex_0','a+')
i = 0
for lines in file3:
    if i%2 == 0:
        lines=lines.replace("\n", '')
    i +=1
    file4.write(lines)
file3.close()
file4.close()