# Auditor setup review

- Review date: 30 October 2026 (Australia/Melbourne).
- Scope: uncommitted auditor configuration and instructions based on `73c59947e3ad7f9946f8ac772ee1cbd2bea53860`.
- Reviewer: independent subagent `/root/review_auditor_setup`.
- Files reviewed: `.codex/config.toml`, `.codex/agents/research-auditor.toml`, `docs/RESEARCH_AUDIT.md`, and additions to `AGENTS.md` and `README.md`.
- Verdict: no material defects found within this configuration-only scope.

## Verified checks

Both TOML files parse and validate against the Codex Draft-07 configuration schema downloaded from the [official repository](https://github.com/openai/codex/blob/main/codex-rs/core/config.schema.json). The role path resolves relative to `.codex/config.toml`. The role declares a read-only sandbox and does not override the session's model.

The instructions cover paper identities, primary-text support for findings, funding/disclosure claims when asserted, data lineage, independent calculations, and rendered figures. They distinguish verified, contradicted, and unverified evidence. The guide separates descriptive charts from paper replications and prohibits treating configuration or a successful build as scientific verification.

## Unverified and unrun checks

A fresh trusted Codex session has not been tested for loading and exposing the named role. Schema validation does not prove runtime registration or primary-source access. The supported fallback is independent delegation with the role instructions and audit guide.

This review did not audit the wiki's papers, summaries, data, or graphs. Those require a separate research audit and evidence ledger.
