"""Smoke tests for the executable Python examples."""

from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


def run_example(filename: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "python" / filename)],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


class PythonExampleTests(unittest.TestCase):
    def test_basic_multiple_inheritance(self) -> None:
        output = run_example("01_basic_multiple_inheritance.py")
        self.assertIn("printing document", output)
        self.assertIn("scanning document", output)

    def test_diamond_calls_base_once(self) -> None:
        output = run_example("02_diamond_problem.py")
        self.assertIn("Call order: D -> B -> C -> A", output)
        self.assertIn("A appears once: True", output)

    def test_super_follows_mro(self) -> None:
        output = run_example("03_mro_and_super.py")
        self.assertIn("Execution: Service -> LoggingMixin -> ValidationMixin -> Root", output)

    def test_method_conflict_uses_first_parent(self) -> None:
        output = run_example("04_method_conflicts.py")
        self.assertIn("D.speak(): B", output)

    def test_mixins_compose_cooperatively(self) -> None:
        output = run_example("05_cooperative_mixins.py")
        self.assertIn("Pipeline: authenticated -> timed -> handled /profile", output)
        self.assertIn("Rejected request: Authentication is required", output)

    def test_composition_example(self) -> None:
        output = run_example("06_composition_over_inheritance.py")
        self.assertIn("printed: scanned: report.pdf", output)


if __name__ == "__main__":
    unittest.main()

