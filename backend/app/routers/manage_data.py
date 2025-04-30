from fastapi import APIRouter, Depends, Form, HTTPException
from app.deps import has_permission
from datetime import datetime, timedelta
from pymongo import MongoClient
import json
import os
from fastapi.responses import FileResponse
router = APIRouter()

# mongo_client = MongoClient("mongodb://admin:bank160225@172.16.1.251:27017/?authSource=admin")
# db = mongo_client["train_chat_collection"]
# collection = db["chats"]

@router.post("/manage_data/export")
def export_data(
    start_date: str = Form(...),
    end_date: str = Form(...),
    permission=Depends(has_permission("manage_data"))
):
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1) - timedelta(seconds=1)
    except ValueError:
        raise HTTPException(status_code=400, detail="فرمت تاریخ اشتباه است!")

    if start_dt > end_dt:
        raise HTTPException(status_code=400, detail="تاریخ شروع نمیتواند بعد از تاریخ پایان باشد!")

    query = {
        "messages.timestamp": {
            "$gte": start_dt,
            "$lte": end_dt
        }
    }
    # data = list(collection.find(query, {"_id": 0}))
    _data = [{"id": 1, "user": "hello"}]
    data = json.dumps(_data)
    if not data:
        raise HTTPException(status_code=404, detail="هیچ داده ای در تاریخ خواسته شده یافت نشد!")

    # for doc in data:
    #     if "messages" in doc:
    #         for message in doc["messages"]:
    #             if "timestamp" in message and isinstance(message["timestamp"], datetime):
    #                 message["timestamp"] = message["timestamp"].isoformat()

    filename = f"export_{start_dt.strftime('%Y-%m-%d')}_to_{end_dt.strftime('%Y-%m-%d')}.json"
    filepath = os.path.join("/tmp", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(_data, f, ensure_ascii=False, indent=4)

    #return {"status": "success", "filename": filename}
    return FileResponse(path=filepath, filename=filename, media_type='application/json')
