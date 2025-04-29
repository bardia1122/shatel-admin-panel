from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pandas as pd
import os

router = APIRouter()
DATA_FILE_PATH = "C:/Programs/Admin Panel/data.csv"

@router.post("/access_kb/upload")
async def upload_file(file: UploadFile = File(...), mode: str = Form(...)):
    if file.content_type not in ["text/csv", "application/vnd.ms-excel"]:
        raise HTTPException(status_code=400, detail="فقط فایل CSV مجاز است")

    uploaded_df = pd.read_csv(file.file)

    if not os.path.exists(DATA_FILE_PATH):
        uploaded_df.to_csv(DATA_FILE_PATH, index=False)
        return {"filename": "data.csv", "msg": "فایل جدید ایجاد شد."}

    existing_df = pd.read_csv(DATA_FILE_PATH)

    if mode == "append":
        result_df = pd.concat([existing_df, uploaded_df], ignore_index=True)
    elif mode == "replace":
        if 'id' not in existing_df.columns or 'id' not in uploaded_df.columns:
            raise HTTPException(status_code=400, detail="ستون 'id' باید در هر دو فایل وجود داشته باشد.")
        filtered_df = existing_df[~existing_df['id'].isin(uploaded_df['id'])]
        result_df = pd.concat([filtered_df, uploaded_df], ignore_index=True)
    else:
        raise HTTPException(status_code=400, detail="مد نامعتبر است.")

    result_df.to_csv(DATA_FILE_PATH, index=False)
    return {"filename": "data.csv", "msg": "آپلود و به‌روزرسانی موفقیت‌آمیز بود."}
