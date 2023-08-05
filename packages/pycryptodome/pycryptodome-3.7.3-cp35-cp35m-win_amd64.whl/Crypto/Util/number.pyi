from typing import List, Optional, Callable


def ceil_div(n: int, d: int) -> int: ...
def size (N: int) -> int: ...
def getRandomInteger(N: int, randfunc: Optional[Callable]=None) -> int: ...
def getRandomRange(a: int, b: int, randfunc: Optional[Callable]=None) -> int: ...
def getRandomNBitInteger(N: int, randfunc: Optional[Callable]=None) -> int: ...
def GCD(x: int,y: int) -> int: ...
def inverse(u: int, v: int) -> int: ...
def getPrime(N: int, randfunc: Optional[Callable]=None) -> int: ...
def getStrongPrime(N: int, e: Optional[int]=0, false_positive_prob: Optional[float]=1e-6, randfunc: Optional[Callable]=None) -> int: ...
def isPrime(N: int, false_positive_prob: Optional[float]=1e-6, randfunc: Optional[Callable]=None) -> bool: ...
def long_to_bytes(n: int, blocksize: Optional[int]=0) -> bytes: ...
def bytes_to_long(s: bytes) -> int: ...
def long2str(n: int, blocksize: Optional[int]=0) -> bytes: ...
def str2long(s: bytes) -> int: ...

sieve_base: List[int]
