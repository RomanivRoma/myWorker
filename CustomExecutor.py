from queue import Queue
from WorkerThread import WorkerThread
from FutureResult import FutureResult
from WorkItem import WorkItem

class CustomExecutor:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.shutdown = False
        self.queue = Queue(maxsize=20)
        self.threads = []

    def execute(self, fn, *args):
        f = FutureResult()
        w = WorkItem(fn, args, f)
        self.queue.put(w)

        return f

    def map(self, func, args_array):
        fs = [self.execute(func, *args) for args in zip(args_array)]

        for i in range(self.max_workers):
            thread = WorkerThread(queue=self.queue)
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)
        return fs


    def shutdown(self):
        self.shutdown = True
        self.queue.put(None)
        return None
