
# VS Codeによる英語と日本語のテキストフォーマット自動化

このプロジェクトは、VS Code内でファイルを開いた状態で、日本語と混在する英語の単語、数字、記号の周りに自動的にスペースを挿入する作業を自動化します。Pythonスクリプト（`eng_space_jpn.py`）がフォーマットを処理し、VS Codeのカスタムタスクによって、このスクリプトをキーボードショートカットで実行できるように設定されています。

---

## 特徴

- **日本語テキスト内の英語フレーズ、数字、記号の周りに自動的にスペースを挿入します**。
- キーボードショートカットでVS Code内でシームレスに動作します。
- **URL、ファイルパス、数式を不要な変更なく維持します**。
- **macOS**と**Windows**の両方に対応しています。
- 日本語の特殊文字（`。、！？「」`）と英語の単語や記号の間にスペースを追加します。
- 日本語と英語の間の句読点、括弧、その他の記号のフォーマットが正しく行われます。

---

## 動作

- **Pythonスクリプト（`eng_space_jpn.py`）**は次の場所に作成されます：
  - macOS: `~/Documents/my_scripts/`
  - Windows: `C:\Users\<Your Username>\Documents\my_scripts\`

- **VS Codeの設定ファイル（`tasks.json`と`keybindings.json`）**は次の場所に設定されます：
  - macOS: `~/Library/Application Support/Code/User/`
  - Windows: `C:\Users\<Your Username>\AppData\Roaming\Code\User\`

---

## 必要条件

- システムにPython 3がインストールされていること。
- システムにVS Codeがインストールされていること。

---

## インストール手順

### 手順1：プロジェクトをクローンまたはダウンロード
このリポジトリをクローンするか、zipファイルとしてダウンロードし、ローカルマシンに解凍します。

### 手順2：セットアップスクリプトを実行
提供されているPythonセットアップスクリプトを実行し、必要なファイルとパスを設定します。

- **macOS**の場合：
  ```bash
  python3 setup.py
  ```

- **Windows**の場合：
  ```bash
  python setup.py
  ```

このスクリプトは次の処理を行います：
- Pythonスクリプト `eng_space_jpn.py` を次の場所に作成します：
  - `~/Documents/my_scripts/`（macOS）
  - `C:\Users\<Your Username>\Documents\my_scripts\`（Windows）
  
- VS Codeの `tasks.json` と `keybindings.json` を次の場所に設定します：
  - `~/Library/Application Support/Code/User/`（macOS）
  - `C:\Users\<Your Username>\AppData\Roaming\Code\User/`（Windows）

### 手順3：VS Codeを再起動
セットアップスクリプトを実行した後、VS Codeを再起動して変更を有効にしてください。

---

## 使い方

1. **VS Codeで日本語と英語が混在するテキストファイルを開きます**。
2. `Ctrl + Shift + T`（Windowsの場合）または `Cmd + Shift + T`（macOSの場合）を押してフォーマットタスクを実行します。
3. スクリプトが開いているファイルを処理し、自動的にテキストをフォーマットします。

---

## フォーマットの動作

### 1. **日本語と英語の間にスペースを追加**
   - 日本語の文字と隣接する英語のテキストや数字の間にスペースを追加します。
   - 例：
     - 入力: `こんにちはJohnさん`
     - 出力: `こんにちは John さん`

### 2. **日本語と英語の記号の間の処理**
   - 日本語の文字と記号（例：`()`, `[]`, `{}`, `+`, `-`, `*`, `#`, `%`, など）の間にスペースを追加します。
   - 例：
     - 入力: `彼は3つのアイテム(+100%増量/#割引)を購入しました。`
     - 出力: `彼は 3 つのアイテム (+100% 増量 /# 割引 ) を購入しました。`

### 3. **日本語の句読点と英語**
   - 日本語の句読点（`、`, `。`, `！`, `？`, `「」` など）と隣接する英語のテキストや記号の間にスペースを追加します。
   - 例：
     - 入力: `それではまた今度！We’ll keep in touch, right?`
     - 出力: `それではまた今度 ！ We’ll keep in touch, right?`

### 4. **URLとファイルパスを保持**
   - URL、ファイルパス、およびフォーマットを変更せずに維持すべきテキストを保持します。
   - 例：
     - 入力: `Please check the path /usr/local/bin and URL https://example.com`
     - 出力: `Please check the path /usr/local/bin and URL https://example.com`

### 5. **括弧と句読点の処理**
   - 日本語の句読点と括弧やカッコの間にスペースを追加します。
   - 例：
     - 入力: `これは。[テスト]です`
     - 出力: `これは 。 [テスト ]です`

### 6. **日本語の引用符の特別処理**
   - 日本語の引用符（`「」`, `『』`, など）と隣接する英語の単語や記号の間にスペースを追加します。
   - 例：
     - 入力: `「さあ行こう！」She is coming soon`
     - 出力: `「さあ行こう！」 She is coming soon`

### 7. **数式の処理**
   - 数式の記号（`+`, `-`, `*`, `/`）と日本語の文字や数字の周りに適切なスペースを維持します。
   - 例：
     - 入力: `数学では(+3 * 2) - 1 = 5 のような計算を学びます。`
     - 出力: `数学では (+3 * 2) - 1 = 5 のような計算を学びます。`

---

## トラブルシューティング

- **キーバインディングの問題**：キーバインディングが機能しない場合は、`keybindings.json` と `tasks.json` ファイルが正しく更新されたか確認してください。
  - macOS: `~/Library/Application Support/Code/User/`
  - Windows: `C:\Users\<Your Username>\AppData\Roaming\Code\User/`

- **Pythonスクリプトの場所**：`eng_space_jpn.py` が `Documents/my_scripts/` フォルダに作成されたことを確認してください：
  - macOS: `~/Documents/my_scripts/`
  - Windows: `C:\Users\<Your Username>\Documents\my_scripts\`

- **Pythonが見つからない**：スクリプトが実行されない場合は、Python 3 がインストールされ、システムのパスで使用可能であることを確認してください。

---

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
