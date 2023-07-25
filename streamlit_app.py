import os
import openai
import numpy as np
import streamlit as st

openai.api_type = "azure"
openai.api_base = "https://dev-gpt.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
#openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

def product_enhancement(title, desc):
    mes=[
        {"role": "system", "content": "You are a professional copywriter."},
        {"role": "user", "content": f"Write a SEO product title from this {title}, product tagline, and improve the following product description in a persuasive tone so more people will buy the product in e-commerce page. Do not change any numerical detail. Write it in Bahasa Indonesia: {desc}"}
        ]
          
    response_text = openai.ChatCompletion.create(
      engine="dev-gpt-4",
      messages = mes,
      temperature=0.7,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
    
    try:
        text = response_text["choices"][0]["message"]["content"]
        print('Desc generated')
    except:
        print("Cannot generate description")
        text = ' '
    out_text =text.replace(r'\n', '\n')

    return out_text

def ads(text):

    # create ads tone 
    mesg=[
        {"role": "system", "content": "You are a copywriter expert in creative agency."},
        {"role": "user", "content": f"Write creative advertising words in Bahasa Indonesia (maximum 20 words) in different tones (friendly, funny, insightful, with personal connection, with emotional appeal) based on the following product description {text}"}
    ]
          
    response_ads = openai.ChatCompletion.create(
      engine="dev-gpt-4",
      messages = mesg,#n = 5,
      temperature=0.9,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
    
    try:
        text_ads = [response_ads["choices"][0]["message"]["content"]]
        print('Ads generated')

    except:
        print("Cannot generate ads wording")
        text_ads = ' '
        
    ads =text_ads[0].replace(r'\n', '\n')
    
    return ads

def script(text):

     # create content script
    mesg=[
        {"role": "system", "content": "You are a copywriter expert in creative agency."},
        {"role": "user", "content": f"Write a influencer marketing script in Bahasa Indonesia (maximum for 30 seconds content) based on the following product description {text}"}
    ]
          
    response_ads = openai.ChatCompletion.create(
      engine="dev-gpt-4",
      messages = mesg,#n = 5,
      temperature=0.9,
      max_tokens=1000,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
    
    try:
        script = [response_ads["choices"][0]["message"]["content"]]
        print('Script generated')

    except:
        print("Cannot generate script")
        script = ' '

    promo = script[0].replace(r'\n', '\n')
    
    return promo

# Page title
st.set_page_config(page_title='Rosemary App')
st.title('Rosemary')
st.header('Rosemary: Konten Produk Jadi Lebih Mantap!')


# Form to accept user's text input for summarization
result_txt = []
result_ads = []
result_promo = []

col1, col2 = st.columns(2)
with col1:
    #Title input
    title = st.text_area('Masukkan judul produk Anda: ', '', height=20)
    desc = st.text_area('Masukkan deskripsi produk Anda: ', '', height = 200)

#with st.form('summarize_form', clear_on_submit=True):
#submitted = st.form_submit_button('Submit')
submitted = st.button('Submit')

if submitted:
    with st.spinner('Tunggu proses 1-2 menit ya...'):
        if len(desc) > 3:
            text = product_enhancement(title, desc)
            result_txt.append(text)
        else:
            st.warning('Tolong berikan judul dan deskripsi produk (minimal 5 kata)', icon="⚠️")
            #st.write('Error:Tolong berikan judul dan deskripsi produk (minimal 5 kata)')
    
with col2:
    if len(result_txt):
        st.text_area(label ='Output setelah diperbaiki: ',value= ' '.join(result_txt), height =300)
    #else:
    #    st.write('Error: Tolong perbaiki input Anda (memenuhi standard kesopanan, etika, dan dalam bahasa Indonesa/Inggris')

place1 = st.empty()
place2 = st.empty()

# ads
if len(desc) > 3:
    text_ads = ads(result_txt)
    result_ads.append(text_ads)
    with place1.container():
        st.subheader('Kalimat promo produk dengan pilihan tones:')
        for item in result_ads:
            st.write(item) 

#script
if len(desc) > 3:
    promo = script(result_txt)
    result_promo.append(promo)
    with place2.container():
        st.subheader('Konten untuk di post di socmed kamu:')
        for item in result_promo:
            st.write(item)

#rate
rate = st.radio(
    "Berikan penilaian",
    ('Bagus', 'Kurang pas'))
if rate == 'Bagus':
    st.write('Terimakasih atas penilaian Anda.')
else:
    st.write("Akan kami perbaiki lagi. Terimakasih atas penilaian Anda.")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.write('About Us: Rosemary is a Bukalapak Data Co Generative AI Text Enhancement Product - 2023')


