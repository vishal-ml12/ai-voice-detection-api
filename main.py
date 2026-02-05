from fastapi import FastAPI
from pydantic import BaseModel
import base64, tempfile

from audio_utils import extract_features
from model import model

app = FastAPI()

class AudioRequest(BaseModel):
    audio_base64: str

@app.post("/detect")
def detect_voice(req: AudioRequest,):
    audio_bytes = base64.b64decode(req.audio_base64)

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(audio_bytes)
        path = f.name

    features = extract_features(path)
    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0])
    print(len(features))

    return {
        "result": "AI_GENERATED" if prediction == 1 else "HUMAN",
        "confidence": round(float(confidence), 2)
    }

