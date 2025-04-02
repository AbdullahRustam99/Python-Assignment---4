import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard ")

upload_file = st.file_uploader("Upload a CSV file", type="csv")

if upload_file is not None:
	
	data = pd.read_csv(upload_file)

	st.header("Data Preview: ")
	st.write(data.head())

	st.header("Filter Data: ")
	columns = data.columns.tolist()
	selected_columns = st.multiselect("Select columns to filter", columns)
	if selected_columns:
		filtered_data = data[selected_columns]
		st.write(filtered_data)
	else:
		st.write(data)
	
	st.header("Data Chart: ")
	x_axis = st.selectbox("Select X-axis", columns)
	y_axis = st.selectbox("Select Y-axis", columns)

	if st.button("Plot"):
		st.line_chart(data.set_index(x_axis)[y_axis])





