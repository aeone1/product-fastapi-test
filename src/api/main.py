

from uuid import uuid1
from fastapi import FastAPI, Request, status

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import scoped_session

from .api import api_router
from .session import session_made


async def not_found(request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": [{"msg": "Not Found."}]}
    )

exception_handlers = {404: not_found}


app = FastAPI(title="Products API", exception_handlers=exception_handlers)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get('/health_check', status_code=status.HTTP_200_OK)
async def health_check():
    return 'ok'


# we create the Web API framework
api = FastAPI(
    title="Products API",
    description="Welcome to Products's API documentation! Here you will able to discover all of the ways you can interact with the Products API.",
    root_path="/api/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """Middleware to attach a database session to each request."""
    session_factory = session_made()  # Get the session factory
    session = session_factory()  # Create a new session
    request.state.db = session  # Attach session to request

    try:
        response = await call_next(request)
    except Exception as e:
        session.rollback()  # Rollback transaction on error
        raise e from None
    finally:
        session.close()  # Ensure session is closed

    return response

# we add all API routes to the Web API framework
api.include_router(api_router)

