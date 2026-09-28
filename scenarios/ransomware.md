# Scenario IR-003: Ransomware-Style Activity

## Initial signal

A synthetic endpoint shows high-volume file rename activity followed by creation of a ransom-note artefact.

## Immediate priorities

- validate the signal
- identify affected endpoint(s)
- determine spread
- protect backups
- prevent further lateral movement
- preserve evidence

## Containment candidates

Depending on evidence and organisational procedure:

- isolate affected endpoints
- disable compromised identities
- block malicious infrastructure
- restrict affected network paths
- prevent known malicious binaries from executing

## Recovery principles

- eradicate persistence
- rebuild or restore from trusted sources
- validate backups before restoration
- monitor recovered systems
- complete post-incident review
