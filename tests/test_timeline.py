from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from timeline import group_by_case, load, render_case  # noqa: E402

def test_three_cases_exist():
    assert set(group_by_case(load())) == {"IR-001", "IR-002", "IR-003"}

def test_events_are_chronological():
    rows = load()
    timestamps = [r["timestamp"] for r in rows]
    assert timestamps == sorted(timestamps)

def test_render_includes_case_and_evidence():
    cases = group_by_case(load())
    output = render_case("IR-002", cases["IR-002"])
    assert "IR-002" in output
    assert "PowerShell" in output
