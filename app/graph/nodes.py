from app.graph.state import GraphState
from app.db.postgres import vector_store
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def retrieve(state: GraphState):
    print("---RETRIEVE---")
    question = state["question"]
    
    docs = vector_store.similarity_search(question, k=2)
    
    return {"documents": docs}

def generate(state: GraphState):
    print("---GENERATE---")
    question = state["question"]
    docs = state["documents"]
    
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.
    If the answer is not in the context, say "I don't know".
    
    Context: {context}
    
    Question: {question}
    """
    
    response = llm.invoke(prompt)
    
    return {"generation": response.content}

def grade_documents(state: GraphState):
    print("---CHECK HALLUCINATIONS---")
    question = state["question"]
    generation = state["generation"]
    
    grader_prompt = f"""You are a grader. 
    User Question: {question}
    System Answer: {generation}
    
    Does the answer verify the facts? Answer 'yes' or 'no'."""
    
    score = llm.invoke(grader_prompt).content
    
    if "yes" in score.lower():
        return {"grade": "useful"}
    else:
        return {"grade": "not useful"}