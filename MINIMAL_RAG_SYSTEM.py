# ── SETUP ──────────────────────────────────────────────
import urllib.request
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# ── DOWNLOAD SAMPLE PDF ───────────────────────────────
url = “https://constitutioncenter.org/media/files/constitution.pdf”
pdf_filename = “constitution.pdf”
urllib.request.urlretrieve(url, pdf_filename)
print(f”✅ Downloaded: {pdf_filename}”)

# ── STEP 1: LOAD ──────────────────────────────────────
loader = PyPDFLoader(pdf_filename)
pages = loader.load()
print(f”✅ Loaded {len(pages)} pages”)

# ── STEP 2: CHUNK ─────────────────────────────────────
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=[”\n\n”, “\n”, “. “, “ “, “”]
)
chunks = text_splitter.split_documents(pages)
print(f”✅ Created {len(chunks)} chunks”)

# ── STEP 3 & 4: EMBED + STORE ────────────────────────
embeddings = HuggingFaceEmbeddings(
    model_name=”all-MiniLM-L6-v2”,
    model_kwargs={”device”: “cuda”}
)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=”./my_vectorstore”
)
print(f”✅ Stored {vectorstore._collection.count()} vectors in ChromaDB”)

# ── STEP 5: SET UP RETRIEVER ─────────────────────────
retriever = vectorstore.as_retriever(search_kwargs={”k”: 3})

# ── STEP 6: LOAD LLM ─────────────────────────────────
model_name = “google/flan-t5-base”
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
generator = pipeline(
    “text2text-generation”,
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    device=0
)
print(f”✅ Loaded LLM: {model_name}”)

# ── HELPER FUNCTIONS ──────────────────────────────────
def format_docs(docs):
    formatted = []
    for doc in docs:
        page = doc.metadata.get(’page’, ‘?’)
        formatted.append(f”[Source: Page {page}]\n{doc.page_content}”)
    return “\n\n---\n\n”.join(formatted)

def ask_rag(question, show_debug=True):
    retrieved_docs = retriever.invoke(question)
    context = format_docs(retrieved_docs)
    
    prompt = f”“”Answer the question based ONLY on the following context. 
If the context doesn’t contain enough information, say “I don’t have enough information to answer this.”
Do not make up information that isn’t in the context.

Context:
{context}

Question: {question}

Answer:”“”
    
    result = generator(prompt)[0][”generated_text”]
    
    if show_debug:
        print(f”\n🔎 Question: {question}”)
        print(f”\n📎 Retrieved {len(retrieved_docs)} chunks:”)
        for i, doc in enumerate(retrieved_docs):
            page = doc.metadata.get(’page’, ‘?’)
            print(f”\n  --- Chunk {i+1} (Page {page}) ---”)
            print(f”  {doc.page_content[:200]}...”)
        print(f”\n{’=’*60}”)
        print(f”💬 Answer: {result}”)
        print(f”{’=’*60}”)
    
    return result, retrieved_docs

# ── ASK QUESTIONS! ────────────────────────────────────
print(”\n” + “🔹” * 30)
answer, docs = ask_rag(”What does the First Amendment say about freedom of speech?”)



