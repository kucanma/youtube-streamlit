# from matplotlib.pyplot import text
import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image # 画像の表示
import time

# タイトルの表示
st.title('Streamlit 超入門')


# プログレスバーの表示
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text =  st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'あなたのコンディション：', condition

# text_area　は　複数行

# # セレクトボックス
# option = st.selectbox(
#     '好きな数字をいれてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', option, 'です。'

# チェックボックス
# if st.checkbox('Show Image'):
#     # 画像の表示
#     img = Image.open('image1.png')
#     st.image(img, caption='image', use_column_width=True)
#     # レイアウトの横幅にあわせて表示　use_column_width=True

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.dataframe(df.style.highlight_max(axis=0), width=1000, height=400)
# axis=0 --> 列　axis=1 --> 行

# st.table(df.style.highlight_max(axis=0))
# 静的な表を作成

# マークダウン記法でかける　コードはバッククオーテーションで記載

"""
# title1
## title2
### title3

```python
import streamlit as st
import numpy as np
```

"""
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df2 = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.60, 138.70],
#     columns=['lat', 'lon']
# )
# st.map(df2)