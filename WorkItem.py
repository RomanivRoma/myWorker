class WorkItem:
    def __init__(self, func, arg, future):
        self.func = func
        self.arg = arg
        self.future = future

    def run(self):
        result = self.func(*self.arg)
        return result
