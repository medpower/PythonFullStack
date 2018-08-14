# -*- coding: utf-8 -*-

import threading

class MutliThread(threading.Thread):

    def __init__(self, threadName,num):
        threading.Thread.__init__(self)
        self.name = threadName
        self.num = num

    def run(self):
        for i in range(self.num):
            print("{0} i={1}".format(threading.current_thread().getName(), i))

if __name__ == '__main__':
    thr1 = MutliThread("thread1",3)
    thr2 = MutliThread("thread2",2)
    #启动线程
    thr1.start()
    thr2.start()

    thr1.join()
    thr2.join()
    print("{0} 线程结束".format(threading.current_thread().getName()))