import requests

# 関数名を generate_draft から write_draft に変更します
def write_draft(outline):
    url = "http://127.0.0.1:11434/api/generate"
    
    prompt_text = f"""以下の目次（章立て）をもとに、noteに掲載する本文（Draft）をMarkdown形式で執筆してください。

【目次】
{outline}

【執筆ルール】
- 読者に寄り添う親しみやすくわかりやすいトーン（丁寧語）で書いてください。
- 各章に見出し（# や ##）をつけ、読みやすく段落を分けてください。
"""

    payload = {
        "model": "qwen2.5:32b",
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
        raise Exception(f"Failed to generate draft: {str(e)}")