import os
from pathlib import Path

import torch
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

path = Path(os.environ.get("WEIGHTS_DIR", "/weights")) / "grounding-dino-tiny"

required_files = ["config.json", "preprocessor_config.json"]
missing_files = [name for name in required_files if not (path / name).is_file()]
has_weights = any((path / name).is_file() for name in ("model.safetensors", "pytorch_model.bin"))
has_tokenizer = any((path / name).is_file() for name in ("tokenizer.json", "vocab.txt"))

if not path.is_dir() or missing_files or not has_weights or not has_tokenizer:
    details = []
    if missing_files:
        details.append("不足ファイル: " + ", ".join(missing_files))
    if not has_weights:
        details.append("重みファイルが必要です: model.safetensors または pytorch_model.bin")
    if not has_tokenizer:
        details.append("トークナイザーが必要です: tokenizer.json または vocab.txt")

    detail_text = "\n".join(details)
    raise SystemExit(
        "Grounding DINO Tinyの重みを読み込めません。\n"
        f"確認先: {path}\n"
        "ホスト側の weights/grounding-dino-tiny/ にモデル一式を配置してください。\n"
        f"{detail_text}\n"
        "詳しくはREADMEの「事前準備（当日までに）」を参照してください。"
    )

processor = AutoProcessor.from_pretrained(path)
model = AutoModelForZeroShotObjectDetection.from_pretrained(path)
print("torch", torch.__version__, "| 読み込み成功")
