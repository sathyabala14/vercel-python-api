from fastapi import FastAPI, Query
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON Data
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    if not name:
        return {"error": "No name provided"}
    
    marks = [student_data.get(n, "Not Found") for n in name]
    
    return {"marks": marks}

