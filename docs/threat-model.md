# Threat Model (Public Repo Boundary)

## Goal

讓社群可以快速整合 ASR，但不能反推商業核心能力。

## Explicitly Out of Scope

- Prompt engineering assets
- Production routing and model-selection policy
- Customer lexicon and correction pipelines
- Internal service orchestration details

## Allowed Surface

- Generic provider adapter pattern
- Mock-based integration test workflow
- Public JSON output schema and tooling
