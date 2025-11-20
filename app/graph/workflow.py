from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes import retrieve, generate, grade_documents

workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("grade_documents", grade_documents)

workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "grade_documents")

def decide_next_step(state):
    if state["grade"] == "useful":
        return END
    else:
        return "retrieve"

workflow.add_conditional_edges(
    "grade_documents",
    decide_next_step,
    {
        END: END,
        "retrieve": "retrieve"
    }
)

app = workflow.compile()