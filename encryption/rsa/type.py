from multipledispatch import dispatch
from sympy import randprime

class __rawData__(list[int]):
    pass

class __rawEncrypted__(list[int]):
    pass

class publicRSAkey:
    def __init__(self, n: int, e: int):
        self.n = n
        self.e = e

class privateRSAkey:
    def __init__(self, n: int, d: int, e: int):
        self.n = n
        self.d = d
        self.e = e
    def public(self) -> publicRSAkey:
        return publicRSAkey(self.e, self.e)


class fullRSAkey:
    n: "int"
    e: "int"
    d: "int"
    ct: "int"
    p: "int"
    q: "int"
    @dispatch()
    # Initilize blank key.
    def __init__(self):
        pass
    @dispatch(int)
    # Initilize key from random size (2**sz) bits
    def __init__(self, sz: int):
        self = fullRSAkey(randprime(1, 2**sz), randprime(1, 2**sz))
    @dispatch(int, int)
    # Initilize key from p and q
    def __init__(self, p: int, q: int):
        pass
    def private(self) -> privateRSAkey:
        return privateRSAkey(self.n, self.d, self.e)