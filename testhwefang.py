import sys

reload(sys)
sys.setdefaultencoding('utf8')
#file1=open("E:\\hfschool\\primary.txt")
file1=open("E:\\hfschool\\middle.txt")
#i=0
for line in file1:
   #i=i+1
   #print line
   data = line.split("\"")
   detail=data[4].split(" ")
   print detail.__len__()
   test1=data[1].split('*')
   print test1.__len__()
   #print data[1]+"*"+detail[1]+'*'+detail[2].replace("\n","")

   f = file('E:\\hfschool\\middlemap.txt', 'a+')
   new_content = data[1]+"*"+detail[1]+'*'+detail[2].replace("\n","")+ '\n'
   f.write(new_content)
   f.close()