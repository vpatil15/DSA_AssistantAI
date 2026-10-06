# This file is used to read your text document file and split them into chunks and store their embeddings .
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

folder = Path(__file__).resolve().parent.parent
database_path = folder / "chroma_db"

# Prevent accidental duplicate indexing in this first version.
if database_path.exists():
    raise SystemExit(
        "chroma_db already exists. Keep it for searching. "
        "To rebuild, remove only that generated folder and run again."
    )

documents = []

for path in sorted((folder / "Data").glob("*.txt")):
    text = path.read_text(encoding="utf-8")

    if text.strip():
        documents.append(
            Document(
                page_content=text,
                metadata={"source": path.name},
            )
        )

if not documents:
    raise SystemExit("Add at least one non-empty .txt file to data.")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    add_start_index=True,
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

database = Chroma(
    collection_name="dsa_notes",
    embedding_function=embeddings,
    persist_directory=str(database_path),
)

database.add_documents(chunks)

print(f"Indexed {len(documents)} files into {len(chunks)} chunks.")