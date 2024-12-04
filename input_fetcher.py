import os
import requests

def fetch_input(filename):
    stripped_filename = os.path.splitext(os.path.basename(filename))[0]
    day = stripped_filename.split("day")[1]
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookie = os.getenv("AOC_cookie")
    headers = {"Cookie" : f"session={cookie}",
                                "User-Agent": "Python Script - Advent of Code Input Fetcher"}
    try:
        response = requests.get(url, headers = headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None