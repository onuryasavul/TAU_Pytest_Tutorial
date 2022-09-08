class Accumulator:

    def __init__(self, accum_val=0):
        self._count = accum_val

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more
