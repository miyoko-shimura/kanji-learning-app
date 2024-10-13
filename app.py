import streamlit as st
import pandas as pd
import random

def load_data():
    return pd.read_csv('kanji_data.csv')

def get_new_question(data):
    return random.choice(data['フレーズ'].tolist())

def main():
    st.title("フレーズ読みクイズアプリ")

    # 初期化
    if 'data' not in st.session_state:
        st.session_state.data = load_data()
    if 'current_phrase' not in st.session_state:
        st.session_state.current_phrase = get_new_question(st.session_state.data)
    if 'question_count' not in st.session_state:
        st.session_state.question_count = 0
    if 'correct_count' not in st.session_state:
        st.session_state.correct_count = 0
    if 'incorrect_count' not in st.session_state:
        st.session_state.incorrect_count = 0

    # 30問終了後のメッセージ
    if st.session_state.question_count >= 30:
        st.success("30問完了しました！おつかれさまでした。")
        if st.button("最初からやり直す"):
            st.session_state.current_phrase = get_new_question(st.session_state.data)
            st.session_state.question_count = 0
            st.session_state.correct_count = 0
            st.session_state.incorrect_count = 0
    else:
        # 問題を表示
        st.header(f"フレーズ: {st.session_state.current_phrase}")
        st.subheader("このフレーズの読み方は？")

        # 自己採点ボタン
        col1, col2 = st.columns(2)
        
        def update_state(is_correct):
            if is_correct:
                st.session_state.correct_count += 1
            else:
                st.session_state.incorrect_count += 1
            st.session_state.question_count += 1
            st.session_state.current_phrase = get_new_question(st.session_state.data)

        with col1:
            if st.button("正解"):
                update_state(True)
        with col2:
            if st.button("不正解"):
                update_state(False)

    # 統計を表示
    st.sidebar.header("統計")
    st.sidebar.write(f"問題数: {st.session_state.question_count}/30")
    st.sidebar.write(f"正解数: {st.session_state.correct_count}")
    st.sidebar.write(f"不正解数: {st.session_state.incorrect_count}")

if __name__ == "__main__":
    main()
