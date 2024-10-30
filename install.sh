echo "update environment"
apt update -y

echo "install dependencies"
apt install -y git 
apt install -y python3 
apt install -y python3-pip 
apt install -y python3-venv 
apt install wget

echo "setup minio"
wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20241013133411.0.0_amd64.deb -O minio.deb
mkdir ~/minio

echo "install stuff"
apt install -y libgl1
apt install -y libglib2.0-0

echo "create virtual environment"
python3 -m venv .venv
source .venv/bin/activate

echo "install dependencies"
pip install -r requirements.txt

echo "run application"
python3 main.py
