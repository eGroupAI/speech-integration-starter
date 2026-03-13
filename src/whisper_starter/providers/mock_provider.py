"""Mock provider for tests and CI."""

from __future__ import annotations

from pathlib import Path

from .base import Segment


class MockProvider:
    def transcribe(self, audio_path: Path, language: str) -> list[Segment]:
        stem = audio_path.stem.replace("_", " ")
        text = stem if stem else "demo transcript"
        return [Segment(start=0.0, end=1.0, text=f"[{language}] {text}")]
