from fastapi import APIRouter, Depends
from app.deps import has_permission

router = APIRouter()

@router.get("/logs")
def view_logs(permission = Depends(has_permission("view_logs"))):
    return {"msg": "User Level 3 can view logs."}

@router.get("/access-db")
def access_db(permission = Depends(has_permission("access_db"))):
    return {"msg": "User can access database"}

@router.get("/manage-data")
def admin_zone(permission = Depends(has_permission("manage_data"))):
    return {"msg": "Entering manage data"}

@router.get("/access-kb")
def admin_zone(permission = Depends(has_permission("access-kb"))):
    return {"msg": "Access to Knowledge Base"}