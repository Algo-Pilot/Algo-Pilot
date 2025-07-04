import requests
from bs4 import BeautifulSoup
import re

beecrowc_id = '1153590'  # ✅ Your Beecrowd ID
url = f'https://judge.beecrowd.com/en/profile/{beecrowc_id}'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Look for "Solved Problems" and its number
# Structure may change; inspect class names if broken
text = soup.get_text()
match = re.search(r'Solved Problems\s+(\d+)', text)

solved = match.group(1) if match else '0'
badge = f'![Beecrowd Stats](https://img.shields.io/badge/Solved-{solved}-brightgreen)'

with open('README.md', 'r') as f:
    md = f.read()

new_md = re.sub(r'!\[Beecrowd Stats\]\(https://img\.shields\.io/badge/Solved-\d+-brightgreen\)', badge, md)

with open('README.md', 'w') as f:
    f.write(new_md)

print(f'✅ Updated solved count to: {solved}')
