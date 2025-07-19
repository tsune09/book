#!/usr/bin/env -S python -m streamlit run

import streamlit as st

st.header('チャット アプリケーション')

with st.container(height=200):
    chat_field = st.chat_input(placeholder='チャットメッセージはこちらに')

if chat_field:
    st.markdown(f'あなたのメッセージ: {chat_field}')
