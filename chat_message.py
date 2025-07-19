#!/usr/bin/env -S python -m streamlit run

import streamlit as st

if 'transactions' not in st.session_state:
    st.session_state.transactions = []

st.header('チャット アプリケーション')

text = st.chat_input()
if text:
    st.session_state.transactions.append(text)
    st.session_state.transactions.append(f'Did you say "{text}"?')

for idx, message in enumerate(st.session_state.transactions):
    if idx % 2 == 0:
        with st.chat_message('user'):
            st.write(message)
    else:
        with st.chat_message('ai'):
            st.write(message)
