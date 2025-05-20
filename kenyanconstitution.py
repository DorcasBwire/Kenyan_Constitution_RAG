!pip install dotenv
!pip install langchain_community
!pip install langchain_huggingface
!pip install langchain_chroma
!pip install groq
!pip install langchain_groq

#import libraries
import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_groq import ChatGroq
from langchain.document_loaders import PyPDFLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#Load env
load_dotenv()
#Read env. files
os.environ["GROQ_API_KEY"] = "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"


GROQ_API_KEY = os.environ["GROQ_API_KEY"]

# Confirm the retrieval of the API keys
if GROQ_API_KEY:
    print("GROQ_API_KEY is set")
else:
    print("GROQ_API_KEY is not set")

#Load the PDF file
!pip install PyPDF
loader = PyPDFLoader("constitution_of_kenya.pdf")
documents = loader.load()
print("PDF loaded successfully")

#Split the document into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(documents)

print(f"Total chunks: {len(documents)}")

#embedding model
embedding = HuggingFaceEmbeddings(
    model_name="all-mpnet-base-v2",
)

#Create a vector store
db = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory="chroma_db"
)
print("Vector store created successfully")

#Define the retiever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

#Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    ["""You are a constitutional analyst specialized in the Kenyan Constitution.
    Use only the following excerpts from the Kenyan Constitution to answer the question.
    If the specific information isn't found in these excerpts, state that the information
isn't available in the provided constitutional sections rather than speculating.

CONSTITUTIONAL EXCERPTS:
{context}

Question: {question}
Answer based strictly on the Kenyan Constitution:"""
    ]
)

#Initialize the model
model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key = GROQ_API_KEY,
    temperature = 0,
    prompt = prompt
)

#Set up RAG Chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

#test the retriever
query = "What are the children rights regarding education according to the Kenyan Constitution?"
docs = retriever.get_relevant_documents(query)

# Print results
for i, doc in enumerate(docs):
    print(f"\n--- Document {i+1} ---\n")
    print(doc.page_content)
