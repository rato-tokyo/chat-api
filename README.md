# Chat API

Vercelのv0で作成したサイトからChatGPTとチャットできるAPIサーバーです。

## 機能

- チャットメッセージの送受信
- ChatGPTとの対話
- メッセージ履歴の保存と取得

## API仕様

### エンドポイント

1. メッセージの送信
   - URL: `https://chat-api-m4h2.onrender.com/chat`
   - メソッド: POST
   - リクエストボディ:
     ```json
     {
       "content": "メッセージ内容",
       "role": "user"
     }
     ```
   - レスポンス:
     ```json
     {
       "content": "AIからの応答",
       "role": "assistant"
     }
     ```

2. メッセージ履歴の取得
   - URL: `https://chat-api-m4h2.onrender.com/messages`
   - メソッド: GET
   - レスポンス:
     ```json
     [
       {
         "content": "ユーザーのメッセージ",
         "role": "user"
       },
       {
         "content": "AIからの応答",
         "role": "assistant"
       }
     ]
     ```

### データ形式

- メッセージはJSONファイルに保存されます
- 各メッセージは以下の形式で保存:
  - `content`: メッセージの内容（文字列）
  - `role`: 送信者の役割（"user" または "assistant"）

## バックエンド（Render）のセットアップ

1. このリポジトリをフォークまたはクローン
2. Renderで新しいWebサービスを作成
   - GitHubリポジトリと連携
   - 環境変数の設定:
     - `OPENAI_API_KEY`: OpenAIのAPIキー
3. デプロイが完了したら、表示されるURLをメモ（例: `https://chat-api-xxxx.onrender.com`）

## テスト方法

1. バックエンドのテスト:
```bash
# テストスクリプトの実行
python test_api.py
```

2. APIの動作確認:
- メッセージの送信:
  ```bash
  curl -X POST https://chat-api-m4h2.onrender.com/chat \
    -H "Content-Type: application/json" \
    -d '{"content": "こんにちは", "role": "user"}'
  ```
- メッセージ履歴の取得:
  ```bash
  curl https://chat-api-m4h2.onrender.com/messages
  ```

## 注意事項

- 本番環境では、CORSの設定を適切なオリジンに制限してください
- APIキーは必ず環境変数として管理してください