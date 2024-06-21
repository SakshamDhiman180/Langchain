# import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
# import vertexai
load_dotenv()

print("----------------------------------------------------->")
print(os.getenv('GEMINI_API_KEY'))

os.environ["GOOGLE_API_KEY"] = os.getenv('GEMINI_API_KEY')


# vertexai.init(project='langchain-tutorial-427106')

## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')

##prompt template

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a assistant, which will answer gk questions"),
    ("user","Question:{question}")
])

##streamlit framework

st.title('Lang-chain Demo with Gemini Api')
input_text=st.text_input("Ask any thing!")

# print(input_text)

##gemini bot
model = ChatGoogleGenerativeAI(model="gemini-pro")
output_parser = StrOutputParser()
model.invoke("Sing a ballad of LangChain.")

if input_text:
    for chunk in model.stream(input_text):
        with st.chat_message("Bot:"):
            st.write(chunk.content)
    