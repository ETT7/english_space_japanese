
# VS Codeによる英語と日本語テキストのフォーマット自動化

このプロジェクトは、VS Codeで開いているファイル内の日本語テキストに混在する英語の単語、数字、記号の周囲にスペースを自動的に追加するプロセスを自動化します。Pythonスクリプト（`eng_space_jpn.py`）がフォーマット処理を行い、VS Code内で簡単なキーボードショートカットを使用してこのスクリプトを実行できるように設定されています。

---

## 特徴

- **日本語テキスト内の英語のフレーズ、数字、記号の周囲に自動的にスペースを追加**します。
- カスタムタスクとキーボードショートカットを介して、VS Code内でシームレスに動作します。
- **URL、ファイルパス、数式をそのまま保持**し、不要な変更を行いません。
- **macOS**および**Windows**の両方に対応しています。
- 日本語の特殊文字（`。、！？「」`）と隣接する英語の単語や記号の周囲にスペースを追加します。
- 括弧やカッコ、その他の特殊記号を含む日本語と英語の間の句読点を正しくフォーマットします。
- **URLやファイルパスはフォーマットの対象外**とし、その構造を破壊しません。

---

## 動作

- **Pythonスクリプト（`eng_space_jpn.py`）**は以下の場所に作成されます：
  - macOSの場合：`~/Documents/my_scripts/`
  - Windowsの場合：`C:\Users\<ユーザー名>\Documents\my_scripts\`

- **VS Codeの設定ファイル（`tasks.json` と `keybindings.json`）**は以下の場所に設定されます：
  - macOSの場合：`~/Library/Application Support/Code/User/`
  - Windowsの場合：`C:\Users\<ユーザー名>\AppData\Roaming\Code\User\`

---

## 必要条件

- Python 3がシステムにインストールされていること。
- VS Codeがシステムにインストールされていること。

---

## インストール

### ステップ 1: プロジェクトをクローンまたはダウンロード
このリポジトリをクローンするか、ZIPファイルとしてダウンロードして、ローカルマシンに解凍します。

### ステップ 2: セットアップスクリプトを実行
提供されているPythonセットアップスクリプトを実行して、必要なファイルとパスを設定します。

- **macOSの場合**：
  ```bash
  python3 setup.py
  ```

- **Windowsの場合**：
  ```bash
  python setup.py
  ```

このスクリプトは以下を行います：
- Pythonスクリプト `eng_space_jpn.py` を以下に作成します：
  - `~/Documents/my_scripts/`（macOS）
  - `C:\Users\<ユーザー名>\Documents\my_scripts\`（Windows）
  
- VS Codeの `tasks.json` と `keybindings.json` を以下に設定します：
  - `~/Library/Application Support/Code/User/`（macOS）
  - `C:\Users\<ユーザー名>\AppData\Roaming\Code\User/`（Windows）

### ステップ 3: VS Codeを再起動
セットアップスクリプトを実行した後、VS Codeを再起動して変更を有効にします。

---

## 使用方法

1. **VS Codeで日本語と英語が混在するファイルを開きます**。
2. Windowsの場合は `Ctrl + Shift + T`、macOSの場合は `Cmd + Shift + T` を押してフォーマットタスクを実行します。
3. スクリプトが開いているファイルを処理し、テキストを自動的にフォーマットします。

---

## フォーマットの挙動

### 1. **日本語の文字と英語の単語の間にスペースを追加**
   - 日本語の文字と隣接する英語のテキストや数字の間にスペースを追加します。
   - 例：
     - 入力：`こんにちはJohnさん`
     - 出力：`こんにちは John さん`

### 2. **日本語と英語の間の記号の処理**
   - 日本語の文字と記号（例：`()`, `[]`, `{}`, `+`, `-`, `*`, `#`, `%`など）の間にスペースを追加します。
   - 例：
     - 入力：`彼は3つのアイテム(+100%増量/#割引)を購入しました。`
     - 出力：`彼は 3 つのアイテム (+100% 増量 /# 割引 ) を購入しました。`

### 3. **日本語の句読点と英語の間**
   - 日本語の句読点（`、`, `。`, `！`, `？`, `「」`など）と隣接する英語のテキストや記号の間にスペースを追加します。
   - 例：
     - 入力：`それではまた今度！We’ll keep in touch, right?`
     - 出力：`それではまた今度 ！ We’ll keep in touch, right?`

### 4. **URLとファイルパスの保持**
   - URL、ファイルパス、およびフォーマットすべきではないテキストを検出して保持します。
   - 例：
     - 入力：`Please check the path /usr/local/bin and URL https://example.com`
     - 出力：`Please check the path /usr/local/bin and URL https://example.com`

### 5. **括弧と句読点の処理**
   - 括弧やカッコの**外側**にのみスペースを追加し、内部のスペースは変更しません。
   - 例：
     - **入力**：`これは。[テスト]です`
     - **出力**：`これは。[テスト] です`

### 6. **日本語の引用符の特別な処理**
   - 日本語の引用符（`「」`, `『』`など）と隣接する英語の単語や記号の間にスペースを追加します。
   - 例：
     - 入力：`「さあ行こう！」She is coming soon`
     - 出力：`「さあ行こう！」 She is coming soon`

### 7. **数式**
   - 数式の記号（`+`, `-`, `*`, `/`）と日本語の文字や数字の間に適切なスペースを維持します。
   - 例：
     - 入力：`数学では(+3 * 2) - 1 = 5 のような計算を学びます。`
     - 出力：`数学では (+3 * 2) - 1 = 5 のような計算を学びます。`

### 8. **行末のスペース削除**
   - 行末の不要なスペースを削除します。
   - 例：
     - 入力：`これはテストです。     `
     - 出力：`これはテストです。`

---

## トラブルシューティング

- **キーバインディングの問題**：キーバインディングが機能しない場合は、`keybindings.json` と `tasks.json` が正しく更新されているか確認してください。
  - macOS: `~/Library/Application Support/Code/User/`
  - Windows: `C:\Users\<ユーザー名>\AppData\Roaming\Code\User/`

- **Pythonスクリプトの場所**：スクリプト `eng_space_jpn.py` が `Documents/my_scripts/` フォルダに作成されていることを確認してください：
  - macOS: `~/Documents/my_scripts/`
  - Windows: `C:\Users\<ユーザー名>\Documents\my_scripts\`

- **Pythonが見つからない**：スクリプトが実行されない場合は、Python 3がインストールされており、システムのパスに設定されていることを確認してください。

---

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。
