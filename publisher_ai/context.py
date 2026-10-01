# publisher_ai/context.py

class ProjectContext:
    def __init__(self, theme_topic: str):
        self.team_theme = "自分だけの”読書時間デザイン”を作る"
        self.theme_topic = theme_topic
        
        # ターゲット層と人間心理（ペルソナ）の定義
        self.target_persona = {
            "target": "多忙で自分の時間が取れず、精神的ゆとりを求めている社会人",
            "psychology": "「読書したいが時間がない」という焦りと、「自分を取り戻す整い時間」への憧れ",
            "triggers": "日常の小さなスキマ時間の再発見、五感（香り、音、空間）を通じた読書体験の肯定"
        }

    def get_header_prompt(self) -> str:
        return f"""
【出版社AIチーム共有コンセプト】: {self.team_theme}
【今回のテーマ】: {self.theme_topic}
【ターゲットと読者心理】:
- 対象読者: {self.target_persona['target']}
- 読者感情: {self.target_persona['psychology']}
- 心理的フック: {self.target_persona['triggers']}

※上記の世界観・ターゲット心理から逸脱せず、プロフェッショナルとしての専門性を持って出力してください。
"""