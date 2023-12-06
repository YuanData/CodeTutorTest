import re

import requests


def parse_counter_from(response_text: str) -> int:
    """ Extract the counter value from the response text using regular expression """
    match = re.search(r"This site has been visited (\d+) times.", response_text)
    return int(match.group(1)) if match else None


def verify_web_counter():
    url = "https://script.google.com/macros/s/AKfycbwjK27Ffh80H015YaMheExmmdfshFK1tmtz-H_fbL-jdG0TZUhlz9vv3m6Hnp8cz2QH0w/exec"

    # First API call
    response1 = requests.get(url)
    count1 = parse_counter_from(response1.text)
    print(f"First response: {response1.text}")

    # Second API call
    response2 = requests.get(url)
    count2 = parse_counter_from(response2.text)
    print(f"Second response: {response2.text}")

    # Verify if the counter has incremented
    if count2 == count1 + 1:
        print("Counter incremented by 1 as expected.")
    else:
        print("Counter did not increment as expected.")


if __name__ == '__main__':
    verify_web_counter()
