# Movie Vibes FastAPI

A FastAPI-based backend for a movie recommendation and review application. This project exposes REST APIs for browsing movies, getting recommendations, and managing user interactions with a rating and mood-based movie discovery experience.

## Features

- Movie catalog API
- Movie details and search endpoints
- Recommendation engine based on user preferences and movie vibes
- Review and rating support
- FastAPI with automatic OpenAPI/Swagger docs
- Easy local development setup

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy (if used in your project)
- PostgreSQL / SQLite (if applicable)

## Project Structure

```bash
movie_vibes_fastapi/
├── app/
│   ├── main.py
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── core/
├── requirements.txt
├── README.md
└── .env.example
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd movie_vibes_fastapi
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
uvicorn app.main:app --reload
```

5. Open the API docs:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

Create a `.env` file and add configuration values like:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/movie_vibes
SECRET_KEY=your-secret-key
```

## API Overview

Example endpoints may include:

- `GET /movies`
- `GET /movies/{movie_id}`
- `GET /recommendations`
- `POST /reviews`
- `GET /health`

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request for any improvements.

## Contact

For questions or support, contact the project maintainer.
