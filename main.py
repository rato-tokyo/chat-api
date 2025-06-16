from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from typing import List, Dict
import os
from openai import OpenAI

app = FastAPI()

# OpenAI APIキーの設定
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では適切なオリジンを指定してください
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# メッセージのモデル定義
class Message(BaseModel):
    content: str
    role: str

# メッセージの保存先
MESSAGES_FILE = "messages.json"

# メッセージの初期化
if not os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "w") as f:
        json.dump([], f)

@app.post("/chat")
async def chat(message: Message):
    try:
        # 既存のメッセージを読み込む
        with open(MESSAGES_FILE, "r") as f:
            messages = json.load(f)
        
        # 新しいメッセージを追加
        messages.append({"content": message.content, "role": message.role})
        
        # ChatGPTからの応答を取得
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages]
        )
        
        ai_response = {
            "content": response.choices[0].message.content,
            "role": "assistant"
        }
        messages.append(ai_response)
        
        # メッセージを保存
        with open(MESSAGES_FILE, "w") as f:
            json.dump(messages, f)
        
        return ai_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/messages")
async def get_messages():
    try:
        with open(MESSAGES_FILE, "r") as f:
            messages = json.load(f)
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 