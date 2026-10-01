import requests

def generate_plan(theme):
    # APIエンドポイントのURL（/api/generate が正しいパスです）
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": "qwen2.5:32b",  # お手元の環境で用意されているモデル名を指定（例: qwen2.5:32b, qwen2.5:14b など）
        "prompt": f"テーマ「{theme}」について、note記事の企画案と目次（章立て）を作成してください。",
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('response')
        else:
            raise Exception(f"Ollama API エラー: {response.status_code}")
    except Exception as e:
        raise Exception(f"Failed to generate plan: {str(e)}")