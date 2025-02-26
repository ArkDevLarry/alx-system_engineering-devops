#!/usr/bin/python3
"""Recursive function to fetch all hot post titles from a subreddit"""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Recursively fetches hot post titles from a given subreddit.

    Args:
        subreddit (str): The subreddit name.
        hot_list (list): Accumulator list for storing post titles.
        after (str): The 'after' parameter for pagination.
        count (int): Keeps track of the number of posts retrieved.

    Returns:
        list: A list of hot post titles, or None if subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
            "User-Agent":
            "0x16-api_advanced:project:v1.0.0 (by /u/example_user)"
            }
    params = {"after": after, "count": count, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None  # Invalid subreddit or request error

        data = response.json().get("data", {})
        after = data.get("after", None)
        count += data.get("dist", 0)

        hot_list.extend(post.get("data",
                                 {}).get("title",
                                         "") for post in data.get("children",
                                                                  []))

        return recurse(subreddit, hot_list,
                       after, count) if after else hot_list

    except Exception:
        return None  # Handle cases where JSON parsing fails
