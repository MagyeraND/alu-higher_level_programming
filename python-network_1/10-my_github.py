#!/usr/bin/python3
"""Uses GitHub API and Basic Authentication to display user ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=(user, pwd))
    try:
        json_dict = r.json()
        print(json_dict.get("id"))
    except ValueError:
        print("None")
