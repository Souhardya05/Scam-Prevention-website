from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile

class TextInput(BaseModel):
    message: str

class VoiceInput(BaseModel):
    file_path: str  # This will be filled by FastAPI's FileUpload





class FakeAccountInput(BaseModel):
    name: str
    followers: int
    following: int