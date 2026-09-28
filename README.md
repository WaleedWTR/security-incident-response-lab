# Security Incident Response Lab

![Incident timeline tests](https://github.com/WaleedWTR/security-incident-response-lab/actions/workflows/tests.yml/badge.svg)

A portfolio incident-response repository containing synthetic scenarios, evidence timelines and repeatable response playbooks.

> **Portfolio note:** Every incident and artefact in this repository is fictional/synthetic.

## Scenarios

- compromised account
- phishing
- ransomware-style endpoint incident

## What this project demonstrates

- incident triage
- evidence preservation
- timeline reconstruction
- scoping
- containment planning
- eradication and recovery
- stakeholder communication
- lessons learned
- MITRE ATT&CK-informed analysis

## Response lifecycle

```text
Prepare
  |
Detect / Report
  |
Triage
  |
Scope
  |
Contain
  |
Eradicate
  |
Recover
  |
Lessons learned
```

## Generate the synthetic timeline

```bash
python scripts/timeline.py
```

## Key documentation

- [Compromised account scenario](scenarios/compromised-account.md)
- [Phishing scenario](scenarios/phishing.md)
- [Ransomware-style scenario](scenarios/ransomware.md)
- [Triage playbook](playbooks/triage.md)
- [Communications playbook](playbooks/communications.md)
- [Evidence-handling principles](docs/evidence-handling.md)

## Skills demonstrated

**Incident Response · DFIR Fundamentals · Cyber Security · Evidence Handling · Threat Analysis · Python · Operational Coordination**
