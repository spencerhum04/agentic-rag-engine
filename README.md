# Agentic RAG Engine

A self-correcting Retrieval Augmented Generation (RAG) system engineered to minimize AI hallucinations.

## Key Features
- Self-Correcting Mechanism: Implements a "Grader" node that evaluates the faithfulness of the LLM's response against source documents before returning it to the user.
- Stateful Orchestration: Uses LangGraph to maintain state across the retrieval, generation, and grading steps, enabling complex cyclic logic.
- Production-Grade Vector Storage: Leverages PostgreSQL with pgvector rather than ephemeral in-memory stores, simulating a real-world enterprise environment.
- Asynchronous API: Built on FastAPI with uvicorn to handle concurrent user requests efficiently.
- Containerized Infrastructure: Fully dockerized database setup for consistent deployment across environments.