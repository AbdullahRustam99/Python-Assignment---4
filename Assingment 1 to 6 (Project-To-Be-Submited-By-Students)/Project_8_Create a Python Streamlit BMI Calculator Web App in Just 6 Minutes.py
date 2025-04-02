import streamlit as st

st.title("BMI Calculator")
st.header("Calculate your Body Mass Index (BMI)")
st.write("Enter your weight in kilograms and height in meters to calculate your BMI.")

weight = st.number_input("Weight (kg)")
height = st.number_input("Height (feet)")
convert_heigh = height * 3.048
bmi = 0.0
if st.button("Calculate BMI"):
	if weight > 0 and convert_heigh > 0:
		bmi += weight / (convert_heigh ** 2)
		st.success(f"Your BMI is: {bmi:.2f}")
	else:
		st.error("Please enter valid weight and height values.")

st.header("BMI Result:")
if bmi > 0:
	if bmi <= 18.5:
		st.markdown("<h1 class=yellow>Underweight<h1/>", unsafe_allow_html=True)
	elif  bmi <= 25:
		st.markdown("<h1 class=green>Normal weight<h1/>", unsafe_allow_html=True)
	elif bmi <= 30:
		st.markdown("<h1 class=orange>Overweight<h1/>", unsafe_allow_html=True)
	else :
		st.markdown("<h1 class=red>Obesity<h1/>", unsafe_allow_html=True)
	

st.markdown("""<style >
	    .red {
	        background-color: #f71735;
	        font-size: 40px;
	        font-weight: bold;
	    	border-radius: 5px;
	    	text-align: center;
	    }
	    .green {
	        background-color: #036d19;
	        font-size: 40px;
	        font-weight: bold;
	    	border-radius: 5px;
	    	text-align: center;
	    }
	    .yellow {
	        background-color: #ffc914;
	        font-size: 40px;
	        font-weight: bold;
	    	border-radius: 5px;
	    	text-align: center;
	    	color: black;
	    }
	    .orange {
	        background-color: #FD5200;
	        font-size: 40px;
	        font-weight: bold;
	    	border-radius: 5px;
	    	text-align: center;
	    }
	    #bmi-calculator{
	        padding: 20px;
	        border-radius: 10px;
	        box-shadow: 0px 0px 10px red;
	    	text-align: center;
	    	margin-bottom: 20px;
	    }   
<style/>""",unsafe_allow_html=True)



