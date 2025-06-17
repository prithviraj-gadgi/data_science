import streamlit as st
import langchain_helper

st.title('Restaurant Application')

cuisine = st.sidebar.selectbox('Select a Cuisine', ('Indian', 'Italian', 'Chinese', 'Mexican'))
language = st.sidebar.selectbox('Select a Language', ('Hindi', 'Italian', 'Mandarin', 'English'))

if cuisine:
    result = langchain_helper.get_details(cuisine, language)
    st.header(result['restaurant_name'])
    st.write(result['restaurant_tagline'])
    st.write('**Menu Items**')
    st.write(result['food_menu'])