#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = get(url, headers=user_agent, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        my_data = response.json().get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return

        for post in my_data:
            print(post.get('data', {}).get('title', "None"))

    except Exception:
        print("None")

