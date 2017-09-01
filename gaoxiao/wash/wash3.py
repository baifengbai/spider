
file4 = file('E:\\school\\schoolprovince\\zhuanyegrade_0_ex_0')
file5=file('E:\\school\\schoolprovince\\zhuanyegrade_0_ex_0_ex','a+')
i = 0
for lines in file4:
    lines_l=lines.split("*")
    if lines_l.__len__() == 11:
        pass
        # file5.write(lines)
    else :
        file5.write(lines)
file5.close()
file4.close()