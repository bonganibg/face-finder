from pydantic import BaseModel

class FindFaceRequest(BaseModel):
    image_url: str
    bucket_name: str
    