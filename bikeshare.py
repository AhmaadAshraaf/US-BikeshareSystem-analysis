import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['january','february','march','april','may','june','all']
weekday_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
def check_user_input(user_input,input_type):
    while True:
        input_user_domain=input(user_input).lower()
        try:
            if input_user_domain in ['chicago','new york city','washington'] and input_type == 'c':
                break
            elif input_user_domain in month_list and input_type == 'm':
                break
            elif input_user_domain in weekday_list and input_type == 'd':
                break
            else:
                if input_type == 'c':
                    print("wrong input! check city input again")
                if input_type == 'm':
                    print("wrong input! check month input again")
                if input_type == 'd':
                    print("wrong input! check weekday input again")
            
        except ValueError:
            print("Oops!your input is invalid")
    return input_user_domain
            
   
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_user_input("which city you would like me to show for you chicago, new york city or washington?\n", 'c')
        # TO DO: get user input for month (all, january, february, ... , june)
    month = check_user_input("which month you would like me to show to you (all, january, february, march, april, may, june)?\n", 'm')
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_user_input("which day you would like me to show to you (all, sunday, monday, tuesday, wednesday, thursday, friday, saturday)?\n", 'd')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    loads data for the specified city and filters by month or day if applicable
    Args:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
    returns:
       df - pandas data frame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months =['january','february','march','april','may','june']
        month = months.index(month) +1
 
        df=df[df['month'] == month]
    
    if day != 'all':
              df=df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month: ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day: ", popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most_used_Start_Station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most_used_End_Station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station','End Station'])
    Most_frequent_combination_station = combination_station.size().sort_values(ascending=False).head(1)
    print("Most frequent combination of start and end station is: ", Most_frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """ Displays statistics on the total and average trip duration."""    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("types of users in data: ", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print("counts of gender are: ", df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("earliest year is: ", earliest_year)

        most_recent_year = df['Birth Year'].max()
        print("most recent year is: ", most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print("most common year is: ", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_raw_data(df):
    row = 0
    while True:
        view_data = input("\Would you like to view first 5 rows of data? for 'yes' type 'y' and for 'no' type 'n'.\n").lower()
        #row=0
        if view_data == "y" :
            print(df.iloc[row : row + 6])
            row += 6
        elif view_data == "n" :
            break
        else:
            print("Sorry! you have entered wrong input")
            
def main():
    while True:
                    city, month, day = get_filters()
                    df = load_data(city, month, day)

                    time_stats(df)
                    station_stats(df)
                    trip_duration_stats(df)
                    user_stats(df,city)
                    view_raw_data(df)

                    restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
                    if restart.lower() != 'yes':
                        break


if __name__ == "__main__":
    main()