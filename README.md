# Chat API

Vercelのv0で作成したサイトからChatGPTとチャットできるAPIサーバーです。

## 機能

- チャットメッセージの送受信
- ChatGPTとの対話
- メッセージ履歴の保存と取得

## セットアップ

1. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

2. OpenAI APIキーの設定:
`main.py`の`api_key`を実際のAPIキーに置き換えてください。

3. サーバーの起動:
```bash
python main.py
```

## Vercel v0での使用方法

v0プロジェクトで以下のようなJavaScriptコードを使用してAPIと通信できます：

```javascript
// メッセージの送信
async function sendMessage(message) {
  const response = await fetch('https://your-render-url/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      content: message,
      role: 'user'
    })
  });
  return await response.json();
}

// メッセージ履歴の取得
async function getMessages() {
  const response = await fetch('https://your-render-url/messages');
  return await response.json();
}
```

## デプロイ

このAPIはRenderでデプロイすることを想定しています。GitHubリポジトリと連携することで自動的にデプロイされます。

## 注意事項

- 本番環境では、CORSの設定を適切なオリジンに制限してください
- APIキーは環境変数として管理することを推奨します
- メッセージの保存にはJSONファイルを使用していますが、本番環境ではデータベースの使用を検討してください