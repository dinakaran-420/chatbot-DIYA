from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from requests.exceptions import ConnectionError

# Set up Streamlit page
st.set_page_config(page_title='DIYA AI')
st.title("DIYA CHATBOT")     
st.caption("The Website is under maintenance, sorry for the late responses.")

# Input box for user query
input_txt = st.text_input("Ask Anything...")
submit = st.button("Submit")

# Initialize prompt and model
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a generative AI Assistant. Your name is Diya."),
     ("user", "User query: {query}")]
)
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Display response on submit
if submit and input_txt:
    try:
        response = chain.invoke({"query": input_txt})
        st.write(response)
    except ConnectionError:
        st.error("Connection error: Unable to reach the AI model server. Please check your internet connection or try again later.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
