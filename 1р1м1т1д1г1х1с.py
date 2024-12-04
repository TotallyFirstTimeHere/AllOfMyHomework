import pandas as pd

# Constants for time conversions
second_in_minute = 60
second_in_hour = 3600
second_in_day = 86400
second_in_week = 604800
second_in_month = 2592000  # Approximate month in seconds (30 days)
second_in_year = 31536000  # Approximate year in seconds (365 days)


# Conversion function
def precise_convert_time(seconds):
    years = seconds // second_in_year
    seconds %= second_in_year

    months = seconds // second_in_month
    seconds %= second_in_month

    weeks = seconds // second_in_week
    seconds %= second_in_week

    days = seconds // second_in_day
    seconds %= second_in_day

    hours = seconds // second_in_hour
    seconds %= second_in_hour

    minutes = seconds // second_in_minute
    seconds %= second_in_minute

    result = []
    if years > 0:
        result.append(f"{years}р")
    if months > 0:
        result.append(f"{months}м")
    if weeks > 0:
        result.append(f"{weeks}т")
    if days > 0:
        result.append(f"{days}д")
    if hours > 0:
        result.append(f"{hours}г")
    if minutes > 0:
        result.append(f"{minutes}х")
    if seconds > 0:
        result.append(f"{seconds}с")

    return "".join(result)


# Example data structure with values in seconds
data_in_seconds = {
    (38, 17): 2097152,
    (38, 19): 524288,
    (38, 21): 131072,
    (40, 17): 8388608,
    (40, 19): 2097152,
    (40, 21): 524288,
    (42, 17): 33554432,
    (42, 19): 8388608,
    (42, 21): 2097152,
    (44, 17): 67108864,
    (44, 19): 33554432,
    (44, 21): 8388608,
}

# Convert seconds to formatted time
converted_data = {(n, l): precise_convert_time(seconds) for (n, l), seconds in data_in_seconds.items()}

# Creating a DataFrame to represent the table
df = pd.DataFrame.from_dict(
    {(n, l): converted_data[(n, l)] for (n, l) in converted_data},
    orient='index'
).unstack().T

df.index.names = ['N', 'L']
df.columns = ["L=17", "L=19", "L=21"]

# Displaying the table
print(df)
