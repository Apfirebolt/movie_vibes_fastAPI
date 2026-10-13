import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastembed import TextEmbedding
from qdrant_client import QdrantClient

load_dotenv()
app = FastAPI(title="Movie Vibes FastAPI", version="1.0.0")

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# 1. Configuration Credentials for Qdrant Cloud
# (Tip: You can also use os.getenv("QDRANT_URL") for production/Vercel environments)
QDRANT_URL = os.getenv("QDRANT_URL", "YOUR_QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "YOUR_QDRANT_API_KEY")
COLLECTION_NAME = "Hollywood_movies"

# Initialize FastEmbed model globally so it doesn't reload on every single request
embedding_model = TextEmbedding()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the home page using Jinja2 templates."""
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "title": "Movie Vibes Finder",
            "heading": "Welcome to Movie Vibes",
            "message": "Explore and search movie recommendations powered by FastAPI, Qdrant, and FastEmbed."
        }
    )

@app.get("/search", response_class=HTMLResponse)
async def search_vibes(request: Request, q: str = Query(..., description="Search query")):
    """Perform vector search using FastEmbed and Qdrant Cloud."""
    try:
        # Generate embedding locally for the user query
        vector_generator = embedding_model.embed([q])
        query_vector = list(vector_generator)[0].tolist()

        # Connect to Qdrant Cloud and run vector search
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        
        search_response = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=10
        )

        # Extract and format the matching points/payloads
        movies = []
        for hit in search_response.points:
            print(f"Hit: {hit}")  # Debugging line to inspect the search results
            meta = hit.payload or {}
            movies.append({
                "title": meta.get("title", "Unknown Title"),
                "director": meta.get("director", "Unknown"),
                "imdb_rating": meta.get("imdb_score", "N/A"),
                "genres": meta.get("genres", "N/A"),
            })

        message = f"Found {len(movies)} matching movie vibes for: '{q}'"
    except Exception as e:
        movies = []
        message = f"Error executing search: {str(e)}"

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "title": f"Search Results for '{q}'",
            "heading": f"Results for: {q}",
            "message": message,
            "movies": movies,
            "search_query": q
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)