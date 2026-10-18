# Fracta

[日本語](README.md) | English

Fracta is the official vulnerability-reproduction and security-behavior laboratory for [Cerune](https://github.com/Cerune-Lang/Cerune).

Its goals are to document small, authorized, reproducible `.ceru` cases; distinguish expected safety traps from genuine security defects; and preserve regression cases after fixes. Execution-path comparison belongs in [Parallax](https://github.com/Cerune-Lang/Parallax).

The initial `cases/checked_overflow.ceru` checks that signed 32-bit integer overflow is detected, **not** that a vulnerability exists.

```sh
cerune check cases/checked_overflow.ceru
cerune run cases/checked_overflow.ceru
cerune run-vm cases/checked_overflow.ceru
```

The check should pass; runtime execution should terminate with a checked-overflow error.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). **Do not disclose unpatched vulnerabilities in public issues or PRs.** The project is experimental, provides no security guarantee, and has not selected a license yet.
