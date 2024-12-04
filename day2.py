from networkx import difference
from input_fetcher import fetch_input


def main():
    response = fetch_input(__file__)
    if response is None:
        return
    print(part1(response))

def part1(response):
    total = 0
    reports = response.splitlines()
    for report in reports:
        levels = report.split()
        prev_level = int(levels[0])
        prev_difference = int(levels[1]) - prev_level
        for level in levels[1:]:
            level = int(level)
            difference = level - prev_level
            if prev_difference * difference < 0:
                total += 1
                break
            if difference == 0 or abs(difference) > 3:
                total += 1
                break
            prev_level = level
            prev_difference = difference
    return len(reports) - total


main()