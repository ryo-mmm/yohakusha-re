import requests

def proofread(text):
    # APIエンドポイント
    url = "http://127.0.0.1:11434/api/generate"
    
    # 校正用プロンプトの構成
    prompt_text = f"""以下の文章を校正し、誤字脱字の修正、より自然で読みやすい表現への推敲を行ってください。

【対象の文章】
{text}

【出力ルール】
- 校正後の完成文を出力してください。
- 修正点やアドバイスがある場合は、文章の最後に箇条書きで補足してください。
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
        raise Exception(f"Failed to proofread text: {str(e)}")