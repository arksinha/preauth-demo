"""Sample configuration for payer integration."""

# Mapping of payer_id to preferred channel
PAYER_CHANNELS = {
    "PAYER_API": "api",
    "PAYER_EDI": "edi",
    "PAYER_PORTAL": "rpa",
}
