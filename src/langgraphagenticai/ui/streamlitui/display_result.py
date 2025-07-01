import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage


class DisplayResultStreamLit:
    def __init__(self,graph,usecase,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
    def display_result_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        print("usecase:",usecase)
        print("usecase:",user_message)

        if usecase=="Basic Chatbot":
            for events in graph.stream({"messages":user_message}):
                for value in events.values():
                    with st.chat_message("user"):
                        print("user_message:",user_message)
                        st.write(user_message)
                    with st.chat_message("assitant"):
                        print("response:",value["messages"].content)
                        st.write(value["messages"].content)
                        


