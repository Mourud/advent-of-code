from networkx import difference
from input_fetcher import fetch_input


def main():
    response = fetch_input(__file__)
    if response is None:
        return
    print(part1(response))
    print(part2(response))


def part1(response):
    reports = response.splitlines()
    bad_reports = find_bad_reports(reports)
    return len(reports) - len(bad_reports)

def find_bad_reports(reports):
    bad_reports = []
    for report in reports:
        if(is_bad_report(report)):
            bad_reports.append(report)
    return bad_reports

def is_bad_report(report):
    levels = report.split()
    prev_level = int(levels[0])
    prev_difference = int(levels[1]) - prev_level
    for level in levels[1:]:
        level = int(level)
        difference = level - prev_level
        if prev_difference * difference < 0 or difference == 0 or abs(difference) > 3:
            return True
        prev_level = level
        prev_difference = difference
    return False
        
def part2(response):
    fixed_reports = 0
    reports = response.splitlines()
    bad_reports = find_bad_reports(reports)
    for bad_report in bad_reports:
        levels = bad_report.split()
        for i, level in enumerate(levels):
            new_report = levels[:i] + levels[i+1:]
            new_report = " ".join(new_report) 
            # print(bad_report)
            if not is_bad_report(new_report):
                fixed_reports += 1
                break
    return len(reports) - len(bad_reports) + fixed_reports
        



main()
