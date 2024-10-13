import streamlit as st
import pandas as pd
import random
import re

# 漢字を抽出する関数
def extract_kanji(text):
    return re.findall(r'[一-龯々]', text)

# アプリのメイン関数
def main():
    st.title("漢字読みクイズアプリ")

    # CSVデータを読み込む
    if 'data' not in st.session_state:
        data = pd.read_csv('kanji_data.csv')
        st.session_state.data = data
        st.session_state.current_phrase = None
        st.session_state.current_kanji = None
        st.session_state.total_questions = 0

    # 新しい問題を選択する関数
    def new_question():
        phrase = random.choice(st.session_state.data['フレーズ'].tolist())
        kanji_list = extract_kanji(phrase)
        if kanji_list:
            kanji = random.choice(kanji_list)
            st.session_state.current_phrase = phrase
            st.session_state.current_kanji = kanji
        else:
            new_question()

    # 初回または「次の問題」ボタンが押されたときに新しい問題を選択
    if st.session_state.current_phrase is None or st.button('次の問題'):
        new_question()
        st.session_state.total_questions += 1

    # 問題を表示
    st.header(f"フレーズ: {st.session_state.current_phrase}")
    st.subheader(f"この中の「{st.session_state.current_kanji}」の読みは？")

    # 解答欄（オプション）
    st.text_input("読みをひらがなで入力してください（任意）:")

    # 総問題数を表示
    st.sidebar.header("統計")
    st.sidebar.write(f"総問題数: {st.session_state.total_questions}")

    # リセットボタン
    if st.sidebar.button("リセット"):
        st.session_state.total_questions = 0
        st.session_state.current_phrase = None
        st.session_state.current_kanji = None

if __name__ == "__main__":
    main()
