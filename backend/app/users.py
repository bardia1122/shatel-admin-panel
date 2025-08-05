from fastapi import APIRouter, Depends
from app.deps import has_permission

router = APIRouter()

@router.get("/logs")
def view_logs(permission = Depends(has_permission("view_logs"))):
    return {"msg": "View logs"}

@router.get("/access_db")
def access_db(permission = Depends(has_permission("access_db"))):
    return {"msg": "Access Database"}

@router.get("/manage_data")
def admin_zone(permission = Depends(has_permission("manage_data"))):
    return {"msg": "Entering manage data"}

@router.get("/access_kb")
def access_kb(permission = Depends(has_permission("access_kb"))):
    return {"msg": "Access Knowledge Base"}

@router.get("/dashboard")
def dashboard():
    return {"msg": "Dashboard"}