import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

URL = "https://judge.beecrowd.com/en/profile/1153590"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Problems solved
solved = soup.find("span", class_="profile-solved-number").text.strip()

# Streak
streak = soup.find("span", class_="profile-solved-streak-text").text.strip()

# Rank
rank = soup.find("span", class_="profile-rank-text").text.strip()

# Create/update stats file
with open("beecrowd_stats.md", "w") as f:
    f.write("## 🐝 Beecrowd Stats\n")
    f.write(f"✅ **Problems Solved:** {solved}\n\n")
    f.write(f"🔥 **Streak:** {streak} days\n\n")
    f.write(f"🏆 **Global Ranking:** {rank}\n\n")
    f.write(f"_Last Updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC_\n")
