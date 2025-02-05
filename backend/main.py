from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from pydantic import BaseModel
from typing import List

# MongoDB connection setup
uri = "mongodb+srv://Miliya27:miliya00hlo@cluster0.qytcg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["doc-review"]
collection = db["details"]

# FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change to specific domain if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Pydantic model for doctor data
class Doctor(BaseModel):
    doctor_id: str  # New field for MongoDB ObjectId
    hospital: str
    name: str
    department: str
    qualification: str
    experience: int
    availability: str
    rating: float
    contact: str

# Route to add a new doctor with all required details
@app.post("/doctors/")
async def add_doctor(doctor: Doctor):
    doctor_dict = doctor.dict()
    result = collection.insert_one(doctor_dict)
    return {"id": str(result.inserted_id), "message": "Doctor added successfully"}


# Route to get all doctors
@app.get("/doctors/", response_model=List[Doctor])
async def get_all_doctors():
    doctors = []
    for doc in collection.find():
        # Add new field doctor_id with the same value as _id
        doc["doctor_id"] = str(doc["_id"])
        doctors.append(doc)
    
    return doctors
# Route to get a specific doctor by ID
@app.get("/doctors/{doctor_id}")
async def get_doctor(doctor_id: str):
    try:
        doctor = collection.find_one({"_id": ObjectId(doctor_id)})
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctor["_id"] = str(doctor["_id"])
        return doctor
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid doctor ID")
