import requests
from context import ProjectContext

def analyze_market_and_psychology(context: ProjectContext):
    url = "http://127.0.0.1:11434/api/generate"
    
    prompt = f"""{context.get_system_prompt_header()}

あなたは行動心理学に詳しいプロのマーケティングアナリストです。
上記テーマについて、ターゲット読者が「思わず読んで実践したくなる心理的欲求」と「読書時間をデザインするための阻害要因」を分析してください。

【出力フォーマット】
1. ターゲットの潜在的悩み（Pain Points）
2. 購買・行動の心理的ハードル
3. 今回の記事/小説で提示すべき「読書時間デザイン」の解決策
"""
    # Ollamaリクエスト（POST）を実行
    ...