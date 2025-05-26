import streamlit as st
from utils import generate_blog

st.title("Blog Generation App")

blog_topic = st.text_input("Enter your blog topic here", placeholder="e.g. 'Future of AI in Healthcare'")

col1, col2, col3, col4 = st.columns(4)

with col1:
    # blog_wordcount = st.text_input("Words", key="blog_wordcount")
    blog_wordcount = st.slider("Word Count", min_value=1000, max_value=2000, value=1500, step=100)
    
with col2:
    blog_style = st.selectbox("Writing Style", 
                              ["Professional", "Conversational", "Technical", "Storytelling",
                               "Listicle", "Interview"], 
                              index=0, key="blog_style")
    
with col3:
    blog_tone = st.selectbox("Tone", 
                             ["Authoritative", "Friendly", "Informative", "Persuasive",
                              "Neutral", "Humorous"], 
                             index=0, key="blog_tone")
    
with col4:
    blog_audience = st.selectbox("Target Audience",
                                 ["General Readers", "Industry Professionals", "Academic Researchers",
                                  "Students"])

if st.button("Generate Blog"):
    st.write(generate_blog(blog_topic, blog_wordcount, blog_style, blog_tone, blog_audience))