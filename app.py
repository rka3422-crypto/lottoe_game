import streamlit as st
from lotto_utils import *

st.title('🎱로또 번호 생성기')
n = st.number_input('몇 게임 할까요?', min_value=1, max_value=10, value=5)
if st.button('번호 뽑기'):
    games = make_games(n)
    lines = []
    for i in range(n):
        lines.append(f'게임 {i + 1:2d} : {to_text(games[i])}')
    st.code('\n'.join(lines), language=None)