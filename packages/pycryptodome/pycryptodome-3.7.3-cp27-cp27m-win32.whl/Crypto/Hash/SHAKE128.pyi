from typing import Union, Optional

Buffer = Union[bytes, bytearray, memoryview]

class SHAKE128_XOF(object):
    oid: str
    def __init__(self,
                 data: Optional[Buffer] = ...) -> None: ...
    def update(self, data: Buffer) -> SHAKE128_XOF: ...
    def read(self, length: int) -> bytes: ...
    def new(self, data: Optional[Buffer] = ...) -> SHAKE128_XOF: ...

def new(data: Optional[Buffer] = ...) -> SHAKE128_XOF: ...
