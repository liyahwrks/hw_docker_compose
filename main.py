from fastapi import FastAPI
from api.routes import user, post

app = FastAPI(title="Blog API")

app.include_router(user.router, prefix="/api", tags=["users"])
app.include_router(post.router, prefix="/api", tags=["posts"])

@app.get("/")
async def root():
    return {
        "message": "Blog API",
        "docs": "/docs"
    }