from threading import Thread


class WorkerThread(Thread):
    def __init__(self, queue):
        super().__init__()
        self.q = queue


    def run(self):
        while True:
            item = self.q.get()
            if item is None: return
            res = item.run()
            item.future.setResult(res)

