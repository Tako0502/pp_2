# import os

# def get_content_lines(filename):
#         with open(filename, 'r') as file:
#             for line in file:
#                 yield line
# def write_list_to_file(filename, my_list):
#         with open(filename, 'w') as file:
#             for item in my_list:
#                 file.write(str(item))
# path1 = "/Users/talanterzhan/Desktop/f1"
# path2 = "/Users/talanterzhan/Desktop/f2"
# for file in os.listdir(path1):
        
import requests

url = "https://uni-x-api.kz/your-endpoint"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,kk-KZ;q=0.8,kk;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NzA0MSwiZW1haWwiOiJ0X3llcnpoYW51bHlAa2J0dS5reiIsIm9yZ2FuaXphdGlvbklkIjoxMCwiaXNBZG1pbiI6ZmFsc2UsImlhdCI6MTcxMDMyOTYwOCwiZXhwIjoxNzEwOTM0NDA4fQ.5aKxQMHvR5363vUxZuon9sk9eZhUUHJJYG2C4uo9P_k",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://uni-x.kz",
    "Referer": "https://uni-x.kz/",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

payload = {
    "key1": "value1",
    "key2": "value2"
}

response = requests.post(url, headers=headers, json=payload)
# Checking the response
if response.status_code == 200:
    print("Request successful!")
    print("Response:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
