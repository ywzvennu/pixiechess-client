from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import Any, Callable, Coroutine, Generic, TypeVar

T = TypeVar("T")


class PageIterator(Iterator[T], Generic[T]):
    """Sync auto-paginating iterator.

    Lazily fetches pages and yields items one at a time.
    Stops when the returned page is empty or page exceeds total_pages.
    """

    def __init__(
        self,
        fetch_page: Callable[[int], dict[str, Any]],
        parse_items: Callable[[dict[str, Any]], list[T]],
        start_page: int = 1,
        total_pages_key: str | None = "totalPages",
    ) -> None:
        self._fetch = fetch_page
        self._parse = parse_items
        self._page = start_page
        self._total_pages: int | None = None
        self._total_pages_key = total_pages_key
        self._buffer: list[T] = []
        self._exhausted = False

    def __iter__(self) -> PageIterator[T]:
        return self

    def __next__(self) -> T:
        while not self._buffer:
            if self._exhausted:
                raise StopIteration
            if self._total_pages is not None and self._page > self._total_pages:
                raise StopIteration
            data = self._fetch(self._page)
            if self._total_pages_key and self._total_pages is None:
                self._total_pages = data.get(self._total_pages_key)
            items = self._parse(data)
            if not items:
                self._exhausted = True
                raise StopIteration
            self._buffer = items
            self._page += 1
        return self._buffer.pop(0)


class AsyncPageIterator(AsyncIterator[T], Generic[T]):
    """Async auto-paginating iterator."""

    def __init__(
        self,
        fetch_page: Callable[[int], Coroutine[Any, Any, dict[str, Any]]],
        parse_items: Callable[[dict[str, Any]], list[T]],
        start_page: int = 1,
        total_pages_key: str | None = "totalPages",
    ) -> None:
        self._fetch = fetch_page
        self._parse = parse_items
        self._page = start_page
        self._total_pages: int | None = None
        self._total_pages_key = total_pages_key
        self._buffer: list[T] = []
        self._exhausted = False

    def __aiter__(self) -> AsyncPageIterator[T]:
        return self

    async def __anext__(self) -> T:
        while not self._buffer:
            if self._exhausted:
                raise StopAsyncIteration
            if self._total_pages is not None and self._page > self._total_pages:
                raise StopAsyncIteration
            data = await self._fetch(self._page)
            if self._total_pages_key and self._total_pages is None:
                self._total_pages = data.get(self._total_pages_key)
            items = self._parse(data)
            if not items:
                self._exhausted = True
                raise StopAsyncIteration
            self._buffer = items
            self._page += 1
        return self._buffer.pop(0)
