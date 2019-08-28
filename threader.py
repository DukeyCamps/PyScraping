import sys
import parser
from queue import Queue
from threading import Thread, Lock, current_thread
import time
namelist = [ID for ID in parser.IDMAKER]
q = Queue()
for i in namelist:
    q.put(i)

# the queue is now constructed

list_lock = Lock()

def download_book():
    while True:
        with list_lock:
            ID = q.get()

        parser.requester.request_download(ID)
        print(current_thread().name, '\t done')
        q.task_done()

try:
	numberOfThreads = int(sys.argv[1])
	print('starting %d threads'%numberOfThreads, end = '')
	time.sleep(0.5)
	print('.', end = '')
	time.sleep(0.3)
	print('.', end = '')
	time.sleep(0.2)
except:
	numberOfThreads = 10

for t in range(numberOfThreads):
    t = Thread(target=download_book)
    t.daemon = True
    t.start()

q.join()
