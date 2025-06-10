"""Simple orchestrator selecting integration channel."""
from __future__ import annotations

from typing import Dict

from . import config
from .connectors import FHIRConnector, EDI278Gateway, RPABot
from .human_review import ManualReviewQueue
from .models import AuthorizationRequest


class Orchestrator:
    def __init__(self, manual_queue: ManualReviewQueue | None = None) -> None:
        self.manual_queue = manual_queue or ManualReviewQueue()
        self.channels: Dict[str, object] = {
            "api": FHIRConnector(),
            "edi": EDI278Gateway(),
            "rpa": RPABot(),
        }

    def process(self, request: AuthorizationRequest) -> None:
        channel_name = config.PAYER_CHANNELS.get(request.payer_id)
        if channel_name is None:
            self.manual_queue.add_task(request)
            return
        connector = self.channels[channel_name]
        try:
            connector.send(request)
        except Exception:
            # Fallback to manual review on error
            self.manual_queue.add_task(request)
