echo "update environment"
apt update -y

echo "install python"
apt install python3 -y

echo "install pip"
apt install python3-pip -y

echo "install virtualenv"
apt install python3-venv -y

echo "install stuff"
apt install libgl1-mesa-glx

