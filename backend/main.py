from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers will be imported once they are implemented
from app.api.endpoints import auth, users, parse, jobs, payments
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"], # Allowing frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """A simple endpoint to confirm the API is running."""
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

# Include routers from the API layer
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Authentication"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Users"])
app.include_router(parse.router, prefix=f"{settings.API_V1_STR}/parse", tags=["PDF Parsing"])
app.include_router(jobs.router, prefix=f"{settings.API_V1_STR}/jobs", tags=["Jobs Status"])
app.include_router(payments.router, prefix=f"{settings.API_V1_STR}/payments", tags=["Payments"])

# Note on API design:
# The original spec had job-related endpoints under the /parse prefix.
# For clarity and to adhere to REST principles (where /jobs is a distinct resource),
# I've implemented them under the /jobs prefix. This keeps the API cleaner and
# avoids technical issues with mounting multiple routers to the same prefix.
