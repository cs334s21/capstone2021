import os
import time
from datetime import datetime, timedelta
import requests
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


def make_request(url, params):
    response = requests.get(url, params=params)
    if response.status_code == 429:
        print("Finished with 1000 calls")
        print("I gonna nap an hour. bye, bye")
        time.sleep(3600)
        print("Hey, I am back to work!!")
        response = requests.get(url, params=params)
    response.raise_for_status()
    return response


def transform_date(response):
    """Expects date in this format yyyy-mm-dd hh:mm:ss"""
    date = response.json()['data'][-1]['attributes']['lastModifiedDate']
    date = date.replace("T", " ").replace("Z", "")

    return str(datetime.fromisoformat(date) + timedelta(hours=-4))


def update_filter(url, params):
    response = make_request(url, params)
    response.raise_for_status()
    params["filter[lastModifiedDate][ge]"] = transform_date(response)


def write_endpoints(endpoint):
    params = {
        "api_key": API_TOKEN,
        "sort": 'lastModifiedDate',
        "page[size]": 250
    }

    folder_path = f'regulations/{endpoint}'
    if not os.path.exists(f"{folder_path}"):
        os.makedirs(folder_path)

    url = f'https://api.regulations.gov/v4/{endpoint}'

    results = make_request(url, params=params)
    total_elements = int(results.json()['meta']['totalElements'])

    output_number = 0
    while total_elements > 0:
        try:
            with open(f'{folder_path}/{endpoint}_{output_number}.txt', 'w') \
                    as writer:
                print(f"{url[31:]} left to write: {total_elements}")
                for page in range(1, 21):
                    params["page[number]"] = str(page)
                    items = make_request(url, params).json()
                    for item in items['data']:
                        writer.write(f"{endpoint}/{item['id']}\n")
                        total_elements -= 1
                update_filter(url, params)
                output_number += 1
        except IndexError:
            print("ran out of items to download")


def write_all_ids():
    write_endpoints('dockets')
    write_endpoints('documents')
    write_endpoints('comments')


if __name__ == "__main__":
    write_all_ids()
