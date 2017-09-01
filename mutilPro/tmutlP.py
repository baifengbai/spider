from multiprocessing import Process,Queue,Lock
import time


queue = Queue(10)


class Myprocess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop


    def run(self):
        global queue
        queue.put(self.loop)
        time.sleep(3)
        print 'Process:', self.loop


if __name__ == '__main__':
    i=0
    while queue.qsize()<4:
        print queue.qsize()
        time.sleep(1)
        p = Myprocess(i)
        p.daemon = True
        p.start()
        p.join()
        i += 1
    print('CPU number:' + str(Process.cpu_count()))
    for p in Process.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')