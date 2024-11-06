import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')

submission_ids = r.json()

json.dump(submission_ids, outfile)


url = 'https://hacker-news.firebaseio.com/v0/item/42067265.json'
r = requests.get(url)

outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile, indent=4)


for subid in submission_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{subid}.json'
    r = requests.get(url)
    response_dict = r.json()


    try:
        print(f'Title: {response_dict['title']}')
        print(f'URL: {response_dict['url']}')
        print(f'Score: {response_dict['score']}')
        print(f'Descendants: {response_dict['descendants']}')
    except:
        pass

    input()