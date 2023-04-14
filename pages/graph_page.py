import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt


# データ分析関連
df = pd.read_csv('./data/data.csv', index_col='日時')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df)
# st.bar_chart(df['設備A'])

# matplotlib
# fig, ax = plt.subplots()
# ax.plot(df.index, df)
# # ax.plot(df.index, df['設備A'])
# ax.set_title('vibration graph')
# st.pyplot(fig)