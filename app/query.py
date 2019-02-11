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
    1. final_query: (Pandas Dataframe) Dataframe of queries rows from the
                    database. Columnd are 'firstName','lastName','country', and
                    'Number of bugs tested on selected device(s)'.

    Example
    ----------
    >>> query(['US','GB'],['HTC One','iPhone 4'])
    >>> Returns dataframe of all relevant rows, and corresponding 'firstName',
    'lastName', 'country', and 'Number of bugs tested on selected device(s)'.

    '''
    # Query by device(s)

    # If 'device_list' contains 'all_devices', select all rows
    if 'all_devices' in device_list:
        query_by_device = testers[['testerId','firstName','lastName','country','BugsTested']]

    # If 'device_list' does not contain 'all_devices', select the relevant rows
    else:
        # Find device_Ids of all devices in 'device_list'
        device_id = devices[devices.description.isin(device_list)].deviceId.tolist()

        # Query those users who use these devices
        query_by_device = testers[['testerId','firstName','lastName','country','BugsTested']].iloc[
        tester_device[tester_device.deviceId.isin(device_id)].testerId.unique()-1,:]

    # Query by country/ies

    # If 'country_list' contains 'all_countries', select all rows
    if 'all_countries' in country_list:
        country_list = testers.country.unique()
        final_query = query_by_device[['firstName',
                                       'lastName',
                                       'country',
                                       'BugsTested']].sort_values('BugsTested',ascending=False)

    # If 'country_list' does not contain 'all_countries', select specific rows
    else:
        final_query = query_by_device[query_by_device.country.isin(country_list)][['firstName',
                                                               'lastName',
                                                                'country',
                                                              'BugsTested']].sort_values('BugsTested',
                                                                                        ascending=False)

    # Assign serial numbers to the final table
    final_query.index = range(1,len(final_query)+1)

    # Rename columns
    final_query.columns = ['First Name','Last Name','Country','Number of Bugs Tested']

    return final_query
