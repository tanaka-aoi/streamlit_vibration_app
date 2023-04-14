import streamlit as st
from PIL import Image

# 基本
st.title('vibration monitoring app')
st.caption('設備振動値監視中')

# 画像
image = Image.open('./data/conan.png')
st.image(image, width=200)