# 【B1研究室】GroundingDINO

CPUだけで動く演習環境です．Windows / Mac（Apple Silicon含む）で同じ手順になります．

## 必要なメモリ

PCのメモリは **8 GiB以上**，Docker Desktop（WindowsではWSL 2を含む）が利用できるメモリは **4 GiB以上** を目安とします．

## 事前準備（当日までに）

1. Docker Desktop をインストール．
2. 次を実行し，メッセージが表示されることを確認する．

   ```
   docker run hello-world
   ```

3. このリポジトリを取得する（`git clone` かZIPのダウンロード）．
4. 重み（`grounding-dino-tiny` フォルダ）を[ダウンロード](https://tokushimauniv-my.sharepoint.com/:f:/g/personal/c612635022_tokushima-u_ac_jp/IgCgky8RLoamTqGNfnRBfMPaATxYNig110UFici0Ru6uBXE?e=4mMYpX)し，リポジトリ直下に`weights/`フォルダを作り，中に置く．次の形になればOK．

   ```
   b1-rinko2026/
   └─ weights/
      └─ grounding-dino-tiny/
         ├─ config.json
         ├─ model.safetensors
         └─ ...
   ```

5. イメージを取得する（注：数GBあります）．

   ```
   docker compose pull
   ```

6. 動作確認をする．

   ```
   docker compose up
   ```

   ブラウザで http://localhost:8888/lab を開き，トークン `lecture` を入力する．
   Launcher の Terminal を開き，次を実行して「読み込み成功」と出ればよい．

   ```
   python src/check.py
   ```

   終了は，`docker compose up` を実行した端末で `Ctrl+C`．

## 当日

```
docker compose up
```

ブラウザで http://localhost:8888/lab を開き，トークン `lecture` を入力する．
演習のノートブックは `notebooks/` に置く．
