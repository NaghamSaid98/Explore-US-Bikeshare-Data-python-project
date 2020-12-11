import time
import pandas as pd
import numpy as np

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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("would you like to see data for chicago,new york city or washington?:").strip().lower())

        if city not in CITY_DATA:
            print("that\'s not a valid city")
        else:
            break    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("choose a month(january:june) to filter data with or choose (all) for all months:").strip().lower())

        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("that\'s not a valid month.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("choose a day to filter data with or choose all for all days:").strip().lower())

        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("that\'s not a valid day.")
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("the most common month is:",common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("the most common day is:",common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print("the most common hour is:",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("the most common start station is:",common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("the most common end station is:",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+' '+df['End Station']
    most_common_combination = df['combination'].value_counts().idxmax()
    print("the most common combination of start station and end station trip is:",most_common_combination)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time:", total_travel_time)
    
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("mean travel time:", avg_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user = df['User Type'].value_counts()
    print("\ncounts of user types: \n",user)
    
    # TO DO: Display counts of gender
    if city != 'washington':
        
        gender =df['Gender'].value_counts()
        print("\ncounts of user gender:\n",gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print("earliest year :",earliest)
    
        most_recent = df['Birth Year'].max()
        print(" most recent year :",most_recent)
    
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print("most common year :",most_common_year)      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    count=0
    while True:
        
        data = input('Would you like to see some raw data? Enter yes or no.\n').strip().lower()
        if data == 'yes':
            print(df[count:count+5])
            count += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
