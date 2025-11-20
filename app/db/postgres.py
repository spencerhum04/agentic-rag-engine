from dotenv import load_dotenv
load_dotenv()

from langchain_postgres import PGVector
from langchain_openai import OpenAIEmbeddings

# Connect to the Docker database
connection = "postgresql+psycopg://admin:password@localhost:5432/vector_db"
collection_name = "company_docs"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)