import json
import requests
import time


def trigger_datasets(api_token, dataset_id, datasets):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={dataset_id}&type=discover_new&discover_by=category_url&limit_per_input=4"

    # Sending API request to trigger dataset collection
    response = requests.post(trigger_url, headers=headers, data=json.dumps(datasets))

    if response.status_code == 200:
        print("Data collection triggered successfully!")
        snapshot_id = response.json().get("snapshot_id")
        return snapshot_id if snapshot_id else print("No snapshot ID returned.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_snapshot_data(api_token, snapshot_id):
    headers = {"Authorization": f"Bearer {api_token}"}
    snapshot_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    )

    # Polling until the snapshot data is ready
    while True:
        response = requests.get(snapshot_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            print("Snapshot still processing... retrying.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        time.sleep(10)


def store_data(data, filename="amazon_bestsellers_data.json"):
    if data:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved in {filename}.")
    else:
        print("No data to store.")


if __name__ == "__main__":
    API_TOKEN = "API_TOKEN"
    DATASET_ID = "gd_l7q7dkf244hwjntr0"

    datasets = [
        {
            "url": "https://www.amazon.com/s?i=luggage-intl-ship",
            "sort_by": "Best Sellers",
            "zipcode": "10001",
        },
    ]

    # Trigger dataset collection
    snapshot_id = trigger_datasets(API_TOKEN, DATASET_ID, datasets)

    if snapshot_id:
        # Retrieve the data once the snapshot is ready
        data = get_snapshot_data(API_TOKEN, snapshot_id)
        if data:
            store_data(data)