# Tester Matching WebApp
Tester-matching algorithm is one of the major features of the Applause platform. When particular criteria are selected according to a Customer's needs, this algorithm comes up with a list of testers, sorted by the most experienced, using a stored tester database. This repository holds all the codes for a Python (Flask)-based web application to demonstrate the tester-matching algorithm. At its heart, this app matches given selection criteria with the database, queries relevant results, sorts them by their experience, and displays them in a tabulated manner.
 <br>
 <br>
 ## About the Data
 The data used to query from is stored in 5 different .csv files.
 <br>
```
1. bugs.csv: CSV of all the Bugs filed by a Tester. Each row corresponds to a single Bug filed by a Tester 
and contains the Tester and the Device the Bug was reported on.

2. devices.csv: CSV of all available Devices. Each row corresponds to a single Device - This is all the 
possible Device types a Tester can have.

3. tester_device.csv: CSV mapping Testers to Devices. Each row maps a Tester to a Device.

4. testers.csv: CSV of of all Testers. Each row corresponds to a Tester.
```
## Querying Tool and Methodology
Pandas module of python has been chosen for querying and sort. Querying speed of Pandas is usually comparable to SQL for datasets lesser than about a million in size. In addition, it is more convenient to use Pandas for flat files like .csv since it avoids the hassle of creating a database and storing tables. Pandas is sufficiently fast for the given data size, and also allows easy datastructure manipulation in python.


## Steps to Use this WebApp

If you are a Linus/MacOS user and already have Python (version =>3.5), pip and git, run the following commands from your command line interpreter (CLI):
```bash
git clone https://github.com/dkedar7/TesterMatching
cd TesterMatching
source RunApp.sh
```

### 1. Install Python.
Install Python (version =>3.5) fom https://www.python.org/downloads/release. This app is built on is 3.7.0, so this is the recommended version. Choose your build, run the exucatable, and add python's path to the list of PATH variables. Open the command line interpreter and type 'python' to see if python's path has been added to PATH.

### 2. Get pip.
Open the CLI (Terminal on MacOS and Command Prompt on Windows. Check if pip is already installed by typing the command
'''bash
python -m pip --version
'''
If pip is not installed, you can get it from https://pip.pypa.io/en/stable/installing/. Restart the CLI.

### 3. Clone this repository.
To clone this repository from the CLI, use
```bash
git clone https://github.com/dkedar7/TesterMatching
```
You may also choose to manually download the contents of this repository in a zipped folder and then unzip the contents.

### 4. Create a virtual environment
Install ``` virtualenv ``` and create an isolated virtual environment.
```bash
cd TesterMatching
python -m pip install virtualenv
python -m virtualenv TesterMatchingApp
```
Activate this environment,
Windows:
```bash
TesterMatchingApp\Source\Activate
```
Mac:
```bash
source TesterMatchingApp/bin/activate
```

### 5. Install all required modules from requirements.txt
```bash
python -m pip install -r requirements.txt
```

### 6. Run the app
```bash
python -m flask run
```

The final app looks like this-
