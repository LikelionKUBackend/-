import requests

google_api_key="AIzaSyBHdscrgCv920Tx5-TfqHoqn_cp4lRD0IQ"
request_url=f"https://www.googleapis.com/youtube/v3/search?key={google_api_key}" \
            f"&textFormat=plainText&part=snippet&q=딩고뮤직"
json_data=requests.get(request_url)
json_data=json_data.json()
print(json_data["items"][0]['snippet']['title'])