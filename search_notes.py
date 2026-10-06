from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

folder = Path(__file__).resolve().parent
database_path = folder / "chroma_db"

if not database_path.exists():
    raise SystemExit("Database not found. Run the indexing script first.")

# Use the same embedding settings as index_notes.py.
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

while True:
    question = input("\nSearch your notes, or type exit: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    results = database.similarity_search(question, k=3)

    for number, document in enumerate(results, start=1):
        print(f"\n--- Result {number} ---")
        print("Source:", document.metadata.get("source"))
        print(document.page_content)