from pydantic import BaseModel, Field


class CreateRoomResponse(BaseModel):
    room_code: str = Field(
        min_length=6,
        max_length=6,
        description="Unique Room code",
    )


class JoinRoomRequest(BaseModel):
    room_code: str = Field(
        min_length=6,
        max_length=6,
        description="Room code to join",
    )


class JoinRoomResponse(BaseModel):
    status: bool
    message: str
