import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)

    def zero(self, printNumber):
        #todo
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber.accept(0)
            if i % 2 == 0:
                self.even_sem.release()
            else:
                self.odd_sem.release()

    def even(self, printNumber):
        #todo
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber.accept(i)
            self.zero_sem.release()

    def odd(self, printNumber):
        #todo
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber.accept(i)
            self.zero_sem.release()

class PrintNumber:
    def accept(self, x):
        print(x, end='')

def test_zero_even_odd():
    n = 8
    zeo = ZeroEvenOdd(n)
    pn = PrintNumber()

    threads = []
    threads.append(threading.Thread(target=zeo.zero, args=(pn,)))
    threads.append(threading.Thread(target=zeo.even, args=(pn,)))
    threads.append(threading.Thread(target=zeo.odd, args=(pn,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    test_zero_even_odd()