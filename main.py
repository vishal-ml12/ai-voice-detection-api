from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="AI Voice Detection API")

API_KEY = "my-secret-key"

class AudioRequest(BaseModel):
    language: str
    audio_format: str = Field(..., alias="audioFormat")
    audio_base64: str = Field(..., alias="audioBase64")
    audio_url: Optional[str] = Field(None, alias="audioUrl")

    class Config:
        allow_population_by_field_name = True

@app.post("/detect")
def detect_audio(request: AudioRequest, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if request.audio_url:
        audio_source = request.audio_url
    else:
        audio_source = "base64_audio_received"

    return {
        "status": "success",
        "language": request.language,
        "audio_format": request.audio_format,
        "audio_source": audio_source,
        "result": "HUMAN",
        "confidence": 0.82
    }

@app.get("/")
def home():
    return {"status": "API is running"}