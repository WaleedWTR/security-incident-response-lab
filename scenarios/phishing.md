# Scenario IR-002: Phishing to Endpoint Execution

## Initial signal

A synthetic suspicious attachment is delivered and an Office application later spawns PowerShell with outbound network activity.

## Investigation

Review:

- message sender and authentication results
- recipients
- attachment/hash information
- process tree
- command line
- network destinations
- related file writes
- other devices/users with the same indicators

## Example containment

- quarantine or purge malicious messages where authorised
- block confirmed malicious indicators
- isolate confirmed compromised endpoints
- revoke sessions if identity compromise is suspected

## Recovery

- restore endpoint to trusted state
- validate security controls
- notify affected users as appropriate
- update detections and awareness material
