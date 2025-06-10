"""Demonstration script for the orchestrator."""
from uuid import uuid4

from .models import AuthorizationRequest
from .orchestrator import Orchestrator


def main() -> None:
    orchestrator = Orchestrator()
    request = AuthorizationRequest(
        request_id=str(uuid4()),
        patient_id="PATIENT1",
        payer_id="PAYER_API",
        service_codes=["PROC1"],
    )
    orchestrator.process(request)
    print(f"Status: {request.status}")
    for attempt in request.attempts:
        print(f"Attempt via {attempt.channel}: {attempt.response}")


if __name__ == "__main__":
    main()
