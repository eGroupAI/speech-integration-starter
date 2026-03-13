"""Public pipeline entry."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .providers.base import WhisperProvider


def transcribe_file(audio_path: str, language: str, provider: WhisperProvider) -> dict[str, Any]:
    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"audio file not found: {audio_path}")
    segments = provider.transcribe(path, language)
    return {
        "language": language,
        "segments": [
            {"start": seg.start, "end": seg.end, "text": seg.text}
            for seg in segments
        ],
    }
