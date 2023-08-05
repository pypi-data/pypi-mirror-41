from typing import Any

__all__ = ['new', 'get_random_bytes']

from os import urandom

class _UrandomRNG(object):

    def read(self, n: int) -> bytes:...
    def flush(self) -> None: ...
    def reinit(self) -> None: ...
    def close(self) -> None: ...

def new(*args: Any, **kwargs: Any) -> _UrandomRNG: ...

def atfork() -> None: ...

get_random_bytes = urandom

