import streamlit as st
import helper
import pickle

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

st.header('Duplicate Question Detection')

q1 = st.text_input('Enter Question 1')
q2 = st.text_input('Enter Question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]
    
    if result:
        st.success('The questions are duplicates.')
    else:
        st.error('The questions are not duplicates.')