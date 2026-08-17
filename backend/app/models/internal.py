from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class Participant(BaseModel):
    participant_id: str


class Room(BaseModel):
    room_code: str = Field(min_length=6, max_length=6)
    participants: List[Participant] = []
    created_at: datetime
