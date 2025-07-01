from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.node.basic_chatbot_node import BasicChatBotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder = StateGraph(State)
    def get_graph(self):
        self.basic_chatbot_node_class=BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node_class.chatbot)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase):
        if usecase=="Basic Chatbot":
            self.get_graph()
        return self.graph_builder.compile()