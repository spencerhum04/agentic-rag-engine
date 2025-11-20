from typing import TypedDict, List

class GraphState(TypedDict):
    question: str
    generation: str
    documents: List[str]
    grade: str