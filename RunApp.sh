cd TesterMatching
python -m pip install virtualenv
python -m virtualenv TesterMatchingApp
source TesterMatchingApp/bin/activate
python -m pip install -r requirements.txt
python -m flask run
