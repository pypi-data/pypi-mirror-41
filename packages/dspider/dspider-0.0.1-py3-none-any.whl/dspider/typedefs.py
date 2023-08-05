import asyncio

from collections.abc import AsyncIterable
from typing import TYPE_CHECKING, Any, Callable, Coroutine, Iterable, Tuple, Union

from aiohttp.typedefs import LooseCookies as Cookies
from aiohttp.typedefs import LooseHeaders as Headers

from .queue import Queue
from .request import Request
from .response import Response


BaseCoroutine = Coroutine[Any, Any, None]
BaseCallback = Callable[[], Union[None, BaseCoroutine]]
BoolCoroutine = Coroutine[Any, Any, bool]
Checker = Callable[[], Union[bool, BoolCoroutine]]
KeyMaker = Callable[[str], str]
Loop = asyncio.AbstractEventLoop
RequestQueueItem = Request
RespOrExc = Union[Response, BaseException]
ResponseQueueItem = Tuple[RespOrExc, Request]

if TYPE_CHECKING:  # pragma: no cover
    ResponseQueue = Queue[ResponseQueueItem]
    RequestQueue = Queue[RequestQueueItem]
    BaseQueue = Queue[Any]
    FutureReturnResponse = asyncio.Future[Response]
    AsyncStrIterable = AsyncIterable[str]
    AsyncRequestIterable = AsyncIterable[Request]
    BaseFuture = asyncio.Future[None]
else:
    BaseQueue = ResponseQueue = RequestQueue = Queue
    FutureReturnResponse = BaseFuture = asyncio.Future
    AsyncRequestIterable = AsyncStrIterable = AsyncIterable

LifecyleActionReturn = Union[Request, Iterable[Request], AsyncRequestIterable]
LifecyleAction = Coroutine[None, None, LifecyleActionReturn]

__all__ = (
    "AsyncRequestIterable",
    "AsyncStrIterable",
    "BaseCallback",
    "BaseCoroutine",
    "BaseFuture",
    "BaseQueue",
    "BoolCoroutine",
    "Checker",
    "Cookies",
    "FutureReturnResponse",
    "Headers",
    "KeyMaker",
    "LifecyleAction",
    "LifecyleActionReturn",
    "RequestQueue",
    "RequestQueueItem",
    "RespOrExc",
    "ResponseQueue",
    "ResponseQueueItem",
)
