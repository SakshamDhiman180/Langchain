from dotenv import load_dotenv
import os

os.environ["GOOGLE_API_KEY"] = os.getenv('GEMINI_API_KEY')

from langchain_google_vertexai import ChatVertexAI

model = ChatVertexAI(model="gemini-pro")

from langchain_core.messages import HumanMessage

x=model.invoke([HumanMessage(content="Hi! I'm Bob")])

print(x)