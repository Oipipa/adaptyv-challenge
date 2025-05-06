set -e
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo
echo "Start the daemon with: env/bin/python -m robot_daemon"
