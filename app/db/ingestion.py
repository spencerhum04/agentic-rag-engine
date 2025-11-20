from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.db.postgres import vector_store

from dotenv import load_dotenv
load_dotenv() 

def ingest():
    print("Loading data...")
    loader = TextLoader("./data/handbook.txt")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    splits = text_splitter.split_documents(docs)

    print(f"Inserting {len(splits)} chunks into Postgres...")
    vector_store.add_documents(splits)
    print("Done!")

if __name__ == "__main__":
    ingest()