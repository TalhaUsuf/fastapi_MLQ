""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random
from consumer import Consumer

class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(100):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify : item %d appended to queue by %s\n'\
                  % (item, self.name))
            time.sleep(0.1)




if __name__ == '__main__':
    queue = Queue()

    t1 = Producer(queue)
    
    t2 = Consumer(queue)
    


    t1.start()
    t2.start()

    
    t1.join()
