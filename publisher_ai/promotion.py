import requests

def generate_promotion(text):
    # APIエンドポイント
    url = "http://127.0.0.1:11434/api/generate"
    
    # 広報（Instagram）用プロンプトの構成
    prompt_text = f"""以下の記事をもとに、Instagram投稿用の「キャプション文章」と「カルーセル画像用のスライド構成案」を作成してください。

【対象の記事内容】
{text}

【出力フォーマット】
1. Instagram投稿用キャプション（本文）
   - 読者の目を引くフックのある導入
   - 記事の要点を分かりやすくまとめた本文
   - 適切なハッシュタグ（5〜10個程度）

2. カルーセル画像用テキスト（表紙＋中身4〜5枚分）
   - 各スライドに記載する短くキャッチーなテキスト案
"""

    payload = {
        "model": "qwen2.5:32b",  # お使いのモデル名に指定
        "prompt": prompt_text,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('response')
        else:
            raise Exception(f"Ollama API Error: {response.status_code} - {response.text}")
    except Exception as e:
        raise Exception(f"Failed to generate promotion texts: {str(e)}")