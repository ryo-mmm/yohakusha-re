import requests
from publisher_ai.context import ProjectContext

def analyze_market_and_psychology(context: ProjectContext):
    url = "http://127.0.0.1:11434/api/generate"
    
    prompt_text = f"""{context.get_header_prompt()}

あなたは行動心理学とコンテンツマーケティングに精通したシニアアナリストです。
上記テーマについて、ターゲット読者の心理状態と市場で刺さる切り口（マーケティングインサイト）を深掘り分析してください。

【分析・出力項目】
1. ターゲットが抱える無意識の悩み・阻害要因（Pain Points）
   - なぜ「読書時間」を作れないのか？（時間的・精神的・環境的要因）
2. 読者の行動を促す心理的フック（Triggers）
   - どんな感情やシチュエーション（五感や空間）を提示されると心が動くか？
3. 「読書時間デザイン」としての推奨切り口（Strategic Insight）
   - 記事や小説で提示すべき具体的提案・コンセプト
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
        raise Exception(f"Failed to analyze market: {str(e)}")