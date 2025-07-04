import requests
from bs4 import BeautifulSoup
import json

URL = "https://judge.beecrowd.com/en/profile/1153590"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

solved = soup.find("span", class_="profile-solved-number").text.strip()
streak = soup.find("span", class_="profile-solved-streak-text").text.strip()
rank = soup.find("span", class_="profile-rank-text").text.strip()

# Save each stat as a Shields.io-compatible JSON

badge_data = [
    ("badge_solved.json", {"label": "Solved", "message": solved, "color": "brightgreen"}),
    ("badge_streak.json", {"label": "Streak", "message": f"{streak} days", "color": "orange"}),
    ("badge_rank.json", {"label": "Rank", "message": rank, "color": "blue"}),
]

for filename, data in badge_data:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)
