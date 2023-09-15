from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# Vectorise the sales response csv data and create embedding.
# function return embedded knowledge base 
def load_embed_data(filepath):
    loader = CSVLoader(file_path=filepath, encoding="utf8")
    documents = loader.load()
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    return db
