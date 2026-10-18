# Case taxonomy / ケース分類

Fracta treats controlled failures as evidence of intended language safety checks, **not evidence of a security vulnerability**.

| Case | Expected diagnostic | Category | Goal |
| --- | --- | --- | --- |
| `checked_overflow` | `integer-overflow` | Arithmetic safety | Checked i32 overflow |
| `division_by_zero` | `division-by-zero` | Arithmetic safety | Reject zero divisor |
| `out_of_bounds` | `array-index-out-of-bounds` | Bounds safety | Reject invalid array index |
| `conversion_out_of_range` | `integer-conversion-out-of-range` | Conversion safety | Reject unrepresentable integer |

## Research workflow

1. Reproduce behavior in an authorized isolated environment.
2. Record source, Cerune commit, platform, command, expected outcome, and observed result.
3. Separate expected runtime traps from discrepancies and possible security defects.
4. Report undisclosed problems privately through `SECURITY.md`, **not** public issues.
5. After remediation or coordinated disclosure, add a minimal public regression fixture.

Fracta catalogs behavior and reproducibility. Parallax generates and compares inputs across execution routes. Both projects should avoid speculative CWE/CVE labels.
