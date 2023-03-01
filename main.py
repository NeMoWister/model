import random
import threading
import time

t_queue = time.strftime('%S', time.localtime())  # момент поступления
t_proc = time.strftime('%S', time.localtime())  # время в обработке
count = 2
t_sum = 0
k = 0
times = 0
mcount = 2


def thr_pro():
    time.sleep(random.randint(1, 13))


class Thr(threading.Thread):

    def __init__(self, th_n, queue=True, event=threading.Event()):
        super().__init__()
        self.th_n = th_n
        self.queue = queue
        self.event = event

    def get_status(self):
        self.th_n.isAlive()

    def start_thr(self):
        self.th_n = threading.Thread(target=thr_pro)
        self.th_n.start()
        self.th_n.join()
        self.event.set()

    def wait(self):
        self.event.wait()
        return True


tr1 = Thr("tr1")
tr2 = Thr("tr2")

while k < 1000:
    tr1.start(), tr2.start_thr()
