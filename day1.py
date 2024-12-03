import os
import requests

url = "https://adventofcode.com/2024/day/1/input"
cookie = os.getenv("AOC_cookie")
headers = {"Cookie" : f"session={cookie}",
                            "User-Agent": "Python Script - Advent of Code Input Fetcher"}
try:
    response = requests.get(url, headers = headers)
    response.raise_for_status()
    file_content = response.text
    for line in file_content
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")