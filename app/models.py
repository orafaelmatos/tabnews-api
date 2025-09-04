from pydantic import BaseModel
from typing import List, Optional

class Post(BaseModel):
    id: str
    title: str
    content: str
    user: str
    tags: Optional[List[str]] = []

class SearchResponse(BaseModel):
    posts: List[Post]
    total: int
