echo "update environment"
apt update -y

echo "install git"
apt install git -y

echo "install python"
apt install python3 -y

echo "install pip"
apt install python3-pip -y

echo "install virtualenv"
apt install python3-venv -y

echo "install stuff"
apt install libgl1-mesa-glx

echo "create virtual environment"
python3 -m venv .venv
source .venv/bin/activate

echo "install dependencies"
pip install -r requirements.txt

echo "run application"
python3 main.py
