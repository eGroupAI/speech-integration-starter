"""Optional provider bridge for faster-whisper.

This file intentionally keeps only generic adapter code.
No production tuning strategy is included.
"""

from __future__ import annotations

from pathlib import Path

from .base import Segment


class FasterWhisperProvider:
    def __init__(self, model_name: str = "small") -> None:
        self.model_name = model_name
        try:
            from faster_whisper import WhisperModel  # type: ignore
        except Exception as exc:
            raise RuntimeError(
                "faster-whisper is not installed. "
                "Install it manually to use this provider."
            ) from exc
        self._model = WhisperModel(model_name)

    def transcribe(self, audio_path: Path, language: str) -> list[Segment]:
        segments, _ = self._model.transcribe(str(audio_path), language=language)
        return [
            Segment(start=float(seg.start), end=float(seg.end), text=seg.text.strip())
            for seg in segments
        ]
