# speech-integration-starter

![Banner](./assets/banner.svg)

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/speech-integration-starter/ci.yml?branch=main&style=for-the-badge)](../../actions)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![License](https://img.shields.io/github/license/eGroupAI/speech-integration-starter?style=for-the-badge)](./LICENSE)
[![ASR Starter](https://img.shields.io/badge/ASR-Starter%20Kit-0F766E?style=for-the-badge)](#)

> 一個專注在「快速接 Whisper」的開源 starter kit。  
> **有工程骨架，沒有商業邏輯。**

---

## 專案定位

這個 repo 提供：

- Whisper 整合介面的標準化封裝
- 可切換 provider 的 adapter pattern
- 可在 CPU-only CI 跑通的 mock pipeline
- 結果輸出 JSON schema 與最小 smoke test

## 公開說明（安全版）

本專案僅提供通用元件說明，不提供實際內部架構圖與流程圖。

## 討論度來源

- **開箱即用**：一行指令就能跑轉寫輸出
- **可測試**：Mock provider 讓 CI 不綁定 GPU
- **可替換**：Provider 介面獨立，方便接不同推論引擎
- **可治理**：清楚標註不開源範圍，避免誤解

---

## 快速開始

### 1) 安裝

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

### 2) 產生示範音檔（合成）

```bash
python scripts/generate_demo_wav.py
```

### 3) 用 mock provider 跑轉寫

```bash
whisper-run transcribe --input ./out/demo.wav --lang zh --provider mock --output ./out/demo.json
```

### 4) 驗證輸出

```bash
whisper-run validate --input ./out/demo.json
```

---

## CLI 指令

```bash
whisper-run transcribe --input <WAV> --lang <LANG> --provider <mock|faster-whisper> --output <JSON>
whisper-run validate --input <JSON>
```

## Python API

```python
from whisper_starter.pipeline import transcribe_file
from whisper_starter.providers.mock_provider import MockProvider

result = transcribe_file(
    audio_path="out/demo.wav",
    language="zh",
    provider=MockProvider(),
)
print(result)
```

---

## 輸出格式

```json
{
  "language": "zh",
  "segments": [
    { "start": 0.0, "end": 1.2, "text": "..." }
  ]
}
```

---

## 安全邊界（重要）

本 repo **不包含**：

- Prompt、模板、few-shot、私有校正規則
- 生產模型路由、品質評分與決策策略
- 客戶詞庫、真實語料、內部服務流程

詳見 `docs/threat-model.md`。

---

## 開發與測試

```bash
pytest -q
```

---

## Roadmap

- [x] v0.1.0：Adapter + Mock + CLI + CI
- [ ] v0.2.0：Provider benchmark harness
- [ ] v0.3.0：Streaming transcription example

---

## 公開後討論引導（Launch Playbook）

建議公開時同步引導社群互動：

- 發起 `ASR accuracy vs speed` benchmark challenge
- 提供 `Bring your own provider` 範例徵稿
- 開啟 GitHub Discussions：`Use Cases / Integrations / Benchmarks`
- 在 README 新增「本週最佳社群案例」區塊

---

## 社群熱度飛輪（Hot Loop）

公開後前四週，建議每週固定執行：

1. 發起 benchmark challenge（速度 vs 品質）
2. 精選 1 個社群整合案例放進 README
3. 每週固定回覆與彙整 FAQ（累積 SEO）
4. 持續釋出小版本（保持專案活躍訊號）

完整貼文稿可直接用 `docs/social-launch-kit-zh-TW.md`。

---

## 授權

MIT License，詳見 `LICENSE`。
