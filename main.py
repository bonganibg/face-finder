from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from models.find_face_request import FindFaceRequest
from services.face_finder import find_person
from services.write_to_blob import file_uploader, get_file_name
from services.write_to_file import write_to_file


def find_faces(request: FindFaceRequest):
    image_url = request.image_url
    bucket_name = request.bucket_name

    found_faces = find_person(image_url)

    for i, image in enumerate(found_faces):
        image_name = f"image_{i}.jpg"
        # write_to_file(image, image_name, bucket_name)
        file_uploader(image, image_name, bucket_name)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/find_face")
async def find_face(request: FindFaceRequest):

    find_faces(request)

    return {"message": "done"}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
