class FutureResult:
    hasResult = False
    _result = None

    def setResult(self, result):
        self._result = result
        if self._result is not None:
            self.hasResult = True

    def getResult(self):
        while not self.hasResult:
            pass
        return self._result

    def result(self):
        return self.getResult()
