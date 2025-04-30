from fastapi import APIRouter, HTTPException
import httpx
import websockets
import json

router = APIRouter()

@router.get("/access_db/send")
async def access_db():
    url = "wss://ai.shatel.ir/chat"
    try:
        async with websockets.connect(url) as websocket:
            await websocket.send("بدون هیچ توضیح اضافه ای قیمت سرویس های ADSL رو بگو")
            response = await websocket.recv()
            
            # Parse the response to extract the "bot" message
            response_data = json.loads(response)
            history = response_data.get("history", [])
            print(response)
            # Extract the "bot" message from the history
            bot_message = ""
            if history and isinstance(history, list):
                bot_message = history[-1].get("bot", "")
            
            # Print and return the bot message
            print(bot_message)
            return {"response": bot_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"WebSocket connection failed: {e}")
    