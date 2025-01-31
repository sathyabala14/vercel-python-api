from fastapi import FastAPI, Query
import json
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Check if JSON file exists before loading
json_file = "q-vercel-python.json"
if os.path.exists(json_file):
    with open(json_file, "r") as file:
        student_data = json.load(file)
else:
    student_data = {}  # Set default empty dictionary

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    if not name:
        return {"error": "No name provided"}

    marks = [student_data.get(n, "Not Found") for n in name]
    return {"marks": marks}
