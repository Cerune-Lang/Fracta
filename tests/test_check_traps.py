import subprocess
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.check_traps import matches_trap


class TrapRecognitionTest(unittest.TestCase):
    def result(self, code, stdout=b"before\n", status=1):
        return subprocess.CompletedProcess(
            args=[], returncode=status, stdout=stdout,
            stderr=("cerune: runtime-v1 code=" + code + " origin=example\n").encode(),
        )

    def test_exact_expected_diagnostic_and_prior_output(self):
        self.assertTrue(matches_trap(self.result("division-by-zero"), "division-by-zero", "before\n"))

    def test_wrong_error_does_not_pass(self):
        self.assertFalse(matches_trap(self.result("integer-overflow"), "division-by-zero", "before\n"))

    def test_crash_does_not_pass(self):
        self.assertFalse(matches_trap(self.result("division-by-zero", status=-11), "division-by-zero", "before\n"))

    def test_wrong_prior_output_does_not_pass(self):
        self.assertFalse(matches_trap(self.result("division-by-zero", stdout=b""), "division-by-zero", "before\n"))


if __name__ == "__main__":
    unittest.main()
