import requests
from bs4 import BeautifulSoup
import re

beecrowd_id = '1153590'  # Your Beecrowd ID
profile_url = f'https://judge.beecrowd.com/en/profile/{beecrowd_id}'

response = requests.get(profile_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize default values
solved = '0'
ranking = 'N/A'
streak = '0'

# Extract all profile text
text = soup.get_text()

# Find Solved Problems
solved_match = re.search(r'Solved Problems\s+(\d+)', text)
if solved_match:
    solved = solved_match.group(1)

# Find Global Ranking
rank_match = re.search(r'Ranking\s+(\d+)', text)
if rank_match:
    ranking = rank_match.group(1)

# Find Streak (Consecutive Days)
streak_match = re.search(r'Streak\s+(\d+)', text)
if streak_match:
    streak = streak_match.group(1)

# Print extracted values for confirmation
print(f'✅ Solved: {solved}, Ranking: {ranking}, Streak: {streak}')

# Update README.md with new badges
with open('README.md', 'r') as f:
    content = f.read()

# Replace badges or insert if not present
content = re.sub(r'!\[Beecrowd Solved\]\(https://img\.shields\.io/badge/Solved-\d+-brightgreen\)',
                 f'![Beecrowd Solved](https://img.shields.io/badge/Solved-{solved}-brightgreen)', content)

content = re.sub(r'!\[Beecrowd Ranking\]\(https://img\.shields\.io/badge/Rank-\d+-blue\)',
                 f'![Beecrowd Ranking](https://img.shields.io/badge/Rank-{ranking}-blue)', content)

content = re.sub(r'!\[Beecrowd Streak\]\(https://img\.shields\.io/badge/Streak-\d+-orange\)',
                 f'![Beecrowd Streak](https://img.shields.io/badge/Streak-{streak}-orange)', content)

with open('README.md', 'w') as f:
    f.write(content)
