from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Attachment:
    """Represents a supporting document for a request."""
    filename: str
    content_type: str
    path: str


@dataclass
class SubmissionAttempt:
    """Record of a submission attempt to a payer."""
    channel: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    success: bool = False
    response: Optional[str] = None


@dataclass
class AuthorizationRequest:
    """Core entity for each prior authorization request."""
    request_id: str
    patient_id: str
    payer_id: str
    service_codes: List[str]
    status: str = "Received"
    attempts: List[SubmissionAttempt] = field(default_factory=list)
    attachments: List[Attachment] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
