import httpx
from fastapi import APIRouter, Request, Header, HTTPException
from typing import Optional
from models.schemas import SignupSchema, SigninSchema

# Make sure router is defined at the top
router = APIRouter()
SPRINGBOOT_URL = "http://localhost:8001"
NODEJS_URL = "http://localhost:8002"

# ============ AUTHENTICATION ENDPOINTS ============

@router.post("/signup")
async def signup(user: SignupSchema):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{SPRINGBOOT_URL}/user/signup",
            json=user.dict()
        )
        return response.json()

@router.post("/signin")
async def signin(login: SigninSchema):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{SPRINGBOOT_URL}/user/signin",
            json=login.dict()
        )
        return response.json()

@router.get("/uinfo")
async def get_user_info(Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{SPRINGBOOT_URL}/user/uinfo",
            headers={"Token": Token}
        )
        return response.json()

@router.get("/profile")
async def get_profile(Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{SPRINGBOOT_URL}/user/profile",
            headers={"Token": Token}
        )
        return response.json()

@router.get("/getallusers/{page}/{size}")
async def get_all_users(page: int, size: int, Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{SPRINGBOOT_URL}/user/getallusers/{page}/{size}",
            headers={"Token": Token}
        )
        return response.json()

@router.get("/searchuser/{keyword}")
async def search_user(keyword: str, Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{SPRINGBOOT_URL}/user/searchuser/{keyword}",
            headers={"Token": Token}
        )
        return response.json()

@router.post("/saveuser")
async def save_user(request: Request, Token: str = Header(...)):
    body = await request.json()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{SPRINGBOOT_URL}/user/saveuser",
            json=body,
            headers={"Token": Token}
        )
        return response.json()

@router.put("/updateuser/{id}")
async def update_user(id: int, request: Request, Token: str = Header(...)):
    body = await request.json()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.put(
            f"{SPRINGBOOT_URL}/user/updateuser/{id}",
            json=body,
            headers={"Token": Token}
        )
        return response.json()

@router.delete("/deleteuser/{id}")
async def delete_user(id: int, Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.delete(
            f"{SPRINGBOOT_URL}/user/deleteuser/{id}",
            headers={"Token": Token}
        )
        return response.json()

# ============ STUDENT MANAGEMENT ENDPOINTS ============

@router.get("/studentservice/getallstudents/{page}/{size}")
async def get_all_students(page: int, size: int, Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{SPRINGBOOT_URL}/student/getallstudents/{page}/{size}",
            headers={"Token": Token}
        )
        return response.json()

@router.post("/studentservice/savestudent")
async def save_student(request: Request, Token: str = Header(...)):
    body = await request.json()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{SPRINGBOOT_URL}/student/savestudent",
            json=body,
            headers={"Token": Token}
        )
        return response.json()

@router.put("/studentservice/updatestudent/{id}")
async def update_student(id: int, request: Request, Token: str = Header(...)):
    body = await request.json()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.put(
            f"{SPRINGBOOT_URL}/student/updatestudent/{id}",
            json=body,
            headers={"Token": Token}
        )
        return response.json()

@router.delete("/studentservice/deletestudent/{id}")
async def delete_student(id: int, Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.delete(
            f"{SPRINGBOOT_URL}/student/deletestudent/{id}",
            headers={"Token": Token}
        )
        return response.json()

@router.get("/studentservice/searchstudent/{keyword}")
async def search_student(keyword: str, Token: str = Header(...)):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{SPRINGBOOT_URL}/student/searchstudent/{keyword}",
            headers={"Token": Token}
        )
        return response.json()

# ============ FEEDBACK ENDPOINTS (MongoDB) ============

@router.post("/feedback/submit")
async def submit_feedback(request: Request, Token: str = Header(...)):
    """Submit feedback to MongoDB via Node.js backend"""
    body = await request.json()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{NODEJS_URL}/feedback/submit",
            json=body,
            headers={"Token": Token}
        )
        return response.json()

@router.get("/feedback/all")
async def get_all_feedbacks(Token: str = Header(...)):
    """Get all feedbacks from MongoDB"""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{NODEJS_URL}/feedback/all",
            headers={"Token": Token}
        )
        return response.json()

@router.put("/feedback/reply/{id}")
async def reply_feedback(id: str, request: Request, Token: str = Header(...)):
    """Reply to a feedback"""
    body = await request.json()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.put(
            f"{NODEJS_URL}/feedback/reply/{id}",
            json=body,
            headers={"Token": Token}
        )
        return response.json()

@router.delete("/feedback/delete/{id}")
async def delete_feedback(id: str, Token: str = Header(...)):
    """Delete a feedback (Admin only)"""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.delete(
            f"{NODEJS_URL}/feedback/delete/{id}",
            headers={"Token": Token}
        )
        return response.json()

@router.get("/feedback/stats")
async def get_feedback_stats(Token: str = Header(...)):
    """Get feedback statistics"""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{NODEJS_URL}/feedback/stats",
            headers={"Token": Token}
        )
        return response.json()