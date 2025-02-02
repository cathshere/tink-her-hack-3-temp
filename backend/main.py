from fastapi import FastAPI
from typing import List

app = FastAPI()

doctors = [
    {"name": "Dr. John Smith", "qualification": "MBBS, MD", "hospital": "City Hospital", "experience": "15 years", "availability": "9 AM - 5 PM", "rating": 4.8, "department": "Cardiologist"},
    {"name": "Dr. Alice Brown", "qualification": "MBBS, DM", "hospital": "Metro Hospital", "experience": "12 years", "availability": "10 AM - 6 PM", "rating": 4.7, "department": "Cardiologist"},
    {"name": "Dr. Robert Taylor", "qualification": "MBBS, MD", "hospital": "General Hospital", "experience": "10 years", "availability": "8 AM - 4 PM", "rating": 4.6, "department": "Cardiologist"},
    {"name": "Dr. Olivia Carter", "qualification": "MBBS, MD", "hospital": "City Hospital", "experience": "9 years", "availability": "10 AM - 5 PM", "rating": 4.7, "department": "Dermatologist"},
    {"name": "Dr. Ethan Brown", "qualification": "MBBS, MD", "hospital": "Metro Hospital", "experience": "12 years", "availability": "9 AM - 3 PM", "rating": 4.8, "department": "Dermatologist"},
    {"name": "Dr. Amelia Scott", "qualification": "MBBS, MD", "hospital": "General Hospital", "experience": "14 years", "availability": "8 AM - 4 PM", "rating": 4.9, "department": "Dermatologist"},
    {"name": "Dr. Daniel Harris", "qualification": "PhD Psychology", "hospital": "Medical Trust", "experience": "12 years", "availability": "8 AM - 3 PM", "rating": 4.8, "department": "Psychologist"},
    {"name": "Dr. Liam Bennett", "qualification": "MBBS, MS(Ortho)", "hospital": "Memorial Hospital", "experience": "14 years", "availability": "10 AM - 6 PM", "rating": 4.9, "department": "Orthologist"},
]

@app.get("/doctors/{department}")
def get_doctors(department: str):
    filtered_doctors = [doc for doc in doctors if doc["department"].lower() == department.lower()]
    return {"doctors": filtered_doctors[:3]}