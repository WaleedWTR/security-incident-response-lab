#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_events.csv"

def load():
    with DATA.open(newline="", encoding="utf-8") as handle:
        return sorted(csv.DictReader(handle), key=lambda row: row["timestamp"])

def group_by_case(rows):
    cases = defaultdict(list)
    for row in rows:
        cases[row["case_id"]].append(row)
    return dict(cases)

def render_case(case_id, events):
    lines = [f"# {case_id}"]
    for event in events:
        lines.append(
            f'{event["timestamp"]} | {event["source"]} | '
            f'{event["entity"]} | {event["severity"].upper()} | {event["event"]}'
        )
    return "\n".join(lines)

if __name__ == "__main__":
    for case_id, events in group_by_case(load()).items():
        print(render_case(case_id, events))
        print()
