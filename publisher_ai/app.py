import streamlit as st
from publisher_ai.planning import generate_plan
from publisher_ai.writing import write_draft
from publisher_ai.proofreading import proofread
from publisher_ai.promotion import generate_promotion


def main():
    st.title("Publishing AI Tool")

    theme = st.text_input('Enter the article theme:', '')
    if st.button('Generate Plan'):
        plan_toc = generate_plan(theme)
        st.write(plan_toc)

    toc = st.text_area('Paste the Table of Contents here:')
    if st.button('Write Draft'):
        draft = write_draft(toc)
        st.markdown(draft)

    text_to_proofread = st.text_area('Enter or paste text to proofread:')
    if st.button('Proofread Text'):
        corrected_text = proofread(text_to_proofread)
        st.write(corrected_text)

    article_for_promotion = st.text_area('Paste the completed article here:')
    if st.button('Generate Promotion Texts'):
        promotion_texts = generate_promotion(article_for_promotion)
        st.write(promotion_texts)

if __name__ == '__main__':
    main()
