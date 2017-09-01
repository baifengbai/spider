from multiprocessing import Pool
import multiprocessing
import time

Num = 0

def reu2():
    return 1,2


def get_i(i, Name, ct, ct2):
    # global Num
    time.sleep(1)
    Name.x += 1
    ct.append(Name.x)
    ct2.append(Name.x*2)
    return i*10


def main():
    global Num
    mgr = multiprocessing.Manager()
    Name = mgr.Namespace()
    Name.x = Num
    ct = mgr.list()
    ct2 = mgr.list()
    pool = Pool(processes=10)
    res = []
    for i in range(10):
        result = pool.apply_async(get_i, (i, Name, ct, ct2, ))
        res.append(result.get())
    pool.close()
    pool.join()
    Num = Name.x
    print "ct:", ct
    print "ct2:", ct2
    print res
    print "ok"

if __name__ == "__main__":
    Num = 0
    a,b=reu2()
    print a
    print b
    for j in range(3):
        main()
        pass
    print Num