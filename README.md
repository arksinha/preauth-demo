# Preauth Demo

This repository contains a minimal demonstration of a pre-authorization
automation platform. It includes:

- Simple data models for prior authorization requests.
- A lightweight orchestrator that selects a payer integration channel.
- Example connectors for FHIR API, EDI 278, and an RPA portal bot.
- A manual review queue for human fallback.

## Running the demo

The `run_demo.py` script processes a sample authorization request and prints
its status and submission attempts.

```bash
python -m preauth.run_demo
```
