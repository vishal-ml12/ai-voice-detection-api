from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="AI Voice Detection API")

# Replace with your API key
API_KEY = "my-secret-key"

# Request model with mandatory fields
class AudioRequest(BaseModel):
    language: str
    audio_format: str
    audio_base64: str
    audio_url: Optional[str] = None  # optional

# Detect endpoint
@app.post("/detect")
def detect_audio(request: AudioRequest, x_api_key: str = Header(...)):
    # API key check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Determine audio source
    if request.audio_url:
        audio_source = request.audio_url
    else:
        audio_source = "base64_audio_received"

    # Dummy detection logic (replace with your real model logic if needed)
    return {
        "status": "success",
        "language": request.language,
        "audio_format": request.audio_format,
        "audio_source": audio_source,
        "result": "HUMAN",
        "confidence": 0.82
    }

# Health check (optional, useful for Render)
@app.get("/")
def home():
    return {"status": "API is running"}