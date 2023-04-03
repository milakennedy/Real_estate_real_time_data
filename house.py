import streamlit as st
import pickle
import numpy as np
import sklearn
def set_css():
    """
    Function to set the CSS style of the app.
    """
    st.markdown("""
    <style>
    .stApp {
        background-color: #c9ffee;
    }
    .stButton button {
        background-color: #295953;
        color: #fff;
    }
    </style>
    """, unsafe_allow_html=True)
def main():
	model = pickle.load(open('3PIN.pkl', 'rb'))
	st.title("House Price Predictor")
	BHK_dict = {"1 BHK": 0, "10 BHK":1 , "2 BHK": 2,"3 BHK":3,"4 BHK":4,"5 BHK":5,"6 BHK":6,"7 BHK":7,"8 BHK":8,"9 BHK":9,"Land":10,"Office":11}
	RS_dict = {"Rent": 0, "Sale":1}
	area_dict = {"Adyar": 0, "Alwarpet":1 , "Anna Nagar": 2,"Anna Nagar, Anna Nagar East":3,"Anna Nagar, Anna Nagar West":4,"Anna Nagar, Shanti colony":5,"Ashok Nagar":6,"Besant Nagar":7,"Chetpet":8,"ECR":9,"Egmore":10,"Ekkatuthangal":11,"Gopalapuram":12,"Kilpauk":13,"Kodambakkam":14,"Kolathur":15,"Korattur":16,"Kottivakkam":17,"Kotturpuram":18,"Mylapore":19,"Neelankarai":20,"Nungambakkam":21,"OMR":22,"Porur":23,"RA Puram":24,"Royapettah":25,"Saligramam":26,"Sholinganallur":27,"T Nagar":28,"Thiruvanmiyur":29,"Velachery":30,"Virugambakkam":31,"other":32}
	source_dict = {"Magic Bricks": 0, "99 acres":1}
	type_dict = {"Appartment": 0, "Office":1,"House":2,"Showroom":3,"Plot":4,"Shop":5,"Land":6}
	property_dict = {"Residential": 0, "Commercial":1,"Independent":2}
	# Define options for the drop-down list
	property_options = ["Residential", "Commercial", "Independent"]

	# Create a drop-down list for user input
	property_input = st.selectbox("Select the property", property_options)

	# Define options for the drop-down list
	type_options = ["Appartment", "Office", "House","Showroom","Plot","Shop","Land"]

	# Create a drop-down list for user input
	type_input = st.selectbox("Select the type", type_options)

	BHK_options = ["1 BHK", "10 BHK", "2 BHK","3 BHK","4 BHK","5 BHK","6 BHK","7 BHK","8 BHK","9 BHK","Land","Office"]

	# Create a drop-down list for user input
	BHK_input = st.selectbox("Select the type", BHK_options)

	rentsale_options = ["Rent", "Sale"]

	# Create a drop-down list for user input
	rentsale_input = st.selectbox("Select Rental or Sale", rentsale_options)

	area_options = ["Adyar","Alwarpet", "Anna Nagar","Anna Nagar, Anna Nagar East","Anna Nagar, Anna Nagar West","Anna Nagar, Shanti colony","Ashok Nagar","Besant Nagar","Chetpet","ECR","Egmore","Ekkatuthangal","Gopalapuram","Kilpauk","Kodambakkam","Kolathur","Korattur","Kottivakkam","Kotturpuram","Mylapore","Neelankarai","Nungambakkam","OMR","Porur","RA Puram","Royapettah","Saligramam","Sholinganallur","T Nagar","Thiruvanmiyur","Velachery","Virugambakkam","other"]

	# Create a drop-down list for user input
	area_input = st.selectbox("Select the area", area_options)

	Source_options = ["Magic Bricks", "99 acres"]

	# Create a drop-down list for user input
	Source_input = st.selectbox("Select the Source", Source_options)

	DaysonMkt_input = st.text_input("Enter the DaysonMkt:")
	# Display the user input


	

	if st.button("Submit"):
		#property
		for key,value in property_dict.items():
			if str(key) == str(property_input):
				property_input=int(value)

		#type
		for key,value in type_dict.items():
			if str(key) == str(type_input):
				type_input=int(value)

		#BHK
		for key,value in BHK_dict.items():
			if str(key) == str(BHK_input):
				BHK_input=int(value)

		#RentSale
		for key,value in RS_dict.items():
			if str(key) == str(rentsale_input):
				rentsale_input=int(value)

		#area
		for key,value in area_dict.items():
			if str(key) == str(area_input):
				area_input=int(value)

		#Source
		for key,value in source_dict.items():
			if str(key) == str(Source_input):
				Source_input=int(value)

		#prediction
		prediction=model.predict([[property_input,type_input,rentsale_input,BHK_input,area_input,Source_input,DaysonMkt_input]])
		output=round(prediction[0],2)
		st.success("The price of the house is"+" ₹"+str(output)) 


if __name__ == '__main__':
	set_css()
	main()
