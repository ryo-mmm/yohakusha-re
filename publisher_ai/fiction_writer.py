import requests
from publisher_ai.context import ProjectContext

def write_short_story(context: ProjectContext, insight: str):
    url = "http://127.0.0.1:11434/api/generate"
    
    prompt_text = f"""{context.get_header_prompt()}

あなたは日常の繊細な情緒や五感を描くことに秀でた文芸作家です。
以下のマーケティング分析（読者心理・インサイト）をもとに、「自分だけの読書時間デザイン」をテーマにしたオリジナルの短編小説（1500〜2000文字程度）を執筆してください。

【マーケティングインサイト】
{insight}

【執筆指示】
- 直接的な説教や解説は避け、主人公の日常、光や音・香りの情景描写を通して「自分を取り戻す読書時間」の愛おしさを表現してください。
- 読者が読み終えたあと、静かに自分の本を開きたくなるような余韻（読後感）を残してください。
- タイトルと本文（Markdown形式）を出力してください。
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
        raise Exception(f"Failed to write short story: {str(e)}")