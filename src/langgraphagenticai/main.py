import streamlit as st
import json

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLM.groq_llm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamLit

def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_input  = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI.")
        return
    
    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error:LLM Model can not be intialized")
                return
            
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            graph_builder = GraphBuilder(model=model)
            graph = graph_builder.setup_graph(usecase=usecase)

            DisplayResultStreamLit(graph,usecase,user_message).display_result_ui()

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")