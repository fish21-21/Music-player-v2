from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

AUDIO_FOLDER = "audio"

# 🎵 Get list of tracks
@app.get("/tracks")
def get_tracks():
    return os.listdir(AUDIO_FOLDER)


# 🎧 Serve actual audio file
@app.get("/audio/{filename}")
def get_audio(filename: str):
    file_path = os.path.join(AUDIO_FOLDER, filename)

    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg")

    return {"error": "File not found"}
