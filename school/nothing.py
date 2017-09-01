#- * - coding: utf - 8 - *
import sets
import sys
import chardet
reload(sys)
sys.setdefaultencoding("utf-8")
magic_char = sets.Set('合肥市小学')
poppins_chars = sets.Set('学时校市')
print ''.join(magic_char & poppins_chars)   #InterSection
st1= ''.join(magic_char & poppins_chars).decode("Windows-1252")
st2=st1.encode("utf-8")
print chardet.detect(st2)
print st1
print ''.join(magic_char | poppins_chars)   #Union