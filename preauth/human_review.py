from typing import List

from .models import AuthorizationRequest


class ManualReviewQueue:
    """Very small in-memory manual task queue."""

    def __init__(self) -> None:
        self._queue: List[AuthorizationRequest] = []

    def add_task(self, request: AuthorizationRequest) -> None:
        self._queue.append(request)
        request.status = "Pending Manual Review"

    def pop_task(self) -> AuthorizationRequest | None:
        if self._queue:
            return self._queue.pop(0)
        return None
