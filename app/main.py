from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from app.services import fetch_posts
from app.models import Post


app = FastAPI(title="TabNews API Backend")


@app.get("/")
def root():
    return {"message": "Welcome to the TabNews API Backend"}


@app.get("/posts/search", response_model=List[Post])
async def search_posts(
    q: Optional[str] = Query(None, description="Search in content"),
    title: Optional[str] = Query(None, description="Search in title only"),
    tag: Optional[str] = Query(None, description="Filter by tag"),
    author: Optional[str] = Query(None, description="Filter by author"),
    limit: int = Query(10, description="Number of results"),
):
    try:
        raw_posts = await fetch_posts(limit=10)
        posts = [
            Post(
                id=post.get("id"),
                title=post.get("title") or "",
                content=post.get("content") or "",
                user=post.get("user") or "",
                tags=post.get("tags") or [],
            )
            for post in raw_posts
        ]

        if title:
            posts = [p for p in posts if title.lower() in p.title.lower()]
        elif q:
            posts = [p for p in posts if q.lower() in p.content.lower()]
        elif tag:
            posts = [p for p in posts if tag.lower() in (t.lower() for t in p.tags)]
        elif author:
            posts = [p for p in posts if author.lower() == p.user.lower()]

        return posts[:limit]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

