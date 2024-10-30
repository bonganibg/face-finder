from services.face_finder import find_person
from services.write_to_blob import file_uploader, get_file_name
from services.write_to_file import write_to_file

if __name__ == "__main__":
    image_url = "https://images.ctfassets.net/6bj3xgxxnl0k/1nmRcnMDePlT1JY3UVfXOf/cbcd22ed3b3dfe9affa432031b911145/AdobeStock_472119374.jpeg?fm=webp"

    output = find_person(image_url)
    bucket_name = get_file_name(image_url)

    count = 1    
    for face in output:
        image_name = f"image_{count}.jpg"
    
        # file_uploader(face, image_name, bucket_name)
        write_to_file(face, image_name, "images")
        count += 1


