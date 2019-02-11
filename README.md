# TesterMatching
Tester-matching algorithm is one of the major features of the Applause platform. When particular criteria are selected according to a Customer's needs, this algorithm comes up with a list of testers, sorted by the most qualified, using a stored tester database. This repository holds the code for a Python (Flask)-based web application to demonstrate the tester-matching algorithm. At its heart, this app matches given selection criteria with the database, queries relevant results, sorts them by their qualifications, and displays them in a tabulated manner.
 <br>
 <br>
 ## About the data
 The data used to query from is stored in 5 different .csv files.
 <br>
 '''
1. bugs.csv: CSV of all the Bugs filed by a Tester. Each row corresponds to a single Bug
filed by a Tester and contains the Tester and the Device the Bug was reported on.
<br>
2. devices.csv: CSV of all available Devices. Each row corresponds to a single Device -
This is all the possible Device types a Tester can have.
<br>
3. tester_device.csv: CSV mapping Testers to Devices. Each row maps a Tester to a Device.
<br>
4. testers.csv: CSV of of all Testers. Each row corresponds to a Tester.
'''

```bash
import numpy as np
```
