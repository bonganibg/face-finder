FROM python:3.12-slim-buster
RUN apt install -y libgl1 /
    apt install -y libglib2.0-0
RUN apt-get update / 
    apt install -y python3-pip

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "main.py"]
