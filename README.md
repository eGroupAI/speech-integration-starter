# speech-integration-starter

![Banner](./assets/banner.svg)

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/speech-integration-starter/ci.yml?branch=main&style=for-the-badge)](../../actions)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/eGroupAI/speech-integration-starter?style=for-the-badge)](./LICENSE)

> 把 `.wav` 送進去，拿回含 `start` / `end` / `text` 的 JSON 轉寫結果。
> Provider 可替換，CPU CI 也能跑完整流程。

---

## 安裝

```bash
python -m venv .venv
# macOS / Linux
. .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -e .[dev]
```

---

## 執行

```bash
# 產生示範音檔（合成靜音，不含真實語料）
python scripts/generate_demo_wav.py

# 執行轉寫
whisper-run transcribe --input ./out/demo.wav --lang zh --provider mock --output ./out/demo.json

# 驗證輸出格式
whisper-run validate --input ./out/demo.json
```

---

## 輸出長這樣

```json
{
  "language": "zh",
  "segments": [
    { "start": 0.0, "end": 1.0, "text": "[zh] demo" }
  ]
}
```

---

## 如果你要在 Python 裡用

```python
from whisper_starter.pipeline import transcribe_file
from whisper_starter.providers.mock_provider import MockProvider

result = transcribe_file(audio_path="out/demo.wav", language="zh", provider=MockProvider())
print(result)
```

---

## 換成自己的推論後端

`MockProvider` 用於測試。換成實際推論後端時，繼承 `WhisperProvider` 協定即可：

```python
from whisper_starter.providers.faster_whisper_provider import FasterWhisperProvider

provider = FasterWhisperProvider(model_name="small")
result = transcribe_file(audio_path="audio.wav", language="zh", provider=provider)
```

> `faster-whisper` 需自行安裝：`pip install faster-whisper`

---

## 適合這些情境

- 需要讓轉寫後端可替換，而不是寫死在流程裡
- 想在 CPU CI 跑完整轉寫測試，不依賴 GPU 環境
- 需要一個有測試覆蓋的轉寫輸出基線

---

## 不包含

- 真實語料與客戶詞庫
- 模型選型策略、後處理規則、任何 Prompt 資產

詳見 [`docs/threat-model.md`](./docs/threat-model.md)。

---

## 開發

```bash
pytest -q
```

---

## 授權

MIT License，詳見 [`LICENSE`](./LICENSE)。
