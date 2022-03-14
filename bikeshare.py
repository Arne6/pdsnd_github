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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ['chicago', 'new york city', 'washington'] 
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    
    city = None
    while city not in cities:
        city = input("Which city would you like to see the data for? There are Chicago, New York City and Washington\n").lower()
        if city in cities:
            break
        else:
            print("Invalid Input")
        

    # get user input for month (all, january, february, ... , june)

    month = None
    while month not in months:
        month = input("Which month would you like to see the data for? - Type 'all' if you want to see data for all months\n").lower()
        if month in months:
            break
        else:
            print("Invalid Input")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = None
    while day not in days:
        day = input("Which day of the week would you like to see the data for? - Type 'all' if you want to see data for all days\n").lower()
        if day in days:
            break
        else:
            print("Invalid Input\n")
    
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
    #The Python index() method returns the index position at which an item is found in a list or 
    #a string. index() returns the lowest resulting index for the item. A ValueError is returned 
    #if the specified item does exist in the list.
    
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe / Converts first character of each word to uppercase and 
        #remaining to lowercase.
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular_month = df['month'].mode()[0]
    print('The most common month is {} \n'.format(most_popular_month))

    # display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is {} \n'.format(most_popular_day))

    # display the most common start hour
    most_popular_hour = df['hour'].mode()[0]
    print('The most common start hour is {} \n'.format(most_popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most common used start station is {} \n'.format(most_common_start))

    # display most commonly used end station
    most_common_start = df['End Station'].mode()[0]
    print('The most common used end station is {} \n'.format(most_common_start))

    # display most frequent combination of start station and end station trip
    df['StartEnd'] = df['Start Station'] + ' and ' + df['End Station']
    print('The most combination of start station and end station trip is\n{}'.format((df['StartEnd'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is {} days".format(round(int(total_time/86400)),1))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nThe average travel time is: {} minutes'.format(round(int(mean_time/60)),1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There are {} subscribers and {} customers.'.format(user_types.loc['Subscriber'],user_types.loc['Customer']))

    # Display counts of gender
    if "Gender" in df.columns:
        gender_types = df['Gender'].value_counts()
        print('There are {} males, {} females.'.format(gender_types[0],gender_types[1]))
    else:
        print('Gender column not found')

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]

        print('The earliest year of birth is {}.'.format(int(round(earliest_birth,1))))
        print('The most recent year of birth is {}.'.format(int(round(most_recent_birth,1))))
        print('The most common year of birth is {}.'.format(int(round(most_common_birth,1))))
    else:
        print('Birth column not found')
    

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw statistics for 5 individual trips."""
    question = input('\nWould you like to view individual trip data? Enter: "yes" or "no".\n').lower()
    if question not in ('yes', 'no'):
        print('you have to type in "yes" or "no"')
        raw_data(df)
    head_ind = 0
    while question == 'yes':
        print(df.iloc[head_ind:head_ind+5]) 
        head_ind += 5
        more_rows = input('\nWould you like to view five more rows? Enter: "yes" or "no".\n').lower()
        if more_rows != 'yes':
            break  
    
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