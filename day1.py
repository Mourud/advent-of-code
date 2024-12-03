import os
import requests


def main():
    url = "https://adventofcode.com/2024/day/1/input"
    cookie = os.getenv("AOC_cookie")
    headers = {"Cookie" : f"session={cookie}",
                                "User-Agent": "Python Script - Advent of Code Input Fetcher"}
    response = getResponse(url, headers)
    if response is None:
        return
    formatted_response = formatResponse(response)
    print(part1(formatted_response))
    print(part2(formatted_response))



def part1(formatted_response):
    for list in formatted_response:
        list.sort()
    distance = 0
    for i in range(len(formatted_response[0])):
        distance += abs(formatted_response[1][i] - formatted_response[0][i])
    return distance

def part2(formatted_response):
    left = formatted_response[0]
    right = formatted_response[1]
    sim = 0
    for elem_l in left:
        for elem_r in right:
            if elem_l == elem_r:
                sim += elem_l
    return sim

def getResponse(url, headers):
    try:
        response = requests.get(url, headers = headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def formatResponse(content) -> list[list]:
    numbers = content.split()
    lists = [[],[]]
    for i, number in enumerate(numbers):
        lists[i%2].append(int(number))
    return lists

print(main())