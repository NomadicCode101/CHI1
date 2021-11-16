import requests

url = "https://mercury-uat.phonepe.com/%20v4/debit"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers)

print(response.text)