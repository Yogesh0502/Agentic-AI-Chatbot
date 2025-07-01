from src.langgraphagenticai.state.state import State

class BasicChatBotNode():
    def __init__(self,model):
        self.llm=model
    def chatbot(self,state):
        return {"messages":self.llm.invoke(state['messages'])}

