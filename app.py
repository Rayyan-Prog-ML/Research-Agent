'''
benefit of template instead of fstring is 
1. Default validation 
2. Reusable (can make a json template and reuse it)
3. Langchain ecosystem(can make a chain)
chain: input->template->model->output
output ko st.write karwadia
'''

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model=GoogleGenerativeAI(model="gemini-2.0-flash")
st.header("🧠 AI Research Assistant", divider="rainbow")
# --- Select Research Paper ---
paper = st.selectbox(
    "📄 Select Research Paper",
    options=[
        "GPT-4 Technical Report",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "Chain of Thought Prompting",
        "Retrieval-Augmented Generation (RAG)"
    ]
)

# --- Select Explanation Style ---
style = st.selectbox(
    "🎨 Select Explanation Style",
    options=[
        "Beginner Friendly",
        "Intermediate (Some Jargon)",
        "Technical / Academic"
    ]
)

# --- Select Explanation Length ---
length = st.selectbox(
    "📏 Select Explanation Length",
    options=[
        "Very Short (1-2 lines)",
        "Short (1 paragraph)",
        "Medium (2-3 paragraphs)",
        "Detailed (long explanation)"
    ]
)
#template
template=load_prompt('template.json')

if st.button("Summarize"):
    chain=template | model
    res=chain.invoke({'paper': paper,
                 "style":style,
                 "length": length
                 })
    st.write(res)
    
