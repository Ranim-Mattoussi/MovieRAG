# MovieRAG

A simple Python Retrieval-Augmented Generation (RAG) demo using the IMDB Top 1000 movies dataset.

## Project Structure

- `main.py` - CLI application that accepts a movie-related question, retrieves relevant reviews, and uses a language model to answer.
- `vector.py` - Builds or loads the Chroma vector store from `imdb_top_1000.csv` and exposes a retriever.
- `requirements.txt` - Python dependencies required to run the app.
- `imdb_top_1000.csv` - Movie dataset used to create embedding documents.
- `chroma_storage/` - Persistent local Chroma database directory for storing vector embeddings.
- `venv/` - Optional Python virtual environment directory (not committed in source control).

## 🛠️ Tech Stack

- Python 3
- LangChain (Ollama integration)
- `langchain_ollama` for LLM inference and embeddings
- Chroma vector store for retrieval
- Pandas for dataset loading and preprocessing
- Ollama models: `llama3.2` for generation and `mxbai-embed-large` for embeddings

## How It Works

1. `vector.py` reads `imdb_top_1000.csv` and creates documents from movie titles and overviews.
2. It uses `OllamaEmbeddings` to compute embeddings and stores them in a Chroma vector database.
3. `main.py` retrieves the top 5 most relevant movie reviews for the input question.
4. It then sends the retrieved reviews and the user question to `OllamaLLM` for a final answer.

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Ensure your environment can access Ollama models or configure the model service used by `langchain_ollama`.

## Usage

Run the application from the project root:

```powershell
python main.py
```

Then type a movie question and press Enter.

Example questions:

- `What is the story of The Godfather?`
- `Which films in the dataset are highly rated crime dramas?`

Type `q`, `quit`, or `exit` to close the app.

## Notes

- `chroma_storage/` is created automatically if it does not exist.
- The first run may take longer because embeddings are built and persisted.
- You can update `imdb_top_1000.csv` to change the dataset used for retrieval.
- If you want to use a different model, update `model="llama3.2"` in `main.py` and the embedding model in `vector.py`.
