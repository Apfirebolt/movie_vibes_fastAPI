from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Movie Vibes FastAPI", version="1.0.0")

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

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
    """Placeholder endpoint for your Qdrant + FastEmbed vector search logic."""
    # TODO: Implement FastEmbed vectorization and Qdrant similarity search here
    
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "title": f"Search Results for '{q}'",
            "heading": f"Results for: {q}",
            "message": f"Showing results for your search: '{q}'. Vector search integration is ready to be plugged in!"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)