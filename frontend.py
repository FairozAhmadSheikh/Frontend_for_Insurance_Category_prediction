import streamlit as st
import requests


API_URL='http://51.21.252.70:8000/predict'

st.title("Application for Insurance Category Prediction ")
st.markdown("Enter Details Below ")

age=st.number_input('Age',min_value=1,max_value=120,value=30)
weight=st.number_input('Weight  (Kgs)',min_value=1.0,value=65.0)
height=st.number_input('Height  (Mtrs)',min_value=1.0,max_value=2.5,value=1.7)
income_lpa=st.number_input('Income (LPA)',min_value=0.1,value=10.0)
smoker=st.selectbox('Are You a Smoker',options=[True,False])
city=st.text_input('City',value='Mumbai')
occupation=st.selectbox('What is your Occupation? ',options=
[     'Factory Worker',         'Businessman',       'Sales Manager',
              'Banker',   'Marketing Manager',     'Insurance Agent',
          'HR Manager',          'Pharmacist',             'Teacher',
   'Software Engineer',          'Consultant',              'Driver',
          'Shop Owner',               'Nurse',          'Accountant',
 'Government Employee',           'Architect',            'Engineer',
   'Real Estate Agent',       'Civil Servant',             'Plumber',
      'Retail Manager',                'Chef',         'Electrician',
           'Carpenter',              'Doctor',      'Lab Technician',
        'Data Analyst',              'Lawyer',      'Content Writer'])

if st.button('Predict Premium Category'):
    input_data={
        'age':age,
        'weight':weight,
        'height':height,
        'income_lpa':income_lpa,
        'smoker':smoker,
        'city':city,
        'occupation':occupation
    }
    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"Predicted Insurance Premium Category:**{result}**")
        else:
            st.error(f'API ERROR :{response.status_code}-{response.text}')
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FASTAPI Server. Make sure it's running on port 8000")