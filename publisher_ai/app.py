import streamlit as st
from publisher_ai.context import ProjectContext
from publisher_ai.market import analyze_market_and_psychology
from publisher_ai.fiction_writer import write_short_story
from publisher_ai.planning import generate_plan
from publisher_ai.writing import write_draft
from publisher_ai.proofreading import proofread
from publisher_ai.promotion import generate_promotion


def main():
    st.title("Publishing AI Tool")
    st.caption("チームテーマ：「自分だけの”読書時間デザイン”を作る」")

    # セッション状態で ProjectContext および中間生成物を管理
    if "context" not in st.session_state:
        st.session_state.context = None

    theme = st.text_input('記事・作品のテーマを入力してください:', '多忙な日常に自分を取り戻す「15分の夜読書」')

    if theme:
        st.session_state.context = ProjectContext(theme_topic=theme)

    # 機能ごとにタブで分割
    tab1, tab2, tab3, tab4 = st.tabs(["1. マーケティング & 小説", "2. 企画 & 下書き", "3. 校正", "4. 広報"])

    # Tab 1: マーケティング分析 & 短編小説
    with tab1:
        st.header("マーケティング分析 & オリジナル短編小説")
        
        if st.button("マーケティング・読者心理を分析する"):
            with st.spinner("心理分析中..."):
                analysis_result = analyze_market_and_psychology(st.session_state.context)
                st.session_state.insight = analysis_result
                st.write(analysis_result)

        insight_input = st.text_area('分析結果・インサイト（小説執筆のインプット）:', value=st.session_state.get('insight', ''))
        
        if st.button("短編小説を執筆する"):
            if insight_input:
                with st.spinner("小説執筆中..."):
                    story = write_short_story(st.session_state.context, insight_input)
                    st.markdown(story)
            else:
                st.warning("マーケティング分析結果を入力または生成してください。")

    # Tab 2: 企画 & 下書き
    with tab2:
        st.header("note記事 企画 & 執筆")
        if st.button("企画案・目次を生成"):
            with st.spinner("企画生成中..."):
                plan_toc = generate_plan(st.session_state.context)
                st.write(plan_toc)

        toc = st.text_area('目次（章立て）を入力:')
        if st.button("下書き本文を執筆"):
            if toc:
                with st.spinner("本文執筆中..."):
                    draft = write_draft(st.session_state.context, toc)
                    st.markdown(draft)
            else:
                st.warning("目次を入力してください。")

    # Tab 3: 校正
    with tab3:
        st.header("文章校正・推敲")
        text_to_proofread = st.text_area('校正対象の文章を入力:')
        if st.button("校正を実行"):
            if text_to_proofread:
                with st.spinner("校正中..."):
                    corrected_text = proofread(st.session_state.context, text_to_proofread)
                    st.write(corrected_text)
            else:
                st.warning("文章を入力してください。")

    # Tab 4: 広報
    with tab4:
        st.header("広報・SNS文章作成")
        article_for_promotion = st.text_area('完成した記事/作品テキストを入力:')
        if st.button("Instagram広報文を生成"):
            if article_for_promotion:
                with st.spinner("広報文作成中..."):
                    promotion_texts = generate_promotion(st.session_state.context, article_for_promotion)
                    st.write(promotion_texts)
            else:
                st.warning("記事テキストを入力してください。")


if __name__ == '__main__':
    main()