"""Generate a tiny demo wav file for smoke tests."""

from __future__ import annotations

import wave
from pathlib import Path


def main() -> None:
    out = Path("out/demo.wav")
    out.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(out), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(16000)
        wav.writeframes(b"\x00\x00" * 16000)
    print(f"generated: {out}")


if __name__ == "__main__":
    main()
