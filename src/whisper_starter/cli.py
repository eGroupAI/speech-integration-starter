"""CLI for whisper starter."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .pipeline import transcribe_file
from .providers.faster_whisper_provider import FasterWhisperProvider
from .providers.mock_provider import MockProvider


def _provider_from_name(name: str):
    if name == "mock":
        return MockProvider()
    if name == "faster-whisper":
        return FasterWhisperProvider()
    raise ValueError(f"unsupported provider: {name}")


def transcribe_command(input_path: str, language: str, provider_name: str, output_path: str) -> int:
    provider = _provider_from_name(provider_name)
    payload = transcribe_file(audio_path=input_path, language=language, provider=provider)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[whisper-run] wrote {output_path}")
    return 0


def validate_command(input_path: str) -> int:
    path = Path(input_path)
    if not path.exists():
        print(f"[whisper-run] file not found: {input_path}", file=sys.stderr)
        return 1
    payload = json.loads(path.read_text(encoding="utf-8"))
    if "language" not in payload or "segments" not in payload:
        print("[whisper-run] invalid payload: missing language or segments", file=sys.stderr)
        return 1
    if not isinstance(payload["segments"], list):
        print("[whisper-run] invalid payload: segments must be list", file=sys.stderr)
        return 1
    print("[whisper-run] validation passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="speech-integration-starter CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    transcribe = sub.add_parser("transcribe", help="Transcribe audio file")
    transcribe.add_argument("--input", required=True, dest="input_path")
    transcribe.add_argument("--lang", required=True, dest="language")
    transcribe.add_argument(
        "--provider",
        default="mock",
        choices=["mock", "faster-whisper"],
        dest="provider_name",
    )
    transcribe.add_argument("--output", required=True, dest="output_path")

    validate = sub.add_parser("validate", help="Validate output JSON")
    validate.add_argument("--input", required=True, dest="input_path")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "transcribe":
        code = transcribe_command(
            input_path=args.input_path,
            language=args.language,
            provider_name=args.provider_name,
            output_path=args.output_path,
        )
        raise SystemExit(code)
    if args.command == "validate":
        code = validate_command(args.input_path)
        raise SystemExit(code)
    raise SystemExit(2)


if __name__ == "__main__":
    main()
