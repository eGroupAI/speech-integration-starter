<div align="center">

<img src="./assets/banner.svg" width="100%" alt="speech-integration-starter"/>

<br/>

[![CI](https://img.shields.io/github/actions/workflow/status/eGroupAI/speech-integration-starter/ci.yml?branch=main&style=for-the-badge&label=CI)](../../actions)&nbsp;
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)&nbsp;
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](./LICENSE)&nbsp;
[![Free & Open Source](https://img.shields.io/badge/Free%20%26%20Open%20Source-%E2%9C%93-brightgreen?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

**把 `.wav` 送進去，拿回含 `start` / `end` / `text` 的 JSON 轉寫結果。
Provider 可替換，CPU CI 也能跑完整流程。**

<br/>

[安裝](#安裝) &nbsp;·&nbsp; [執行](#執行) &nbsp;·&nbsp; [輸出格式](#輸出格式) &nbsp;·&nbsp; [換 Provider](#換成自己的推論後端) &nbsp;·&nbsp; [授權](#授權)

</div>

---

## 安裝

```bash
python -m venv .venv
. .venv/bin/activate          # Windows: .venv\Scripts\activate
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

## 輸出格式

```json
{
  "language": "zh",
  "segments": [
    { "start": 0.0, "end": 1.0, "text": "[zh] demo" }
  ]
}
```

---

## Python API

```python
from whisper_starter.pipeline import transcribe_file
from whisper_starter.providers.mock_provider import MockProvider

result = transcribe_file(audio_path="out/demo.wav", language="zh", provider=MockProvider())
print(result)
```

---

## 換成自己的推論後端

`MockProvider` 用於測試，不需要 GPU。換成實際推論後端時，繼承 `WhisperProvider` 協定即可：

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

本專案採 **[MIT License](./LICENSE)** 授權，**永久免費、可商業使用、可修改、可散佈**。

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)](https://opensource.org/licenses/MIT)
[![Free & Open Source](https://img.shields.io/badge/Free%20%26%20Open%20Source-%E2%9C%93-brightgreen?style=flat-square)](https://opensource.org/licenses/MIT)

| 權利 | 說明 |
| --- | --- |
| ✅ 免費使用 | 個人、商業、學術皆可，不收費 |
| ✅ 可修改 | 可依需求自由調整原始碼 |
| ✅ 可散佈 | 可重新散佈原始或修改版本 |
| ✅ 可商業使用 | 可用於商業產品中 |
| ℹ️ 保留聲明 | 散佈時需保留原始版權與授權聲明 |

版權所有 © 2026 [eGroupAI 益群健康資訊](https://www.egroupai.com/zh-TW)

---

## 維護者

本 repo 由 **eGroupAI 益群健康資訊** 維護，作為公司開源貢獻的一部分。

| 項目 | 資訊 |
| --- | --- |
| 官網 | [https://www.egroupai.com/zh-TW](https://www.egroupai.com/zh-TW) |
| 聯絡信箱 | [service@egroupai.com](mailto:service@egroupai.com) |
| GitHub 組織 | [github.com/eGroupAI](https://github.com/eGroupAI) |

如有問題或建議，歡迎透過 [GitHub Issues](../../issues) 或上述信箱與我們聯絡。
