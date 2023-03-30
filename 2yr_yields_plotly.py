import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint and parameters
url = 'https://api.stlouisfed.org/fred/series/observations'
params = {
    'series_id': 'GB2YR',
    'api_key': 'YOUR_API_KEY_HERE',
    'observation_start': 'START_DATE_HERE',
    'observation_end': 'END_DATE_HERE',
    'frequency': 'd'
}

# Make a request to the API and parse the response as a Pandas DataFrame
response = requests.get(url, params=params)
df = pd.read_json(response.content)['observations']

# Convert the date string to a datetime object and set it as the index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Create a line plot of the data
plt.plot(df['value'])

# Customize the plot
plt.title('UK 2-Year Bond Yields')
plt.xlabel('Date')
plt.ylabel('Yield (%)')
plt.show()
