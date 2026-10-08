import torch
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

path = "/weights/grounding-dino-tiny"
processor = AutoProcessor.from_pretrained(path)
model = AutoModelForZeroShotObjectDetection.from_pretrained(path)
print("torch", torch.__version__, "| 読み込み成功")
