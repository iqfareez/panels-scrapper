import os
import requests
import time

# Load json data
url = 'https://storage.googleapis.com/panels-api/data/20240916/media-1a-i-p~s'

response = requests.get(url)
data = response.json()['data']

# List all HD wallpapers
hd_links = [v['dhd'] for v in data.values() if 'dhd' in v]

print("Links fetched. Total: ", len(hd_links))

# If you want to limit the amount of data fetched, uncomment the below line
# hd_links = hd_links[:5] # Only take first 5 wallpapers

# Download all HD wallpapers
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i, link in enumerate(hd_links, start=1):
    print(f"Downloading {i} of {len(hd_links)}")
    start_time = time.time()
    r = requests.get(link)
    end_time = time.time()
    link_filename = link.split('?')[0].split('/')[-1].replace('~', '-')
    with open(os.path.join(output_folder, link_filename), 'wb') as f:
        f.write(r.content)
    print(f"{link_filename} saved. {end_time - start_time:.2f} s")

