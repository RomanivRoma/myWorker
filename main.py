from datetime import datetime
from time import sleep
from CustomExecutor import CustomExecutor

if __name__ == '__main__':

    def longRunningTask(x):
        sleep(2)
        return x * 2
    exec = CustomExecutor(max_workers=2)
    futures = exec.map(longRunningTask, [1, 2, 3, 4, 5, 6])
    for f in futures:
        print("{} - {}".format(datetime.now(), f.result()))
        # print(f.getResult())


