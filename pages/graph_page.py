import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# サイドバー
st.sidebar.markdown("## 設定項目")
location_selected = st.sidebar.selectbox('監視エリア',('東京','大牟田','千綿'))
facility_selected = st.sidebar.selectbox('監視設備',('pumpA','pumpB','pumpC'))
item_selected = st.sidebar.multiselect('監視項目', ('変位','速度','加速度'))
# st.sidebar.markdown("## Target Variables")
# st.sidebar.plotly_chart(fig_target, use_container_width=True)

# データ分析関連
df = pd.read_csv('./data/data.csv', index_col='日時')
st.subheader('振動値グラフ')
# st.table(df)
st.line_chart(df)
st.subheader('振動値データ')
st.dataframe(df)
# st.bar_chart(df)
# st.bar_chart(df['設備A'])

# matplotlib
# fig, ax = plt.subplots()
# ax.plot(df.index, df)
# # ax.plot(df.index, df['設備A'])
# ax.set_title('vibration graph')
# st.pyplot(fig)