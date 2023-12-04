import os
import streamlit as st 
from langchain.llms import openai
from langchain.llms import AzureOpenAI
from langchain.agents import  load_tools, initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"] = 'https://aoiaipsi.openai.azure.com/'

os.environ["OPENAI_API_KEY"] = os.environ["AZURE_OPENAI_API_KEY"] = 'f769445c82844edda56668cb92806c21'

os.environ["OPENAI_API_VERSION"] = os.environ["AZURE_OPENAI_API_VERSION"] = "2023-07-01-preview" #"2023-03-15-preview"

os.environ["OPENAI_API_TYPE"] = "azure"

AZURE_OPENAI_NAME = 'gpt-35-turbo-0301'

llm = AzureOpenAI(temprature=0,streaming=True,openai_api_key="OPENAI_API_KEY")
tools = load_tools(
    ["ddg-search"]
)
agent = initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if prompt := st.chat_input():
    st.chat_message("user").write("prompt")
    with st.chat_message("assistant"):
        st.write("thinking....")   
        st_callback = StreamlitCallbackHandler(st.container())    
        response = agent.run(prompt, callbacks=[st_callback])
     

