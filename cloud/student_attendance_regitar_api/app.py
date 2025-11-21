from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum

# Create API
app = FastAPI(title="Student Attendance API", version="1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------
# Request Model
# ---------------------------------------------
class Attendance(BaseModel):
    student_id: int
    student_name: str
    status: str  # Present / Absent

# Temporary DB
attendance_db = []

# ---------------------------------------------
# Health Check
# ---------------------------------------------
@app.get("/")
def home():
    return {"message": "Student Attendance API is running!"}

# ---------------------------------------------
# 1) Mark Attendance
# ---------------------------------------------
@app.post("/mark_attendance")
async def mark_attendance(data: Attendance):

    record = {
        "student_id": data.student_id,
        "student_name": data.student_name,
        "status": data.status
    }

    attendance_db.append(record)

    return {
        "message": f"Attendance marked for {data.student_name} ({data.status})",
        "record": record
    }

# ---------------------------------------------
# 2) View Attendance Summary
# ---------------------------------------------
@app.get("/attendance_summary")
async def summary():

    total = len(attendance_db)
    present = len([s for s in attendance_db if s["status"].lower() == "present"])
    absent = len([s for s in attendance_db if s["status"].lower() == "absent"])

    return {
        "total_students": total,
        "present": present,
        "absent": absent
    }

# ---------------------------------------------
# AWS Lambda Handler
# ---------------------------------------------
lambda_handler = Mangum(app)
