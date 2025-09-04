import httpx

TABNEWS_BASE_URL = "https://www.tabnews.com.br/api/v1"

async def fetch_posts(query: str = None, tag: str = None, author: str = None, limit: int = 10):
    """
    Fetch posts from TabNews API with optional filters.
    """
    params = {}
    if query:
        params["q"] = query
    if tag:
        params["tag"] = tag
    if author:
        params["user"] = author
    params["per_page"] = limit

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TABNEWS_BASE_URL}/contents", params=params)
        response.raise_for_status()
        return response.json()
