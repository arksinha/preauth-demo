from typing import Any

from ..models import AuthorizationRequest, SubmissionAttempt


class FHIRConnector:
    """Simulated RESTful FHIR API connector."""

    channel_name = "api"

    def send(self, request: AuthorizationRequest) -> SubmissionAttempt:
        """Pretend to submit the request via RESTful API."""
        # In a real implementation, convert to FHIR and POST to payer API.
        attempt = SubmissionAttempt(channel=self.channel_name, success=True,
                                    response="202 Accepted")
        request.attempts.append(attempt)
        request.status = "Submitted via API"
        return attempt
