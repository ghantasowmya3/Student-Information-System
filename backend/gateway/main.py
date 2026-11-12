from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import authController

app = FastAPI(title="Student Information System Gateway", version="1.0.0")

# Configure CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(authController.router, prefix="/authservice", tags=["Authentication"])

@app.get("/")
async def root():
    return {
        "message": "Student Information System Gateway",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "authentication": {
                "signup": "POST /authservice/signup",
                "signin": "POST /authservice/signin",
                "userinfo": "GET /authservice/uinfo",
                "profile": "GET /authservice/profile",
                "getallusers": "GET /authservice/getallusers/{page}/{size}",
                "searchuser": "GET /authservice/searchuser/{keyword}",
                "saveuser": "POST /authservice/saveuser",
                "updateuser": "PUT /authservice/updateuser/{id}",
                "deleteuser": "DELETE /authservice/deleteuser/{id}"
            },
            "feedback": {
                "submit": "POST /authservice/feedback/submit",
                "getall": "GET /authservice/feedback/all",
                "reply": "PUT /authservice/feedback/reply/{id}",
                "delete": "DELETE /authservice/feedback/delete/{id}",
                "stats": "GET /authservice/feedback/stats"
            },
            "students": {
                "getall": "GET /authservice/studentservice/getallstudents/{page}/{size}",
                "save": "POST /authservice/studentservice/savestudent",
                "update": "PUT /authservice/studentservice/updatestudent/{id}",
                "delete": "DELETE /authservice/studentservice/deletestudent/{id}",
                "search": "GET /authservice/studentservice/searchstudent/{keyword}"
            }
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "services": {
            "fastapi": "running",
            "springboot": "http://localhost:8001",
            "nodejs": "http://localhost:8002"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)