#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Check if the subreddit is valid
        if response.status_code != 200:
            print(None)
            return

        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        posts = data.get('data', {}).get('children', [])
        for post in posts[:10]:
            title = post.get('data', {}).get('title', 'No Title')
            print(title)

    except Exception as e:
        print(None)

# Example usage
top_ten('python')
