from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.set_page_config(page_title='DIYA AI')
st.title("DIYA CHATBOT")
st.caption("The Website is under maintanence, sorry for the late responses.")
input_txt = st.text_input("Ask Anything...")


submit = st.button("Submit")
prompt = ChatPromptTemplate.from_messages(
    [("system","you are a generative AI Assistant. Your name is diya"),
     ("user","user query:{query}")]
)

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
  st.write(chain.invoke({"query":input_txt}))
