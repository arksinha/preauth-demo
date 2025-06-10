from ..models import AuthorizationRequest, SubmissionAttempt


class RPABot:
    """Simulated RPA bot for payer portal."""

    channel_name = "rpa"

    def send(self, request: AuthorizationRequest) -> SubmissionAttempt:
        """Pretend to automate a payer portal submission."""
        attempt = SubmissionAttempt(channel=self.channel_name, success=True,
                                    response="Portal Submitted")
        request.attempts.append(attempt)
        request.status = "Submitted via RPA"
        return attempt
