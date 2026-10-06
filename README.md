# AlgoSage — GenAI DSA Study Assistant

AlgoSage is a study chatbot that answers data structures and algorithms
questions using local notes. It retrieves relevant passages and uses
Gemini to generate answers with source labels.

## How It Works

1. Split notes into smaller chunks.
2. Generate embeddings using a Hugging Face Sentence Transformers model.
3. Store the chunks and embeddings in Chroma.
4. Retrieve relevant passages for each question.
5. Send those passages to Gemini through LangChain.
6. Display the answer and retrieved passages in Streamlit.

This approach is called Retrieval-Augmented Generation (RAG).
It provides context to the model without retraining it.

## Technologies

- Python — application logic
- Streamlit — interactive chat interface
- LangChain — model and vector database integrations
- Hugging Face / Sentence Transformers — local text embeddings
- Chroma — vector storage and similarity search
- Gemini API — answer generation
- python-dotenv — environment configuration
- Git and GitHub — version control

## MCP Integration

The earlier MCP version exposes a `read_notes()` tool through a local
server. The current RAG interface accesses Chroma directly.

## Run the Interface

With dependencies installed, the Chroma database indexed, and your
Gemini credentials configured in `.env`, run:

    python -m streamlit run ui.py --server.fileWatcherType none

## Limitations

Answers and citations may contain mistakes. Gemini API quotas apply.
Changes to notes require rebuilding the index. Retrieval currently
uses only the latest question.

## Planned Enhancements

- LangGraph workflow for retrieval, context checking, and answering
- MCP tool for vector search
- Improved retrieval for follow-up questions
