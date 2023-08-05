from typing import Union, Optional

Buffer = Union[bytes, bytearray, memoryview]

class SHA1Hash(object):
    digest_size: int
    block_size: int
    oid: str

    def __init__(self, data: Optional[Buffer] = ...) -> None: ...
    def update(self, data: Buffer) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> SHA1Hash: ...
    def new(self, data: Optional[Buffer] = ...) -> SHA1Hash: ...

def new(data: Optional[Buffer] = ...) -> SHA1Hash: ...
digest_size: int
block_size: int
