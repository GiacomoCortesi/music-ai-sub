from pydantic import BaseModel
from datetime import datetime

class File(BaseModel):
    video_name: str
    video_id: str
    video_url: str
    image_url: str
    upload_date: datetime
    video_id: str
    video_path: str
    image_path: str