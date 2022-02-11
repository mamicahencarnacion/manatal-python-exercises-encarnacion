import os
import requests


def get_number_of_followers(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=public_metrics"

    payload = {}
    headers = {
        "Authorization": f"Bearer {os.getenv('TWT_BEARER')}",
        "Content-Type": "application/json",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()

    if response_json.get("data"):
        return response_json["data"]["public_metrics"]["followers_count"]
    raise Exception(f"Cannot get number of followers for {username}")


if __name__ == "__main__":
    username = input("Input Twitter username: ")

    number_of_followers = get_number_of_followers(username=username)
    print(f"{username} has {number_of_followers or 0} followers.")
