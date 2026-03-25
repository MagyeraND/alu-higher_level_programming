#!/usr/bin/python3
"""Sends a POST request with a letter as a search parameter."""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        r = requests.post(url, data={"q": q})
        json_dict = r.json()
        if not json_dict:
            print("No result")
        else:
            print("[{}] {}".format(json_dict.get("id"), json_dict.get("name")))
    except ValueError:
        print("Not a valid JSON")
