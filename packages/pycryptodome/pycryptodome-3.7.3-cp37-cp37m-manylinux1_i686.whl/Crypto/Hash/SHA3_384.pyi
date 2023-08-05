from typing import Union, Optional

Buffer = Union[bytes, bytearray, memoryview]

class SHA3_384_Hash(object):
    digest_size: int
    oid: str
    def __init__(self, data: Optional[Buffer], update_after_digest: bool) -> None: ...
    def update(self, data: Buffer) -> SHA3_384_Hash: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def new(self) -> SHA3_384_Hash: ...

def new(__data: Buffer = ..., update_after_digest: bool = ...) -> SHA3_384_Hash: ...

digest_size: int
