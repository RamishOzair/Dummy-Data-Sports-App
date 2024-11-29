import requests

ACCESS_TOKEN = 'a54b134669e423b692c03645b461409fa1cef14c'  # The retrieved access token
ACTIVITIES_URL = 'https://www.strava.com/api/v3/athlete/activities'

def get_activities():
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    response = requests.get(ACTIVITIES_URL, headers=headers)
    if response.status_code != 200:
        print(response.json())  # Print the error message from the response
        return {'error': 'Failed to fetch activities'}
    activities = response.json()
    return activities

if __name__ == '__main__':
    activities = get_activities()
    print(activities)

