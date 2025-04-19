from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from predict.text_predict import predict_text
from predict.voice_predict import transcribe_audio
from predict.fake_account_predict import predict_fake_account


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextInput(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Scam Detection API is running."}

@app.post("/predict_text")
async def predict_text_route(input: TextInput):  # renamed to avoid conflict
    text = input.text
    if "congratulations" in text.lower():
        return {"result": "Scam"}
    else:
        return {"result": "Not Scam"}


@app.post("/predict_voice")
async def predict_from_voice(file: UploadFile = File(...)):
    file_location = "temp_audio.wav"
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    transcription = transcribe_audio(file_location)

    if transcription.startswith("Error"):
        return {"error": transcription}

    prediction = predict_text(transcription)
    return {
        "transcription": transcription,
        "prediction": prediction
    }



@app.post("/predict_fake_account")
async def fake_account(
    name: str = Form(...),
    followers: int = Form(...),
    following: int = Form(...),
    file: UploadFile = File(...)
):
    result = predict_fake_account(name, followers, following, file)
    return result