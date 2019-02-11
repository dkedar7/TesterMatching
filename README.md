# TesterMatching
Tester-matching algorithm is one of the major features of the Applause platform. When particular criteria are selected according to a Customer's needs, this algorithm comes up with a list of testers, sorted by the most experienced, using a stored tester database. This repository holds all the codes for a Python (Flask)-based web application to demonstrate the tester-matching algorithm. At its heart, this app matches given selection criteria with the database, queries relevant results, sorts them by their experience, and displays them in a tabulated manner.
 <br>
 <br>
 ## About the Data
 The data used to query from is stored in 5 different .csv files.
 <br>
```
1. bugs.csv: CSV of all the Bugs filed by a Tester. Each row corresponds to a single Bug filed by a Tester and contains the Tester and the Device the Bug was reported on.
2. devices.csv: CSV of all available Devices. Each row corresponds to a single Device - This is all the possible Device types a Tester can have.
3. tester_device.csv: CSV mapping Testers to Devices. Each row maps a Tester to a Device.
4. testers.csv: CSV of of all Testers. Each row corresponds to a Tester.
```
## Querying Tool and Methodology
Pandas module of python has been chosen for querying and sort. Querying speed of Pandas is usually comparable to SQL for datasets lesser than about a million in size. In addition, it is more convenient to use Pandas for flat files like .csv since it avoids the hassle of creating a database and storing tables. Pandas is sufficiently fast for the given data size, and also allows easy datastructure manipulation in python.


## Steps to Use this WebApp
### 1. Install Python.
Install Python (version =>3.5). This app is built on is 3.7.0, so this is the recommended version.
