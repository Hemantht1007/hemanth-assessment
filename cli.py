import argparse
import requests
import yaml
import json

API_URL = "http://localhost:8000"


def upload_record(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)

    files = {
        'file': ('data.yaml', yaml.dump(data), 'application/x-yaml')
    }

    response = requests.post(f"{API_URL}/upload/", files=files)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error uploading record. Response: {response.text}")


def get_record(name):
    response = requests.get(f"{API_URL}/person/{name}")

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error getting record. Response: {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI client for interacting with FastAPI server")
    parser.add_argument("action", choices=["upload", "get"], help="Action to perform")
    parser.add_argument("name", nargs="?", default=None, help="Name of person record to retrieve")
    parser.add_argument("--filename", "-f", default=None, help="YAML file containing person record")

    args = parser.parse_args()

    if args.action == "upload":
        if not args.filename:
            print("Error: Filename not provided for upload action")
            exit(1)
        upload_record(args.filename)
    elif args.action == "get":
        if not args.name:
            print("Error: Name not provided for get action")
            exit(1)
        get_record(args.name)
    else:
        print(f"Error: Invalid action '{args.action}' provided")
        exit(1)

