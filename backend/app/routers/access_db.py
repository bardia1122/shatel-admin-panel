from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/access_db/send")
async def access_db():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            print(response.text)
        return {"status": "success", "data": response.json()}
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {url}: {e}")
        raise HTTPException(status_code=500, detail="Failed to access the URL")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail="HTTP error occurred")