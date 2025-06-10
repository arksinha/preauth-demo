from ..models import AuthorizationRequest, SubmissionAttempt


class EDI278Gateway:
    """Simulated EDI 278 connector."""

    channel_name = "edi"

    def send(self, request: AuthorizationRequest) -> SubmissionAttempt:
        """Pretend to send an X12 278 transaction."""
        attempt = SubmissionAttempt(channel=self.channel_name, success=True,
                                    response="EDI ACK")
        request.attempts.append(attempt)
        request.status = "Submitted via EDI"
        return attempt
