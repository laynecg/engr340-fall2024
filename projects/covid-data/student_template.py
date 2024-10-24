import sys
import pandas as pd
import numpy as np
from numpy.ma.core import argmax


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(df):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    ### Grabbing all the data where the county is Rockingham, Virginia and Harrisonburg City, Virginia
    ### We need to differentiate between Virginia and other states
    rockingham = df[df['county'] == 'Rockingham']
    rockinghamVA = rockingham[rockingham['state'] == 'Virginia']
    harrisonburg = df[df['county'] == 'Harrisonburg city']
    harrisonburgVA = harrisonburg[harrisonburg['state'] == 'Virginia']
    ### Grabbing date data
    harrisonburg_dates_array = harrisonburgVA["date"].to_numpy()
    rockingham_dates_array = rockinghamVA["date"].to_numpy()
    print("The first Covid case for Harrisonburg was on",harrisonburg_dates_array[0])
    print("The first Covid case for Rockingham County was on" ,rockingham_dates_array[0])
    return

def second_question(df):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    ### Grabbing data for Rockingham, Virginia
    rockingham = df[df['county'] == 'Rockingham']
    rockinghamVA = rockingham[rockingham['state'] == 'Virginia']
    rockingham_dates_array = rockinghamVA["date"].to_numpy()
    ### Turning the cases column for Rockingham into an array
    rockingham_cases = rockinghamVA["cases"].to_numpy()
    ### Finding case difference
    max_cases_R = np.diff(rockingham_cases)
    ### Finds the location of the maximum difference
    max_cases_R_date = np.argmax(max_cases_R)+1
    ### print(max_cases_R_date)
    ### Referencing the index of the argument to get the date
    print("The greatest number of new daily cases in R. County was on" ,rockingham_dates_array[max_cases_R_date])

    ### Grabbing data for Harrisonburg, Virginia
    harrisonburg = df[df['county'] == 'Harrisonburg city']
    harrisonburgVA = harrisonburg[harrisonburg['state'] == 'Virginia']
    harrisonburg_dates_array = harrisonburgVA["date"].to_numpy()
    ### Turning the cases column into an array
    harrisonburg_cases = harrisonburgVA["cases"].to_numpy()
    ### Finding case difference between elements
    max_cases_H = np.diff(harrisonburg_cases)
    ### Finds the location of the maximum difference; adding 1 to shift the day back to the maximum
    max_cases_H_date = np.argmax(max_cases_H)+1
    ### print(max_cases_H_date)
    ### Referencing the index of the argument to get the date
    print("The greatest number of new daily cases in Hburg was on" ,harrisonburg_dates_array[max_cases_H_date])

    return

def third_question(df):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    ### Grabbing data for Rockingham, Virginia
    rockingham = df[df['county'] == 'Rockingham']
    rockinghamVA = rockingham[rockingham['state'] == 'Virginia']
    rockingham_dates_array = rockinghamVA["date"].to_numpy()
    ### Turning the cases column for Rockingham into an array
    rockingham_cases = rockinghamVA["cases"].to_numpy()

    ### Grabbing data for Harrisonburg, Virginia
    harrisonburg = df[df['county'] == 'Harrisonburg city']
    harrisonburgVA = harrisonburg[harrisonburg['state'] == 'Virginia']
    harrisonburg_dates_array = harrisonburgVA["date"].to_numpy()
    ### Turning the cases column into an array
    harrisonburg_cases = harrisonburgVA["cases"].to_numpy()

    ### creating an empty list
    seven_day_R = []
    ### Writing a for loop to find the 7 day maximum for Rockingham County; -7 ends the iterating 7 elements before the end
    for i in range(len(rockingham_cases)-7):
        ### finding the difference between an element and the element 6 away
        seven_day_sum_R = rockingham_cases[i+6]-rockingham_cases[i]

        ### adding element to the end of the list
        seven_day_R.append(seven_day_sum_R)
    maximal_period_R = argmax(seven_day_R)+1
    print("The greatest 7-day period in Rockingham County started on" ,rockingham_dates_array[maximal_period_R], "and ended on" ,rockingham_dates_array[maximal_period_R+6])

    seven_day_H = []
    ### Writing a for loop to find the 7 day maximum for Harrisonburg
    for j in range(len(harrisonburg_cases)-7):
        ### finding the difference between an element and the element 6 away
        seven_day_sum_H = harrisonburg_cases[j+6]-harrisonburg_cases[j]
        ### adding element to the end of the list
        seven_day_H.append(seven_day_sum_H)
    maximal_period_H = argmax(seven_day_H)+1
    print("The greatest 7-day period in Harrisonburg started on" ,harrisonburg_dates_array[maximal_period_H], "and ended on" ,harrisonburg_dates_array[maximal_period_H+6])
    return

if __name__ == "__main__":
    #data = parse_nyt_data('us-counties.csv')

    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')
    df = pd.read_csv('us-counties.csv')

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(df)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(df)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(df)


