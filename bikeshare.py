#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #---------------------------------------------------------------------------------------------------------------------
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_list = ['chicago','new york city','washington']
    while True:
        city = input("choose one of the following cities: chicago, new york city, washington \n>").lower()
        if city not in city_list:
            print("please enter one of the specified cities")
        else: break
            
    #---------------------------------------------------------------------------------------------------------------------
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_list = ['all','january','february','march','april','may','june']
    while True:
        month = input("choose a month to filter by (all, january, february, ... , june) \n>").lower()
        if month not in month_list:
            print("please enter one of the specified months")
        else: break
            
    #---------------------------------------------------------------------------------------------------------------------
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input("choose a day to filter by (all, monday, tuesday, ... sunday) \n>").lower()
        if day not in day_list:
            print("please enter one of the specified days")
        else: break
            
    #---------------------------------------------------------------------------------------------------------------------
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    #convert month string to datetime
    if month.lower() != 'all':
        month = dt.datetime.strptime(month , "%B")
        month = int(month.strftime("%m"))

    #pick weekday number from weekday dict
    if day.lower() != 'all':
        weekday_dict = {'monday':0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
        day = weekday_dict[day]

    df = pd.read_csv (r'C:\Users\kntr\Udacity\{}.csv'.format(city.replace(" ","_"))) #reading the csv file
    df['Start Time'] = pd.to_datetime(df['Start Time']) #converting the column to datetime format

    df['day of week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['month name'] = df['Start Time'].dt.month_name()
    
    if month != 'all':
        df = df[df['Start Time'].dt.month == month] #filtering the month

    if day != 'all':
        df = df[df['Start Time'].dt.weekday == day] #filtering the day

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('most common month: ', df['month name'].mode()[0])

    # display the most common day of week
    print('most common weekday: ', df['day of week'].mode()[0])

    # display the most common start hour
    print('most common hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station: ', most_used_start_station)

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('most commonly used end station: ', most_used_end_station)

    # display most frequent combination of start station and end station trip
    if 'Start Station' in df:
        df['Combination'] = df['Start Station'] + " / " + df['End Station']
        most_freq_comb_station = df['Combination'].mode()[0]
        print('most frequent combination of start station and end station trip: ', most_freq_comb_station)  
    else:
        print('there is no data for start station')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if 'Trip Duration' in df:
        total_travel_time = sum(df['Trip Duration'])
        print('total travel time is:' , total_travel_time)
    else:
        print('there is no data for travel time')
        
    # display mean travel time
    if 'Trip Duration' in df:
        mean_travel_time = df['Trip Duration'].mean()
        print('mean travel time is: ' , mean_travel_time)
    else:
        print('there is no data for travel time')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #counting the usertypes
    if 'User Type' in df:
        count_usertypes = df['User Type'].value_counts()
        print(count_usertypes)
    else:
        print('there is no data for usertype')
        
    #counting gender
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print('Male: ', count_gender['Male'])
        print('Female: ', count_gender['Female'])
    else:
        print('there is no data for gender')

    #counting the earliest birth year, latest birth year and most common birth year
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('earliest birth year is: ', earliest_birth_year)

        latest_birth_year = df['Birth Year'].max()
        print('latest birth year is: ', latest_birth_year)

        count_birth_year = df['Birth Year'].mode()[0]
        print('most frequent birth year is: ', count_birth_year)
    else:
        print('there is no data for birth year')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Prompts user to print raw data or not"""
    r = 0
    Y_or_N = 'yes'
    while Y_or_N == 'yes':
        Y_or_N = input("do you want to print raw data? \n>").lower()
        print(df.iloc[r:r+5,:])
        r+=5
 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[11]:


df = pd.read_csv (r'C:\Users\kntr\Udacity\chicago.csv')
df.iloc[0:9,:]


# In[ ]:




