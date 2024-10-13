import streamlit as st
import pandas as pd
import random

def main():
    st.title("フレーズ読みクイズアプリ")

    # CSVデータを読み込む
    if 'data' not in st.session_state:
        data = pd.read_csv('kanji_data.csv')
        st.session_state.data = data
        st.session_state.current_phrase = None
        st.session_state.question_count = 0
        st.session_state.correct_count = 0
        st.session_state.incorrect_count = 0

    # 新しい問題を選択する関数
    def new_question():
        return random.choice(st.session_state.data['フレーズ'].tolist())

    # 初回または「次の問題」ボタンが押されたときに新しい問題を選択
    if st.session_state.current_phrase is None or st.button('次の問題'):
        st.session_state.current_phrase = new_question()
        st.session_state.question_count += 1

    # 問題を表示
    st.header(f"フレーズ: {st.session_state.current_phrase}")
    st.subheader("このフレーズの読み方は？")

    # 自己採点ボタン
    col1, col2 = st.columns(2)
    with col1:
        if st.button("正解"):
            st.session_state.correct_count += 1
            st.session_state.current_phrase = new_question()
            st.session_state.question_count += 1
    with col2:
        if st.button("不正解"):
            st.session_state.incorrect_count += 1
            st.session_state.current_phrase = new_question()
            st.session_state.question_count += 1

    # 統計を表示
    st.sidebar.header("統計")
    st.sidebar.write(f"問題数: {st.session_state.question_count}/30")
    st.sidebar.write(f"正解数: {st.session_state.correct_count}")
    st.sidebar.write(f"不正解数: {st.session_state.incorrect_count}")

    # 30問終了後のメッセージ
    if st.session_state.question_count >= 30:
        st.success("30問完了しました！おつかれさまでした。")
        if st.button("最初からやり直す"):
            st.session_state.current_phrase = None
            st.session_state.question_count = 0
            st.session_state.correct_count = 0
            st.session_state.incorrect_count = 0
            st.experimental_rerun()

if __name__ == "__main__":
    main()
