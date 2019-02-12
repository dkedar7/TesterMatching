# Tester Matching WebApp
Tester-matching algorithm is one of the major features of the Applause platform. When particular criteria are selected according to a Customer's needs, this algorithm comes up with a list of testers, sorted by the most experienced, using a stored tester database. This repository holds all the codes for a Python (Flask)-based web application to demonstrate the tester-matching algorithm. At its heart, this app matches given selection criteria with the database, queries relevant results, sorts them by their experience, and displays them in a tabulated manner.

For example, if a customer is interested in users from 'US' and 'GB' only, and with experience with testing in 'iPhone 5', 'Galaxy S4', and 'HTC One', then running the code:
```python
from app.query import query
result = query(['US','GB'],['iPhone 5', 'Galaxy S4','HTC One'])
print (result)
```
returns

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
      <th>Number of Bugs Tested</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Miguel</td>
      <td>Bautista</td>
      <td>US</td>
      <td>114</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Stanley</td>
      <td>Chen</td>
      <td>GB</td>
      <td>110</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Leonard</td>
      <td>Sutton</td>
      <td>GB</td>
      <td>106</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Darshini</td>
      <td>Thiagarajan</td>
      <td>GB</td>
      <td>104</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Michael</td>
      <td>Lubavin</td>
      <td>US</td>
      <td>99</td>
    </tr>
  </tbody>
</table>


 ## About the Data
 The data used to query from is stored in 5 different .csv files.
 
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
<br>
The following methodology has been used to do the entire querying task:
<br>
1. Query testers by the desired device(s).
\t 1.1. Find device_Ids of all devices in the desired 'device_list'.
1.2. Query tester_Ids of the testers who use these devices.
1.3. Query testers corresponding to these tester_Ids.
2. From the bugs, keep only the bugs corresponding to devices in 'device_list'.
3. Add a column to 'testers' indicate how many 'relevant_bugs' were tested by testers.
4. Query by the countries of interest.
4.1. Keep only the testers from countries in 'country_list'.
5. Sort by the number of 'relevant_bugs' tested.


## How to install and run this app

If you are a Linus/MacOS user and already have Python (version =>3.5), pip and git, run the following commands from your command line interpreter (CLI):
```bash
git clone https://github.com/dkedar7/TesterMatching
cd TesterMatching
source RunApp.sh

```

#### 1. Install Python.
Install Python (version =>3.5) fom https://www.python.org/downloads/release. This app is built on is 3.7.0, so this is the recommended version. Choose your build, run the exucatable, and add python's path to the list of PATH variables. Open the command line interpreter and type 'python' to see if python's path has been added to PATH.

#### 2. Get pip.
Open the CLI (Terminal on MacOS and Command Prompt on Windows. Check if pip is already installed by typing the command
'''bash
python -m pip --version
'''
If pip is not installed, you can get it from https://pip.pypa.io/en/stable/installing/. Restart the CLI.

#### 3. Clone this repository.
To clone this repository from the CLI, use
```bash
git clone https://github.com/dkedar7/TesterMatching
```
You may also choose to manually download the contents of this repository in a zipped folder and then unzip the contents.

#### 4. Create a virtual environment
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

#### 5. Install all required modules from requirements.txt
```bash
python -m pip install -r requirements.txt
```

#### 6. Run the app
```bash
python -m flask run
```
Copy and paste the link displayed on the CLI in a browser. You can select your criteria and get the queried table displayed on the side.

<img src="https://github.com/dkedar7/TesterMatching/blob/master/AppLayout.png" alt="App Layout">

