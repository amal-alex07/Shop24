import urllib.parse
import requests
import json

data = { "customer_id":"187179000000084166",
         "date":"2019-10-23",
         "line_items":
            [
                {
                "item_id":"187179000000089007",
                "rate":33.92,
                "quatntity":"1.00",
                }
            ]
        }

headers = {"content-type": "application/x-www-form-urlencoded;charset=UTF-8","Authorization":"Zoho-authtoken 19ae38d713e09a166f2d4dc180273945","organization_id": "60002546970"}
url = "https://inventory.zoho.in/api/v1/salesorders"
r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.json())