import streamlit as sl

sl.text("Main Page")
sl_slider = sl.sidebar.slider("x")
sl.sidebar.write("Test Slider", sl_slider)

if sl.checkbox("Show text!"):
    sl.sidebar.text("Text shows!")

sl_selectbox = sl.sidebar.selectbox("Select box", [2, 3], 1)

sl.text(sl_selectbox)

left_column, right_column = sl.columns(2)
left_column.text("left column")
with right_column:
    sl.text_input("type text here")
    sl.text_input("type text here now")