# Import Pandas
import pandas as pd

# Import the required files
bugs = pd.read_csv("Data/bugs.csv")
devices = pd.read_csv('Data/devices.csv')
tester_device = pd.read_csv('Data/tester_device.csv')
testers = pd.read_csv('Data/testers.csv')

testers['BugsTested'] = bugs.groupby('testerId').agg({'bugId':'count'}).astype(int).values

def query(country_list,device_list):
    '''
    Function queries the database according to specified selections.

    Parameters
    ----------
    1. country_list: (list) List of country names (list containing any
                    combinations of 'JP', 'US', 'GB', and 'all_countries'.

    2. device_list: (list) List of device names (list containing any
                    combinations of device name string and 'all_devices'.

    Returns
    ----------
    query_by_country: (Pandas Dataframe) Dataframe of queries rows from the
                    database. Columnd are 'firstName','lastName','country', and
                    'Number of bugs tested on selected device(s)'.

    Example
    ----------
    >>> query(['US','GB'],['HTC One','iPhone 4'])
    >>>
          First Name    Last Name Country  Number of Bugs Tested
    1     Taybin       Rutkin      US                     66
    2   Darshini  Thiagarajan      GB                     30
    3     Miguel     Bautista      US                     23
    4    Michael      Lubavin      US                     17


    '''
    # 1. Query by device(s)

    # If 'device_list' contains 'all_devices', select all rows
    if 'all_devices' in device_list:
        query_by_device = testers[['testerId','firstName','lastName','country']]

    # If 'device_list' does not contain 'all_devices', select the relevant rows
    else:
        # 1.1. Find device_Ids of all devices in 'device_list'
        device_id = devices[devices.description.isin(device_list)].deviceId.tolist()

        # 1.2. Query tester_Ids of the testers who use these devices
        testerIds_using_devices = tester_device[tester_device.deviceId.isin(device_id)].testerId.unique()

        # 1.3. Query testers corresponding to these tester_Ids
        query_by_device = testers[testers.testerId.isin(testers_using_devices)][['testerId',
                                                                                 'firstName',
                                                                                 'lastName',
                                                                                 'country']]

    # 2. Keep only the bugs corresponding to devices in 'device_list'.
    relevant_bugs = bugs[bugs.deviceId.isin(device_id)]

    # 3. Add an integer column to indicate how many 'relevant_bugs' were tested by testers.
    query_by_device['BugsTested'] = relevant_bugs.groupby('testerId').agg({'bugId':'count'}).astype(int).values


    # 4. Query by country/ies

    # If 'country_list' contains 'all_countries', select all rows
    if 'all_countries' in country_list:
        country_list = testers.country.unique()
        query_by_country = query_by_device[['firstName','lastName','country','BugsTested']].sort_values('BugsTested',ascending=False)

    # If 'country_list' does not contain 'all_countries', select specific rows
    else:

        # 4.1. Keep only the testers from countries in 'country_list'
        testers_concerned_countries = query_by_device[query_by_device.country.isin(country_list)]

        # 5. Sort by the number of 'relevant_bugs' tested
        query_by_country = testers_concerned_countries[['firstName','lastName','country','BugsTested']].sort_values(
            'BugsTested',ascending=False)

    # Assign serial numbers to the final table
    query_by_country.index = range(1,len(query_by_country)+1)

    # Rename columns
    query_by_country.columns = ['First Name','Last Name','Country','Number of Bugs Tested']
