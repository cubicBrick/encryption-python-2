from multipledispatch import dispatch
from sympy import randprime

class fullRSAkey:
    @dispatch()
    # Initilize blank key.
    def __init__(self):
        pass
    @dispatch(int)
    # Initilize key from random size (2**sz) bits
    def __init__(self, sz: int):
        self.__init__(randprime(1, 2**sz), randprime(1, 2**sz))
    @dispatch(int, int)
    # Initilize key from p and q
    def __init__(self, p: int, q: int):
        pass