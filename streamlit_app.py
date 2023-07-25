import os
import numpy as np
import streamlit as st

def product_enhancement(txt):
    
    out_text = 'Udah di enhance nih' 
    ads = 'Ayo beli sekarang!' 
    promo = 'Like and subscribe ya!"
    
    return out_text, ads, promo

# Page title
st.set_page_config(page_title='Rosemary App')
st.title('Rosemary App')
st.header('Enhance your product content!')


# Form to accept user's text input for summarization
result_txt = []
result_ads = []
result_promo = []

col1, col2 = st.columns(2)
with col1:
    #Text input
    txt_input = st.text_area('Enter your product title and description', '', height=200)
    with st.form('summarize_form', clear_on_submit=True):
        submitted = st.form_submit_button('Submit')
        if submitted:
            with st.spinner('Processing...'):
                text, ads, promo = product_enhancement(txt_input)
                result_txt.append(text)
                result_ads.append(ads)
                result_promo.append(promo)
with col2:
    if len(result_txt):
        st.text_area(label ='Output: Enhanced product content',value= ' '.join(result_txt), height =200)

# ads
st.subheader('Output: Ads Wordings with various tones')
for item in result_ads:
    st.write(item)

#script
st.subheader('Output: Promotional script with tags')
for item in result_promo:
    st.write(item)

#rate
rate = st.radio(
    "Rate our results!",
    ('Good', 'Need improvement'))

st.write('About Us: Rosemary is a Bukalapak Data Co Generative AI Text Enhancement Product - 2023')
