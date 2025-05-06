set -e
[[ -d env ]] || python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt pyinstaller
[[ -f robot_daemon/__main__.py ]] || printf 'from robot_daemon.main import main\nmain()\n' > robot_daemon/__main__.py
PATCH='import pathlib, sys
BASE = pathlib.Path(getattr(sys, "_MEIPASS", pathlib.Path(__file__).parent.parent))'
grep -q '_MEIPASS' robot_daemon/config.py || sed -i "1 a $PATCH" robot_daemon/config.py
rm -rf build dist robot_daemon.spec
pyinstaller --onefile --name robotd --add-data config.yaml:. --paths "$(pwd)" robot_daemon/__main__.py
echo
echo "./dist/robotd ready"
