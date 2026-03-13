"""Provider protocol for ASR backends."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass
class Segment:
    start: float
    end: float
    text: str


class WhisperProvider(Protocol):
    def transcribe(self, audio_path: Path, language: str) -> list[Segment]:
        """Return transcription segments."""
