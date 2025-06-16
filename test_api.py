import requests
import json
import sys
from typing import List, Dict

API_URL = "https://chat-api-m4h2.onrender.com"

def get_messages() -> List[Dict]:
    """メッセージ履歴を取得"""
    response = requests.get(f"{API_URL}/messages")
    response.raise_for_status()
    return response.json()

def send_message(message: str) -> Dict:
    """メッセージを送信"""
    response = requests.post(
        f"{API_URL}/chat",
        json={"content": message, "role": "user"}
    )
    response.raise_for_status()
    return response.json()

def print_messages(messages: List[Dict]):
    """メッセージを整形して表示"""
    for msg in messages:
        role = "👤" if msg["role"] == "user" else "🤖"
        print(f"{role} {msg['content']}")
    print()

def main():
    # メッセージ履歴の表示
    print("=== メッセージ履歴 ===")
    messages = get_messages()
    print_messages(messages)

    # 対話モード
    print("=== チャット開始 ===")
    print("終了するには 'quit' または 'exit' と入力してください")
    
    while True:
        try:
            user_input = input("👤 ").strip()
            if user_input.lower() in ["quit", "exit"]:
                break
            
            # メッセージを送信
            response = send_message(user_input)
            print(f"🤖 {response['content']}")
            print()
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            break

if __name__ == "__main__":
    main() 