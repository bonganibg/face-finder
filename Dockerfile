version: "3.8"

services:
  minio:
    image: minio/minio:latest
    container_name: minio
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ./minio-data:/data
      - "./minio-config:/root/.minio"
  face_finder:
    build: .
    container_name: face_finder
    ports: 
      - "8000:8000"
    env_file: 
      - .env
    depends_on:
      - minio

