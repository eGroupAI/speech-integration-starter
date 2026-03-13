from __future__ import annotations

import wave
from pathlib import Path

from whisper_starter.pipeline import transcribe_file
from whisper_starter.providers.mock_provider import MockProvider


def _write_silent_wav(path: Path) -> None:
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(16000)
        wav.writeframes(b"\x00\x00" * 16000)


def test_transcribe_file_returns_segments(tmp_path: Path) -> None:
    audio = tmp_path / "hello_demo.wav"
    _write_silent_wav(audio)
    payload = transcribe_file(str(audio), "zh", provider=MockProvider())
    assert payload["language"] == "zh"
    assert len(payload["segments"]) == 1
    assert "hello demo" in payload["segments"][0]["text"]
