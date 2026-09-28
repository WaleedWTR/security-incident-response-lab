# Scenario IR-001: Compromised Account

## Initial signal

Repeated authentication failures are followed by a successful sign-in from the same synthetic source. A new mailbox rule is then observed.

## Triage questions

- Is the source expected for the user?
- Is the device/session known?
- Were MFA and Conditional Access satisfied?
- Are there other successful sign-ins from the source?
- Was mailbox configuration changed?
- Was sensitive data accessed?

## Example containment

Subject to organisational procedure and confirmed compromise:

- revoke active sessions
- reset credentials
- require strong re-authentication
- remove malicious mailbox rules
- review registered authentication methods
- inspect related cloud activity

## Recovery

- confirm known-good account state
- validate legitimate mailbox settings
- monitor for re-entry
- review how credentials were obtained
