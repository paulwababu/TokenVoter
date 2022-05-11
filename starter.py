import  urllib.request
from voter import *
import concurrent.futures
import json


def main():
    with concurrent.futures.ThreadPoolExecutor(100) as executor:
        futures = []
        url = "https://a24f-105-160-107-214.ngrok.io/credentials_json"
        response = urllib.request.urlopen(url)
        emailJson = json.loads(response.read())
        for credentials in emailJson:
            email = credentials["email"] + '@vedsredec.com'
            password = credentials["password"]
            futures.append(executor.submit(Coinsniper, f"{email}:{password}"))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())